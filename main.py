import requests

SONARQUBE_URL = 'http://localhost:9000'  # Replace with your SonarQube URL
SONARQUBE_USER_TOKEN = "REPLACE_ME" # Replace with your SonarQube User Token

# Define the headers for the API request
headers = {
    'Authorization': 'Bearer ' + SONARQUBE_USER_TOKEN
}

project_info_arr = []
page_index = 1
page_size = 10
running_total = 0
expected_total = 0
do_once = True
print(f"Retreiving all project keys in SonarQube at '{SONARQUBE_URL}'")
while do_once or running_total < expected_total:
    # Make the API request
    search_projects_url = f'{SONARQUBE_URL}/api/projects/search?p={page_index}&ps={page_size}'
    search_response = requests.get(search_projects_url, headers=headers)

    # Check if the request was successful
    if search_response.status_code == 200:
        # Parse the response as JSON
        data = search_response.json()
        expected_total = int(data["paging"]["total"])

        for project_info in data["components"]:
            project_key = project_info["key"]
            project_name = project_info["name"]
            project_info_arr.append({
                "project_key": project_key,
                "project_name": project_name
            })

    else:
        print(f'Search request failed with status code {search_response.status_code}')

    running_total = len(project_info_arr)
    print(f"Retreived {running_total} / {expected_total} projects")
    page_index += 1
    do_once = False

projects_arr = []
for project_info in project_info_arr:
    project_key = project_info["project_key"]
    # Make the API request
    search_project_url = f"{SONARQUBE_URL}/api/measures/component?component={project_key}&metricKeys=ncloc"
    search_project_response = requests.get(search_project_url, headers=headers)
    # Check if the request was successful
    if search_project_response.status_code == 200:
        # Parse the response as JSON
        project_data = search_project_response.json()
        ncloc = 0
        project_name = project_info["project_name"]
        if (len(project_data["component"]["measures"]) > 0):
            ncloc = (project_data["component"]["measures"][0]["value"])
        print(f"Project : {project_key} has {ncloc} lines of code")
        projects_arr.append({
            "project_name": project_name,
            "project_key": project_key,
            "ncloc": ncloc
        })
    else:
        print(f'Failed to get lines of code for project: {project_key} with status code {search_project_response.status_code}')
    
# sort the projects by name in ascending order
projects_arr.sort(key=lambda project: project["project_name"].lower())

# print the project names and their lines of code in csv format
print_csv_format = False
if (print_csv_format):
    print("\n\n")
    print("Project-Name, Project-Key, Lines-of-Code")
    for project in projects_arr:
        print(f"{project['project_name']}, {project['project_key']}, {project['ncloc']}")
    print("\n\n")

# print the total lines of code for all projects
total_ncloc = 0
for project in projects_arr:
    ncloc = int(project["ncloc"])
    total_ncloc += ncloc
print(f'Total lines of code for all projects : {str(total_ncloc)}')
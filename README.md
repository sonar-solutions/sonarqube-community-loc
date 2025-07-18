# SonarQube Community LOC

This Python application retrieves all project keys from a SonarQube instance and calculates the total lines of code (`ncloc`) for all projects. The results are printed in the terminal. 

**Note:** This script should be run by an administrator whose user token has access to all projects in the SonarQube instance to ensure accurate results.

## Legal Disclaimer

**Important Notice:** This tool is designed to provide quick estimates and does not guarantee accuracy for commercial or production use. If further accuracy is needed, please use industry standard tools. This tool is provided for convenience purposes only.

## Prerequisites

- Python 3.9 or higher (if running the script directly)
- Docker (if using the Docker container)

## Configuration

The script uses the following environment variables to connect to the SonarQube instance:

- `SONARQUBE_URL`: The URL of your SonarQube instance (default: `http://localhost:9000`).
- `SONARQUBE_USER_TOKEN`: Your SonarQube User Token.

You can modify these values directly in the `main.py` file.

## Usage

### Option 1: Run the Script Directly

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash
   python main.py
   ```

### Option 2: Use Docker

1. Build the Docker image:

   ```bash
   docker build -t sonarqube-community-loc .
   ```

2. Run the Docker container:

   ```bash
   docker run --rm -it sonarqube-community-loc
   ```

## Output

The script will:

1. Retrieve all project keys from the SonarQube instance.
2. Retrieve the lines of code (`ncloc`) for each project.
3. Print the total lines of code for all projects.

If you want the output in CSV format, you can enable the `print_csv_format` flag in the `main.py` file.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.


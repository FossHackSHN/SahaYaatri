Here is the updated README with the GNU GPL 3 license:

```markdown
# SahaYaatri

SahaYaatri is a project aimed at providing efficient and reliable information about bus routes, schedules, and stations. This repository contains the codebase for data processing and service APIs to support the SahaYaatri platform.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Bus Route Information**: Detailed information about bus routes.
- **Schedule Management**: Up-to-date bus schedules.
- **Station Mapping**: Mapping of bus stations with relevant data.
- **Data Cleaning**: Scripts for cleaning and managing bus route data.

## Installation
To install and set up the project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/FossHackSHN/SahaYaatri.git
    cd SahaYaatri
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To use the SahaYaatri services, run the main application:

```sh
python main.py
```

### Example
To get information about a specific bus route:
```python
import requests

response = requests.get('http://localhost:5000/bus?route_id=123')
print(response.json())
```

## Contributing
We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code follows our coding standards and includes appropriate tests.

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
```

This README provides an overview of the project, instructions for installation, usage examples, guidelines for contributing, and specifies the GNU GPL 3 license.
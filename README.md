# Rayka

## Overview

Rayka is a Django-based application that utilizes AWS DynamoDB to store and retrieve device data. This README provides information on setting up and running the project.

### Prerequisites

Before you can run Rayka, please make sure you have the following prerequisites installed and configured:

1. **AWS CLI**: You need to install the AWS Command Line Interface (CLI) on your system. If you haven't already, you can follow the installation instructions in the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

2. **AWS Configuration**: After installing the AWS CLI, configure it by running the following command and providing your AWS Access Key ID and Secret Access Key:

    ```
    aws configure
    ```

3. **Python Dependencies**: Rayka relies on specific Python packages, which can be installed using `pip` within a virtual environment:

    ```
    python -m pip install -r requirements.txt
    ```

### Running Rayka

Once you've satisfied the prerequisites, you can run Rayka. Follow these steps:

1. **Activate Virtual Environment**: If you haven't already, activate your Python virtual environment where you installed the project dependencies:

    ```
    source <path_to_your_virtual_env>/bin/activate
    ```

2. **Migrate the Database**: Ensure that the database is set up correctly by running Django migrations:

    ```
    python manage.py migrate
    ```

3. **Start the Development Server**: Launch the Django development server:

    ```
    python manage.py runserver
    ```

    The server will start, and you should see output indicating the server is running at a specific URL (e.g., `http://127.0.0.1:8000/`). You can access the API from this URL.

4. **Test Endpoints**: You can test the API endpoints by using tools like [curl](https://curl.se/) or [Postman](https://www.postman.com/) or by sending HTTP requests programmatically.

    - To store a new device model, make a POST request to:
      ```
      POST http://localhost:8000/api/models/
      ```
      Include the JSON data for the device model in the request body.

    - To retrieve a device by its ID, make a GET request to:
      ```
      GET http://localhost:8000/api/devices/{id}/
      ```
      Replace `{id}` with the ID of the device you want to retrieve.


### Test

```
python manage.py test
```

#### Test Coverage
```
coverage run manage.py test
coverage html
```

### Additional Configuration

You can further customize and configure the application by modifying the Django settings in `settings.py`. Additionally, for production deployment, make sure to set up security measures and handle AWS credentials securely.

Feel free to explore the codebase, make improvements, and adapt it to your specific requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Setup Locally

### Prerequisite

- Make sure you have both `Python` and `Pip` installed on your machine before proceeding.

Once the application is cloned successfully, Then navigate to the folder within command line in order to run the commands below.

### Virtual Environment setup

You need to run the commands below within your shell:</br>

- `python3 -m venv ./venv` to install a virtual environment
- `source ./venv/bin/activate` in order to activate the virtual environment
- `pip install -r ./requirements.txt` to install all the dependencies.
  At this stage you should have the application running. However, you need to update the appropriate field/s within the file refer to the sample on `env.example`. for this example, You can just rename the file to `.env` and remove `.example`.

### Running The Application

In the shell, run:

```
make dev-mode
```

The command above, will migrate the database and run the application on `http://127.0.0.1:8000`.

<b>Note: </b> Make sure you have created a user account, So you can use the application. </br>If not you can simply run the command below and follow until you create a `superuser`. Keep in mind that in order to run the command below you must be in the same directory of the cloned project :

```
./manage.py createsuperuser
```

</br>

## Running Test

This will include testing the core functionalities of the application.

```
make dev-test
```

## Docker

Make sure you have Docker and Docker-engine installed and port `8000` is available.

```
make dev-docker
```

Open `http://0.0.0.0:8000` in the browser to test.

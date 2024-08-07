# FastAPI Poetry Starter App

## Local Development Guidelines
1. Clone the repository
2. Navigate to the repository
3. Run `. ./app.sh setup` to setup the project
4. Run `. ./app.sh start dev` to run the application in development mode
5. To import the project in IntelliJ IDEA, follow the steps below:
    - Open IntelliJ IDEA
    - Click on `File` -> Open
    - Select the directory where the repository is cloned
    - Click on Open
    - Configure the project SDK
        - Click on `File` -> `Project Structure`
        - Click on `Platform Settings` -> `SDKs`
        - Click on the `+` icon and `select python SDK`
        - Click `Virtualenv Environment` then click existing environment then click on `...` and navigate to `/fastapi-poetry-starter/.venv/bin/python3.11`
        - Click on `Apply` and then `OK`
        - Then go to `Project Settings` -> `Project`
        - Select the Project SDK as the one you just configured
        - Click on `Apply` and then `OK`
        - The project SDK is now configured
    - The project will be imported, and you can start working on it
    - To run the project from IntelliJ IDEA, you can create a run configuration
        - Click on `Run` from header menu -> `Edit Configurations`
        - Click on the `+` icon and select `Python`
        - Name the configuration and select the script path as `/fastapi-poetry-starter/com/crack/snap/make/app.py`
        - Give `dev` in script parameters
        - Click on `Apply` and then `OK`
        - To debug the project from IntelliJ IDEA, you can click on the `bug icon` to start the server in debug mode

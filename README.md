# FastAPI Sandbox

## Pre-requisites
- Python 3.8 or higher
- Docker

## Getting Started
1. Clone the repository

2. Create a virtual environment

3. Run docker-compose

    ```bash
    $ docker-compose up -d
    ```

4. Setup pgAdmin
    - Open a browser and go to `localhost:8080`
    - Login with the following credentials:
        - Email: `jisun.delosreyes@gmail.com`
        - Password: `password` 
    - Add a new server
        - General
            - Name: `FastAPI Sandbox`
        - Connection
            - Host name/address: `db`
            - Port: `5432`
            - Username: `postgres`
            - Password: `password`
    - Create a new database
        - Right click on `Databases` and select `Create` > `Database`
        - Name: `fastapi-sandbox`

5. Install the requirements

    ```bash
    $ pip install -r requirements.txt
    ```

6. Run the server

    ```bash
    $ uvicorn main:app --reload
    # or 
    $ make run-dev
    ```

# FastAPI Sandbox

## Pre-requisites
- Python 3.8 or higher
- Docker

## Getting Started
1. Clone the repository

2. Create a environment file

    ```bash
    $ cp .env.example .env
    ```

3. Create a virtual environment

4. Run docker-compose

    ```bash
    $ docker-compose up -d
    ```

5. Setup pgAdmin
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
6. Install the requirements

    ```bash
    $ pip install -r requirements.txt
    ```

7. Seed the database

    ```bash
    $ make run-seed
    ```

7. Run the server

    ```bash
    $ uvicorn main:app --reload
    # or 
    $ make run-dev
    ```

## Useful Commands

### Run the server
```bash
    $ uvicorn main:app --reload
    # or
    $ make run-dev 
```

### Reset the database
```bash
    $ make reset-db
```
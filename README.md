## How to start?

- Clone this project (git clone \[repo URL\])
- Remove the .git directory so you can initialize git for your own project. (run the following command inside the project folder `rm -rf .git`)
- Create a virtual environment so you can install all the dependencies in it (EG: `python3 -m venv .venv`)
  - Once the virtual environment is created, enable it by running `source .venv/bin/activate`
  - Install dependencies by running `pip install -r requirements.txt`

## How to set up the database?

This project uses [sqlalchemy](https://www.sqlalchemy.org/) to interact with the database, and [alembic](https://alembic.sqlalchemy.org/en/latest/) for easy database migrations management, to setup the database please follow this steps:

- Create a file called `.env` in the root of the project.
- Copy the content of `.env.example` in the `.env` file and replace the content of each variable with your own values.
  - To generate a secret key you could use the following command `openssl rand -hex 32`.
- Now run the following command to create the migrations `alembic revision --autogenerate -m "create_users_and_tasks_tables"`.
- to update the database with the changes from this migration, please run the following command `alembic upgrade head`.


## How to start the development server?

This is a normal fastapi project, within the dependencies we can find uvicorn, and since the main.py file is under the app/ directory, we'll have to run the command to serve our api this way `uvicorn app.main:app --reload`.

---
Now that you have all this basic setup configured, have fun building something amazing 🖤.

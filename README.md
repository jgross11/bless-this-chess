# generic-group-project

## Setting up the project

1. Download and install Python, Docker Desktop, etc. 

2. Obtain a copy of the `.env` file (contact someone in the project) that contains credentials for various services and place it in `/config`. 

3. Run buildAllWindows.bat in `/config` (non windows users, manually run command within the batch file). This creates a Docker container which runs a MySQL DB instance (and any images that need to be added in the future..).

4. Run createDatabase.py in `/config` with the command `python \.createDatabase.py` - this creates the necessary tables for the project within the db and inserts any relevant test data into the tables.

5. Depending on your Python install / environment, you may or may not have to manually download the modules used in the project (Flask, Jinja, etc.). You can do so using the command `pip install module-name`, provided you have Pip installed. 

## Running the project

Run app.py in `/` with the command `python \.app.py` - if setup was done correctly, the web server will start listening on port 5000. (`localhost:5000`)

Stop running the web server by closing terminal or pressing ctrl (command) + c.

## Project Structure

`config` - contains files that setup the project's environment, typically to be ran once upon initial project setup.

`src` - source files for the project

`src/init` - used to initialize the web server - DB connectivity, credential reading

`src/obj` - data objects used on the backend

`src/view` - front end resources - Jinja templates, CSS

`src/controllers` - back end web controllers 
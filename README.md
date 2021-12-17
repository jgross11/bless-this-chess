# bless-this-chess

## Setting up the project

1. Download and install Python, Docker Desktop, etc. 

2. Obtain a copy of the `.env` file (contact someone in the project) that contains credentials for various services and place it in `/config`. 

3. Run buildAllWindows.bat in `/config` (non windows users, manually run command within the batch file). This creates a Docker container which runs a MySQL DB instance (and any images that need to be added in the future..).

4. Run createDatabase.py in `/config` with the command `python \.createDatabase.py` - this creates the necessary tables for the project within the db and inserts any relevant test data into the tables. This can also be re-ran to initialize a clean working copy of the database, should your testing corrupt it ;)

5. Depending on your Python install / environment, you may or may not have to manually download the modules used in the project (Flask, Jinja, etc.). You can do so using the command `pip install module-name`, provided you have Pip installed. 

## Running the project

Run wsgi.py in `/` with the command `python \.wsgi.py` - if setup was done correctly, the web server will start listening on port 5000. (`localhost:5000`)

Stop running the web server by closing terminal or pressing ctrl (command) + c.

## Project Structure

`config` - contains files that setup the project's environment, typically to be ran once upon initial project setup or to reset environment to clean state.

`docs` - technical documentation which may or may not make sense or be applicable to the end product.

`bless_this_chess` - the meat of the project, where all source files reside. Abbreviated BTC onwards.

`BTC/view` - project wide front end resources (CSS, etc.).

`BTC/routes` - URL routing components.

ex.

`BTC/routes/user` - Contains components necessary to handle user routing requests.

`BTC/routes/user/static` - User routing specific front end resources.

`BTC/routes/user/templates` - User routing specific Jinja templates.

`BTC/routes/user/routes.py` - Backend logic to handle user routing requests.

All `BTC/routes/` subfolders should (probably) be structured similarly. 
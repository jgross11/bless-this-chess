Steps on setting up the project on a local machine

- Download and install python, docker desktop, etc. 

run buildAllWindows.bat in /config (non windows users, manually run command within the batch file)

after docker container created, close command line

start container from within docker desktop - mysql db now running

run createDatabase.py with the command python \.createDatabase.py - this creates the necessary tables for the project within the db and inserts any relevant test data into the tables

run app.py with the command python \.app.py

the web server should start and you should be good to go!

stop running the web server by closing terminal or pressing ctrl (command) + c
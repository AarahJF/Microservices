How to run?
delete the db.sqlite3 file

Open ubuntu terminal
Install python and flask in ubuntu according to the given instruction in this web page
https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/
Go back one directory from the root (cd ..)
Type python (This will open python idle in ubuntu)
Run the following commands in order to connect to database and create tables

from project import db, create_app
app=create_app()
app.app_context().push()
db.create_all()

ctrl+z to exit from python idle

After executing these commands you will be able to see a db.sqlite3 database file created at your root directory.

Next go to your root directory (cd project)
Run the flask application (flask --app __init__ run)
Can access the login system from the given url on the terminal

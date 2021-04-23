# Sixth_Lab
My six python lab
#Task
Implement a REST service (GET / POST / PUT / DELETE operations) for one of the class from laboratory work 3 using Python language tools: Flask Python 3.x
Implement the preservation of a class object from laboratory work 3 in the database using the following process stack SQLAlchemy-1.1.15 MySQL-5.7 / MySQL-8.0 (depending on which database was selected in the 8th work)

#To lounch:
Enter "git clone https://github.com/glodanm/python_lab6 " in console
Create virtual environment being in folder of that project
Activate virtual environment
Install flask_sqlalchemy, flask_marshmallow, marshmallow-sqlalchemy
Being in folder of that project create database: write in terminal "python" then ">>> from car_service import db >>> db.create_all()"
Run flask app
Go to the instrument of API testing, open "http://localhost:5000/entertainment" and test methods GET/POST/PUT/DELETE

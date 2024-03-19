from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.users import User
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Potter"
    user.name = "Harry"
    user.age = 21
    user.position = "magic"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "garrypotter@lox.org"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Goncharov"
    user.name = "Igor"
    user.age = 21
    user.position = "kent"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "igor@mars.org"
    user.set_password(user.hashed_password)
    session.add(user)


def main():
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = 2, 3
    job.start_date = dt.date
    job.is_finished = False


if __name__ == '__main__':
    main()

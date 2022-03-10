from models import Persons, Users


def insert_persons():
    person = Persons(name='Jose', age=35)
    print(person)
    person.save()


def search():
    person = Persons.query.all()
    # person = Persons.query.filter_by(name="Ali").first()
    print(person)


def upgrade_person():
    person = Persons.query.filter_by(name='Ali').first()
    person.age = 38
    person.save()


def delete_person():
    person = Persons.query.filter_by(name='Ali').first()
    person.delete()


def insert_user(login, password):
    user = Users(login=login, password=password)
    user.save()


def verify_users():
    users = Users.query.all()
    print(users)


if __name__ == "__main__":
    insert_user('manuel', '12345')
    insert_user('carolina', '54321')
    verify_users()
    # insert_persons()
    # upgrade_person()
    # delete_person()
    # search()

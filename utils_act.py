from model_sql_test import Activities


def insert_activity():
    activity = Activities(name='jose')
    print(activity)
    activity.save()


def search():
    activity = Activities.query.all()
    # activity = Activities.query.filter_by(name="manuel").first()
    print(activity)


def upgrade_activity():
    activity = Activities.query.filter_by(name='manuel').first()
    activity.save()


def delete_activity():
    person = Activities.query.filter_by(name='Ali').first()
    person.delete()


if __name__ == "__main__":
    # insert_activity()
    # upgrade_activity()
    # delete_activity()
    search()

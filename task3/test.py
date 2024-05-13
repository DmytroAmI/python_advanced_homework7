from datetime import date
from user import User
from user_registration import add_user, show_users, find_user


if __name__ == '__main__':
    first_name = "Dmytro"
    surname = "Dmytrovich"
    last_name = "Dmytrenko"
    birth_date = date(2010, 1, 1)
    email = "dmitriystorchak98@gmail.com"

    new_user = User(last_name, first_name, surname, birth_date, email)
    print("Add new user: ", new_user.get_short_name())

    add_user('users.db', new_user)

    print("Find user:")
    find_user('users.db', first_name, last_name, email)

    print("All users:")
    show_users('users.db')

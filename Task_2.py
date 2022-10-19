import json


FILE_NAME = "phonebook.json"


def save_to_disk(phone_book: dict, file_name) -> None:
    """
    :param phone_book: dict object
    :param file_name: str file_name. Example: phonebook.json
    :return: None
    """
    with open(file_name, 'w') as file:
        json.dump(phone_book, file, indent=4)


def read_from_file(path_to_file: str):
    """
    :param_path_to_file
    :return: dict
    """
    try:
        with open(path_to_file, "r") as book:
            temp = json.load(book)
    except:
        print("No such file")
        return None
    return temp


def add_items(my_book: dict):
    first_name = input("Enter your first name:  ")
    last_name = input("Enter your last name: ")
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone_number: ")
    city = input("Enter your city: ")

    my_book[phone_number] = \
        {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "phone_number": phone_number,
        "city": city
        }
    return my_book


def delete_item(my_book: dict):
    phone_number = input("Enter phone number you want to delete: ")
    try:
        my_book.pop(phone_number)
    except KeyError:
        print("No such phone number in phone book")
        return None


def update_item(my_book: dict):
    while True:
        phone_number = input("Please write your number: ")
        new_phone_number = input("Enter new phone number: ")
        try:
            my_book[phone_number]["phone_number"] = new_phone_number
        except:
            print("!___There is no such number, please enter existing phone number___!")
        continue

    new_first_name = input("Enter new fist name: ")
    new_last_name = input("Please, write  a new last name: ")
    new_full_name = input("Please, write  a new full name: ")
    new_city = input("Please, write  a new city: ")

    if new_city:
        my_book[phone_number]['city'] = new_city
    if new_first_name:
        my_book[phone_number]['first_name'] = new_first_name
    if new_last_name:
        my_book[phone_number]['last_name'] = new_last_name
    if new_full_name:
        my_book[phone_number]['last_name'] = new_full_name
    my_book[new_phone_number] = my_book[phone_number]
    del my_book[phone_number]
    return my_book


def search_phone_number(my_book):
    try:
        search_phone = input("Please enter the phone number of the contact you wanna find: ")
        print(my_book[search_phone])
    except KeyError:
        print("There is no such phone in phonebook")


def search_first_name(my_book):
    try:
        first_name = input("Please enter the first name of the contact you wanna find: ")
        for key in my_book:
            if my_book[key]["first_name"] == first_name:
                print(my_book[key])
    except:
        print("There is no such first name in phonebook")


def search_last_name(my_book):
    try:
        last_name = input("Please enter the last name of the contact you wanna find: ")
        for key in my_book:
            if my_book[key]["last_name"] == last_name:
                print(my_book[key])
    except:
        print("There is no such last name in phonebook")


def search_full_name(my_book):
    try:
        full_name = input("Please enter the full name of the contact you wanna find: ")
        for key in my_book:
            if my_book[key]["full_name"] == full_name:
                print(my_book[key])
    except:
        print("There is no such full name in phonebook")


def search_city(my_book):
    try:
        city = input("Please enter the city of the contact you wanna find: ")
        for key in my_book:
            if my_book[key]["city"] == city:
                print(my_book[key])
    except:
        print("There is no such city in phonebook")


if __name__ == "__main__":
    data = read_from_file(FILE_NAME)
    if data is None:
        data = {}

    while True:
        enter = input("""
        Hi there! Please, choose the option (Enter the number):\n
        - Add new entries - "1"
        - Search by first name - "2" 
        - Search by last name - "3"
        - Search by full name - "4"
        - Search by telephone number - "5"
        - Search by city - "6"
        - Delete a record for a given telephone number - "7"
        - Update a record for a given telephone number - "8"
        - Show the whole phone book - "9"\n
        ! ! ! DON'T FORGET TO _SAVE_ and _EXIT_ - "10" ! ! !\n
        Enter line >>> """)

        if enter == "1":
            add_items(data)
        elif enter == "2":
            search_first_name(data)
        elif enter == "3":
            search_last_name(data)
        elif enter == "4":
            search_full_name(data)
        elif enter == "5":
            search_phone_number(data)
        elif enter == "6":
            search_city(data)
        elif enter == "7":
            delete_item(data)
        elif enter == "8":
            update_item(data)
        elif enter == "9":
            print(data)
        if enter == "10":
            print("See you next time, good luck!")
            save_to_disk(data, FILE_NAME)
            break

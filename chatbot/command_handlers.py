from pathlib import Path

from chatbot.command_parser import read_file
from chatbot.constants import DB_PATH
from chatbot.decorators import check_edit_phone_error, \
    check_empty_contacts_error, check_file_exists, check_add_contacts_error, check_show_phone_error


@check_add_contacts_error
def add_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    contacts[args[0].strip()] = args[1].strip()
    return "Contact added."


@check_empty_contacts_error
def all_contacts(contacts: dict[:str, str]) -> str:
    return "\n".join([name + " - " + phone for name, phone in sorted(contacts.items())])


@check_show_phone_error
def show_phone(args: tuple[str], contacts: dict[str, str]) -> str:
    name = args[0].strip()
    return f"{name} phone is: {contacts[name]}"


@check_edit_phone_error
def change_phone(args: tuple[str, str], contacts: dict[str, str]) -> str:
    contacts[args[0].strip()] = args[1].strip()
    return "Contact updated."


@check_file_exists
def export_contacts(contacts: dict[str, str]) -> str:
    with open(Path(DB_PATH).absolute(), 'w') as f:
        for contact, phone in contacts.items():
            f.write(f"{contact} {phone}\n")

    return "Contacts saved into file."


@check_file_exists
def import_contacts(contacts: dict[str, str]) -> str:
    for row in read_file(Path(DB_PATH).absolute()):
        name, phone = row.split(' ')
        contacts[name.strip()] = phone.strip()

    return "Contacts loaded from file."

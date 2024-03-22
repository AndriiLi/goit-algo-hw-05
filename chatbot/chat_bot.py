from colorama import Fore

from chatbot.command_parser import parse_input
from chatbot.command_handlers import add_contact, change_phone, show_phone, all_contacts, export_contacts, \
    import_contacts
from chatbot.constants import LEVEL_ERROR, LEVEL_WARNING, MESSAGE_LEVELS, INVALID_COMMAND


def print_colored(message: str, color: Fore = Fore.BLUE) -> None:
    if message.startswith(LEVEL_ERROR):
        color = Fore.RED

    if message.startswith(LEVEL_WARNING):
        color = Fore.YELLOW

    for marker in MESSAGE_LEVELS:
        message = message.replace(marker, '').strip()

    print(f"{color}{message}{Fore.RESET}")


def run_chat_bot() -> None:
    contacts = {}
    print_colored("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")

            command, *args = parse_input(user_input)
            match command:
                case "close" | "exit" | "q" | "quit":
                    print_colored("Good bye!")
                    break
                case "hello" | "hi":
                    print_colored("How can I help you?")
                case "add":
                    print_colored(add_contact(args=args, contacts=contacts))
                case "change":
                    print_colored(change_phone(args=args, contacts=contacts))
                case "phone":
                    print_colored(show_phone(args=args, contacts=contacts))
                case "all":
                    print_colored(all_contacts(contacts=contacts))
                case "save":
                    print_colored(export_contacts(contacts=contacts))
                case "load":
                    print_colored(import_contacts(contacts=contacts))
                case _:
                    print_colored(LEVEL_ERROR + " " + INVALID_COMMAND)

        except Exception:
            print_colored(LEVEL_ERROR + " " + INVALID_COMMAND)

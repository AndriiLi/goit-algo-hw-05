from chatbot.constants import LEVEL_ERROR, LEVEL_WARNING, GIVE_NAME_PHONE, GIVE_PHONE, GIVE_NAME, NOT_FOUND, \
    CONTACT_EXISTS, PHONE_NOT_NUMBER


def check_add_contacts_error(func):
    def inner(*args, **kwargs):
        try:
            if len(kwargs['args']) == 0:
                return LEVEL_ERROR + " " + GIVE_NAME_PHONE

            if len(kwargs['args']) == 1:
                return LEVEL_ERROR + " " + GIVE_PHONE

            if not kwargs['args'][1].isdigit():
                return LEVEL_ERROR + " " + PHONE_NOT_NUMBER

            if kwargs['args'][0] in kwargs['contacts'].keys():
                return LEVEL_WARNING + " " + CONTACT_EXISTS

            return func(*args, **kwargs)

        except IndexError:
            return LEVEL_ERROR + " " + GIVE_NAME_PHONE

    return inner


def check_show_phone_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return LEVEL_ERROR + " " + GIVE_NAME

    return inner


def check_empty_contacts_error(func):
    def inner(*args, **kwargs):
        if not len(kwargs['contacts']):
            return LEVEL_WARNING + "Contacts is empty now"

        return func(*args, **kwargs)

    return inner


def check_edit_phone_error(func):
    def inner(*args, **kwargs):
        try:

            if len(kwargs['args']) == 0:
                return LEVEL_ERROR + " " + GIVE_NAME_PHONE

            if len(kwargs['args']) == 1:
                return LEVEL_ERROR + " " + GIVE_PHONE

            if not kwargs['args'][1].isdigit():
                return LEVEL_ERROR + " " + PHONE_NOT_NUMBER

            if kwargs['args'][0] not in kwargs['contacts'].keys():
                return LEVEL_WARNING + " " + NOT_FOUND

            return func(*args, **kwargs)
        except IndexError:
            return LEVEL_ERROR + " " + NOT_FOUND

    return inner


def check_file_exists(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OSError:
            return LEVEL_ERROR + "Wrong path to file"

    return inner

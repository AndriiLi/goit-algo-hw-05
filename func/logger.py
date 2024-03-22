import collections
import re
import sys
from collections import namedtuple
from datetime import datetime
from enum import Enum
from typing import Callable

from colorama import Fore

LoggerRow = namedtuple('LoggerRow', ['datetime', 'level', 'message'])
ErrorLevelItem = namedtuple('ErrorLevel', ['key', 'name', 'color'])


class Commands:
    path = None
    level = None
    sorting = None
    limiting = None


class ErrorLevel(Enum):
    INFO = ErrorLevelItem('INFO', 'INFO', Fore.GREEN)
    ERROR = ErrorLevelItem('ERROR', 'ERROR', Fore.RED)
    DEBUG = ErrorLevelItem('DEBUG', 'DEBUG', Fore.BLUE)
    WARNING = ErrorLevelItem('WARNING', 'WARNING', Fore.YELLOW)


class WrongInputLevelOptions(Exception):
    """" Input wrong level options """


def read_file(path: str, parser_line: Callable[[str], LoggerRow]) -> list[LoggerRow]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                yield parser_line(line)
    except OSError:
        raise ValueError


def parse_log_line(row: str) -> LoggerRow | None:
    try:
        re_level = '|'.join(get_errors_level_list())
        pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (" + re_level + ") (.*)"
        matched_row = re.search(pattern, row).groups()
        return LoggerRow(
            datetime=matched_row[0],
            level=matched_row[1],
            message=matched_row[2]
        )
    except (AttributeError, IndexError):
        return None


def get_errors_level_list() -> list:
    return [level.name for level in ErrorLevel]


def filter_logs_by_level(logs: list[LoggerRow], level: str) -> list:
    return list(filter(lambda x: x.level == ErrorLevel[level].value.name, logs))


def count_logs_by_level(logs: list[LoggerRow]) -> dict:
    levels = [item.level for item in logs]
    return dict(collections.Counter(levels))


def print_separator_row() -> None:
    print(f"{'-' * 40}")


def display_log_counts(counts: dict):
    data = {'Рівень логування': 'Кількість'}
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    data.update(counts)

    print("")
    for key, row in enumerate(data.items()):
        colum1, column2 = row
        if key == 0:
            print(f"{colum1:<20} | {column2:<20}")
            print_separator_row()
        else:
            print(
                f"{ErrorLevel[colum1].value.color}{colum1:<20}{Fore.RESET} | {ErrorLevel[colum1].value.color}{column2:<20}{Fore.RESET}")
    print("")


def sorted_by_time(error: LoggerRow) -> datetime:
    return datetime.strptime(error.datetime, '%Y-%m-%d %H:%M:%S')


def display_log_errors(errors: list[LoggerRow], level: str = None, sorted_by_date: bool = False, limit: int = None):
    if level:
        print(f"\n Деталі логів для рівня {ErrorLevel[level].value.color}{ErrorLevel[level].name}{Fore.RESET}:")
        print_separator_row()

    if limit:
        errors = errors[0: limit]

    for error in sorted(errors, key=sorted_by_time, reverse=sorted_by_date):
        print(f"{error.datetime} {ErrorLevel[error.level].value.color}{error.level}{Fore.RESET} {error.message}")
    print("")


def clear_command(command: str) -> str | None:
    clear = command.strip().lower()
    return clear if clear != '' else None


def command_parser() -> Commands:
    length_commands = len(sys.argv)
    commands = Commands()

    if length_commands >= 2:
        commands.path = clear_command(sys.argv[1])

    if length_commands >= 3:
        clear = clear_command(sys.argv[2])

        if clear.upper() not in get_errors_level_list():
            raise WrongInputLevelOptions

        commands.level = clear.upper()

    if length_commands >= 4:
        commands.sorting = True if clear_command(sys.argv[3]) == 'desc' else False

    if length_commands >= 5:
        commands.limiting = int(clear_command(sys.argv[4]))

    return commands


def print_colored(message: str, color=Fore.RED) -> None:
    print(f"{color} {message} {Fore.RESET}")


def load_logs(path: str, level: str, order: bool = 'asc', limit: int = 5) -> None:
    logs = [row for row in read_file(path, parse_log_line) if row is not None]
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    if level:
        filtered = filter_logs_by_level(logs, level)
        display_log_errors(filtered, level, order, limit)


def show_logs() -> None:
    try:
        commands = command_parser()
        load_logs(commands.path, commands.level, commands.sorting, commands.limiting)

    except (ValueError, TypeError):
        print_colored('Вхідний файл не існує')
    except WrongInputLevelOptions:
        print_colored(
            'Не вірно введенна опция рівень логування оберіть щось з цього ' + " | ".join(get_errors_level_list()))


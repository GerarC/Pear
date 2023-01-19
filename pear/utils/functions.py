import shutil
from rich.table import Table
from rich.align import Align
from rich.console import Console
from ..persistence.archive import Archive
from .styles import *;

console = Console()

def centered_print(text, style = None) -> None:
    '''Prints an object with center alignment.

    Args:
        text (Union[str, Rule, Table]): It's the object to print.
        style (str, Style, Optional): Style of the object. defaults to None.
    '''
    width = shutil.get_terminal_size().columns
    console.print(Align.center(text, style=style, width=width))

def print_archive_table(title: str, archive: list, showtype:bool=False):
    ''' Print a table of the given archive.

    Args:
        title (str): title of the table.
        archive (list): list with the data.
        showtype (bool): lets show the types
    '''
    table = Table(
        title= f'List of {title}',
        title_style='#F2CE00',
        header_style='#E39400',
        style='#E39400 bold',
    )
    table.add_column('Index', style='#E39400')
    table.add_column(title, justify='center')
    if showtype:
        table.add_column('Type', justify='center')
    table.add_column('Seen')
    if not len(archive): centered_print(table)
    else:
        for index, item in enumerate(archive):
            item_type = None
            if item['seen']:
                item_index = f'[#818596][s]{str(index + 1)}[/s][/]'
                item_name = f'[#818596][s]{item["name"]}[/s][/]'
                if showtype:
                    item_type = f'[#818596][s]{item["type"]}[/s][/]'
                item_status = '[#F2CE00][b]✔[/b][/]'
            else:
                item_index = f'[#F2CE00]{str(index + 1)}[/]'
                item_name = f'[#F2CE00]{item["name"]}[/]'
                if showtype:
                    item_type = f'[#F2CE00]{item["type"].capitalize()}[/]'
                item_status = '[#E34400][b]✗[/b][/]'
            if showtype: table.add_row(item_index, item_name, item_type, item_status)
            else: table.add_row(item_index, item_name, item_status)
        centered_print(table)

def show_all_archive(type: str):
    '''Prints a table all the saved items of the given type.

    Args:
        type (str): the type of the archive
    '''
    print_archive_table(type.capitalize(), Archive(type).list_archive())


def add_item(type: str, data: dict) -> None:
    '''Saves the name of the item in the database.

    Args:
        type (str): type of the archive.
        item (dict): item to save.
    '''
    Archive(type).append(data)
    centered_print('Added successfully', SUCCESS)

def item_seen(type: str, index: int) -> None:
    '''Sets as seen the item of the index.

    Args:
        type (str): type of the archive.
        index (int): Index of the item.
    '''
    try:
        Archive(type).set_seen(index - 1)
        centered_print('Set as unseen successfully', SUCCESS)
    except IndexError:
        centered_print('Your index was out of the range', DANGER)
        centered_print('or the archive is empty', DANGER)

def remove_item(type: str, index: int) -> None:
    '''Removes the item of the index.

    Args:
        type (str): type of the archive.
        index (int): Index of the item.
    '''
    try:
        item = Archive(type).delete_by_index(index - 1)
        centered_print(f'[b]{item["name"]}[/b] was removed successfully', SUCCESS)
    except IndexError:
        centered_print('Your index was out of the range', DANGER)
        centered_print('or the archive is empty', DANGER)

def item_unseen(type: str, index: int) -> None:
    '''Sets as unseen the item of the index.

    Args:
        type (str): type of the archive.
        index (int): Index of the item.
    '''
    try:
        Archive(type).set_unseen(index - 1)
        centered_print('Set as unseen successfully', SUCCESS)
    except IndexError:
        centered_print('Your index was out of the range', DANGER)
        centered_print('or the archive is empty', DANGER)

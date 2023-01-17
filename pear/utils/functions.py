import shutil
from rich.rule import Rule
from rich.table import Table
from rich.align import Align
from rich.console import Console
from rich.style import Style
from typer import style

console = Console()

def centered_print(text, style:Style = None) -> None:
    '''Prints an object with center alignment.

    Args:
        text (Union[str, Rule, Table]): It's the object to print.
        style (Style, Optional): Style of the object. defaults to None.
    '''
    width = shutil.get_terminal_size().columns
    console.print(Align.center(text, style=style, width=width))
    
def print_archive_table(title: str, archive: list):
    ''' Print a table of the given archive.

    Args:
        title (str): title of the table.
        archive (list): list with the data.
    '''
    table = Table(
        title= f'List of {title}',
        title_style='#f2ce00',
        header_style='#e39400',
        style='#e39400 bold',
    )
    table.add_column('Index', style='#e39400')
    table.add_column(title, justify='center')
    table.add_column('Seen')
    if not len(archive): centered_print(table)
    else:
        for index, item in enumerate(archive):
            if item['seen']:
                item_name = f'[#818596] [s]{item["name"]}[/s][/]'
                item_status = '[#F2CE00] ✔[/]'
                item_index = f'[#818596] [s]{str(index + 1)}[/s][/]'
            else:
                item_name = f'[#F2CE00] {item["name"]}[/]'
                item_status = '[#E34400] ✗[/]'
                item_index = f'[#F2CE00] {str(index + 1)}[/]'
            table.add_row(item_index, item_name, item_status)
        centered_print(table)


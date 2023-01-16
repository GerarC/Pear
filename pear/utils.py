import shutil
from rich.align import Align
from rich.console import Console
from rich.markdown import Markdown
from rich.rule import Rule
from rich.table import Table
from rich.style import Style

console = Console()

def centered_print(text, style:Style = None) -> None:
    '''prints an object with center alignment.

    Args:
        text (Union[str, Rule, Table]): It's the object to print.
        style (Style, Optional): Style of the object. defaults to None.
    '''
    width = shutil.get_terminal_size().columns
    console.print(Align.center(text, style=style, width=width))

import os
from os.path import expanduser
import typer
from styles import *
from utils import (
    centered_print
)

app = typer.Typer()


@app.callback(invoke_without_command=True)
def recommend_any():
    '''Prints a random Film, Serie, or documentary saved in the Jsons.'''
    centered_print('I recommend you to watch...', INFO)

def recommend(type: str) -> None:
    pass

def addfilm():
    pass

def filmviewed():
    pass

def removefilm():
    pass

def addserie():
    pass

def serieviewed():
    pass

def removeserie():
    pass

def adddoc():
    pass

def removedoc():
    pass

def docviewed():
    pass

def main():
    global config_path
    config_path = os.path.join(expanduser('~'), '.config', 'pear')
    app()

if __name__ == '__main__':
    main()

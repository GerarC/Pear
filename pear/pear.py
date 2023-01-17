import os
import typer
from datetime import datetime
from os.path import expanduser
from json import JSONDecodeError
from rich.markdown import Markdown
from persistence.archive import Archive
from persistence.config import ConfigHandler
from utils.styles import *
from utils.functions import (
    console,
    centered_print,
    print_archive_table,
)

app = typer.Typer()


@app.callback(invoke_without_command=True)
def recommend_any(context: typer.Context):
    '''Prints a random Film, Serie, or documentary saved in the Jsons.'''
    if context.invoked_subcommand is None:
        now_date = datetime.now()
        username = config['username']

        centered_print('I recommend you to watch...', INFO)

@app.command(short_help='recommends a movie')
def recommend(type: str, archive: str = 'movies') -> None:
    pass

@app.command(short_help='shows all the saved films')
def showfilms():
    '''Shows all the save movies.
    '''
    archive = Archive(config['archives'][0]).list_archive()
    print_archive_table('Movies', archive)


@app.command(short_help='adds the film you pass as argument.')
def addfilm(film: str) -> None:
    '''Saves the name of the film in the database.

    Args:
        film (str): film to save.
    '''
    global config
    data = {
        'name': film,
        'seen': False
    }

    archive = Archive(config['archives'][0])
    archive.append(data)
    centered_print('Film added successfully', SUCCESS)

@app.command(short_help='sets the film of an index as seen')
def filmviewed(index: int) -> None:
    '''Sets as seen the film of the index.

    Args:
        index (int): Index of the film.
    '''
    archive = Archive(config['archives'][0])
    try:
        archive.set_seen(index - 1)
        centered_print('Set film as seen successfully', SUCCESS)
    except IndexError:
        centered_print('Your index was out of the range', DANGER)
        centered_print('or the archive is empty', DANGER)

@app.command(short_help='removes film of a given index')
def removefilm(index: int) -> None:
    '''Removes the film of the index.

    Args:
        index (int): Index of the film.
    '''
    archive = Archive(config['archives'][0])
    try:
        archive.delete_by_index(index - 1)
        centered_print('Film was removed successfully', SUCCESS)
    except IndexError:
        centered_print('Your index was out of the range', DANGER)
        centered_print('or the archive is empty', DANGER)

def showseries():
    pass

def addserie():
    pass

def serieviewed():
    pass

def removeserie():
    pass

def showdocs():
    pass

def adddoc():
    pass

def removedoc():
    pass

def docviewed():
    pass

@app.command(short_help='reset the data and run setup.')
def setup() -> None:
    '''Initialize the configuration and save it in the file'''
    config = {}
    config['username'] = typer.prompt(
        typer.style('Hello, What is your name?', fg=typer.colors.BRIGHT_GREEN)
    )
    code_md = Markdown(
        '''
        pear callme <your name>
    ''')
    name = config['username']
    paragraph = [
        f'\nThanks {name}! I\'m pear',
        'I will save your movies,series and documentaries',
        'If you want I will recommend',
        'some of your saved names.'
    ]
    for phrase in paragraph: centered_print(phrase, INFO)
    centered_print('\nIf you want to change your name, you can use:')
    console.print(code_md)
    config['setup_done'] = True
    config['archives'] = [
        'movies',
        'series',
        'documentaries'
    ]
    config_handler.write(config)
    persis_path = os.path.join(
        expanduser('~'), '.config', 'pear', 'library')
    if not os.path.exists(persis_path): os.makedirs(persis_path)
    [Archive(archive) for archive in config['archives']]


def main():
    global config_handler
    config_handler = ConfigHandler()
    try:
        global config
        config = config_handler.load()
    except FileNotFoundError:
        config_handler.create_file()
        typer.run(setup)
    except JSONDecodeError:
        centered_print('There is an error in your ~/.config/pear/config.json file, If you know what is it, you can fix it manually or you can enter your name again.', WARN)
        centered_print('ENTERING YOUR NAME WILL OVERWRITE YOUR CONFIG FILE', DANGER)
        typer.run(setup)
    else:
        if config['setup_done'] is True:
            app()
        else: typer.run(setup)


if __name__ == '__main__':
    main()

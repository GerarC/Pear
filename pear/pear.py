#!/usr/bin/env python
import os
import typer
import random
from os.path import expanduser
from json import JSONDecodeError
from rich.markdown import Markdown
from pear.persistence.archive import Archive
from pear.persistence.config import ConfigHandler
from pear.utils.styles import *
from pear.utils.functions import (
    console,
    centered_print,
    print_archive_table,
    add_item,
    remove_item,
    item_seen,
    item_unseen,
    show_all_archive,
)

app = typer.Typer()


@app.callback(invoke_without_command=True)
def recommend_any(context: typer.Context):
    '''Prints a random Movie, Serie, or documentary saved in the Jsons.'''
    if context.invoked_subcommand is None:
        username = config['username']

        complete_archive = []
        [complete_archive.extend(Archive(type).list_archive()) for type in config['archives']]
        unseen_things = list(filter(lambda item: not item['seen'], complete_archive))
        unseen_amount = len(unseen_things)

        index = random.randint(0, unseen_amount - 1)

        recommendation = unseen_things[index]
        centered_print(f'Hello {username}! I recommend you to watch...', INFO)
        centered_print(f'the next {recommendation["type"]}:', INFO)
        centered_print(f'{recommendation["name"]}', 'bold')


@app.command(short_help='shows all the archive')
def showall(types: bool = True) -> None:
    '''Shows all items of the archives.'''
    complete_archive = []
    [complete_archive.extend(Archive(type).list_archive()) for type in config['archives']]

    print_archive_table('All', complete_archive, showtype=types)

@app.command(short_help='recommends a movie')
def recommend(type: str, archive: str = 'movies') -> None:
    # TODO finish recommend function.
    pass

@app.command(short_help='shows all the saved movies')
def showmovies():
    '''Shows all the saved movies.
    '''
    show_all_archive(config['archives'][0])

@app.command(short_help='adds the movie you pass as argument.')
def addmovie(movie: str) -> None:
    '''Saves the name of the movie in the database.

    Args:
        movie (str): movie to save.
    '''
    data = {
        'name': movie,
        'seen': False,
        'type': 'movie'
    }
    add_item(config['archives'][0], data)

@app.command(short_help='sets the movie of an index as seen')
def seenmovie(index: int) -> None:
    '''Sets as seen the movie of the index.

    Args:
        index (int): Index of the movie.
    '''
    item_seen(config['archives'][0], index)

@app.command(short_help='sets the movie of an index as seen')
def unseenmovie(index: int) -> None:
    '''Sets as seen the movie of the index.

    Args:
        index (int): Index of the movie.
    '''
    item_unseen(config['archives'][0], index)

@app.command(short_help='removes movie of a given index')
def removemovie(index: int) -> None:
    '''Removes the movie of the index.

    Args:
        index (int): Index of the movie.
    '''
    remove_item(config['archives'][0], index)

@app.command(short_help='shows all the saved series')
def showseries():
    '''Shows all the saved movies.
    '''
    show_all_archive(config['archives'][1])

@app.command(short_help='adds the serie you pass as argument.')
def addserie(serie: str) -> None:
    '''Saves the name of the serie in the database.

    Args:
        serie (str): serie to save.
    '''
    data = {
        'name': serie,
        'seen': False,
        'type': 'serie'
    }
    add_item(config['archives'][1], data)

@app.command(short_help='sets the serie of an index as seen')
def seenserie(index: int) -> None:
    '''Sets as seen the serie of the index.

    Args:
        index (int): Index of the serie.
    '''
    item_seen(config['archives'][1], index)

@app.command(short_help='sets the serie of an index as seen')
def unseenserie(index: int) -> None:
    '''Sets as seen the serie of the index.

    Args:
        index (int): Index of the serie.
    '''
    item_unseen(config['archives'][1], index)

@app.command(short_help='removes serie of a given index')
def removeserie(index: int) -> None:
    '''Removes the serie of the index.

    Args:
        index (int): Index of the serie.
    '''
    remove_item(config['archives'][1], index)

@app.command(short_help='shows all the saved documentaries')
def showdocs():
    '''Shows all the saved documentaries.
    '''
    show_all_archive(config['archives'][2])

@app.command(short_help='adds the documentary you pass as argument.')
def adddoc(documentary: str) -> None:
    '''Saves the name of the documentary in the database.

    Args:
        documentary (str): documentary to save.
    '''
    data = {
        'name': documentary,
        'seen': False,
        'type': 'documentary'
    }
    add_item(config['archives'][2], data)

@app.command(short_help='sets the documentary of an index as seen')
def seendoc(index: int) -> None:
    '''Sets as seen the documentary of the index.

    Args:
        index (int): Index of the documentary.
    '''
    item_seen(config['archives'][2], index)

@app.command(short_help='sets the documentary of an index as seen')
def unseendoc(index: int) -> None:
    '''Sets as seen the documentary of the index.

    Args:
        index (int): Index of the documentary.
    '''
    item_unseen(config['archives'][2], index)

@app.command(short_help='removes documentary of a given index')
def removedoc(index: int) -> None:
    '''Removes the documentary of the index.

    Args:
        index (int): Index of the documentary.
    '''
    remove_item(config['archives'][2], index)

@app.command(short_help='changes your name')
def iam(name:str) -> None:
    '''changes your saved name

    Args:
        name (str):
    '''
    if name == '':
        centered_print('Please enter your name!', WARN)
        return
    config['username'] = name
    config_handler.write(config)
    centered_print(f'Ok, now I know that your name is [b]{name}[/b]', SUCCESS)

@app.command(short_help='reset the data and run setup.')
def setup() -> None:
    '''Initialize the configuration and save it in the file'''
    config = {}
    config['username'] = typer.prompt(
        typer.style(
            'Hello, What is your name?',
            fg=typer.colors.BRIGHT_GREEN
        )
    )
    code_md = Markdown('''pear iam <your name>''')
    name = config['username']
    paragraph = [
        f'\nThanks {name}! I\'m pear',
        'I will save your movies, series and documentaries',
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
        expanduser('~'),
        '.config',
        'pear',
        'library'
    )
    if not os.path.exists(persis_path): os.makedirs(persis_path)
    [Archive(archive) for archive in config['archives']]

def main() -> int:
    ''' Main function of the application, loads the configuration.'''
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
        centered_print(
            'ENTERING YOUR NAME WILL OVERWRITE YOUR CONFIG FILE',
            DANGER
        )
        typer.run(setup)
    else:
        app() if config['setup_done'] else typer.run(setup)
    return 0

if __name__ == '__main__': main()

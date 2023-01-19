# Pear

Pear or _**Pe**nding **Ar**chive_ is a CLI application designed
to save the name of movies, series, and documentaries
that you wanna watch later.
And when you call it,
it will recommend any of the saved names in the *Archive*.


### Example

![sample](images/sample.gif)

## Commands

|**Command**|**Description**|
|:---------:|:-------------:|
|`--help`|Show all commands|
|`addmovie`|Add the movie you enter|
|`addserie`|Add the serie you enter|
|`adddoc`|Add the documentary you specify|
|`removemovie`|Remove the movie you specify|
|`removeserie`|Remove the serie you specify|
|`removedoc`|Remove the documentary you enter|
|`seenmovie`|Set as seen the movie|
|`seenserie`|Set as seen the serie|
|`seendoc`|Set as seen the documentary|
|`unseenmovie`|Set as unseen the movie|
|`unseenserie`|Set as unseen the serie|
|`unseendoc`|Set as unseen the documentary|
|`showmovies`|Print a table with all the movies|
|`showseries`|Print a table with all the series|
|`showdocs`|Print a table with all the documentaries|
|`showall`|Print a table with all content|
|`setup`|Init/reboot the configuration|
|`iam`|Change the user name|


## How to Install

If you want to install this project, you can clone it
~~~ bash
git clone https://github.com/GerarC/Pear.git
~~~
Once you've cloned it, install it with pip
~~~ bash
pip install .
~~~

## For the future

I wanna expand this project a little bit more. For example, add an option to import and export markdown files. Here is the list of I wanna do:
- Export to markdown.
- Import from markdown.
- Improve the Archive.
- Let add other archive.
- Let add categories and filter with it.
- Refactor the code, just a little bit.

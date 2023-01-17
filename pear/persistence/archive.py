from .base import JsonDB

class Archive:
    """Archive of the unseen things, here you save and administrate things you want to see.

    Args:
        type (str): name of the Archive
    """

    def __init__(self, type: str) -> None:
        self.type = type
        self.__database = JsonDB([], type)

    def list_archive(self) -> list:
        """List all the items from the database.

        Returns:
            items (list): list of the items.
        """
        items = self.__database.read()
        return items

    def item_by_index(self, index: int) -> dict:
        """Returns the item of the given id.

        Args:
            index (int): index of the wanted item.

        Returns:
            item (dict): object of the index.

        Raises:
            IndexError if the list is empty or the index is out of the range.
        """
        items = self.list_archive()
        items_amount = len(items)
        if 0 <= index < items_amount and items_amount:
            return items[index]
        else: raise IndexError

    def append(self, item: dict) -> None:
        """Appends a item to the data base.

        Args:
            item (dict): the item to append.
        """
        self.__database.append(item)


    def set_seen(self, index: int) -> None:
        """Sets the seen key of the item in true

        Args:
            index (int): index of the seen item.

        Raises:
            IndexError if the list is empty or the index is out of the range.
        """
        items = self.list_archive()
        items_amount = len(items)
        if 0 <= index < items_amount and items_amount:
            items[index]["seen"] = True
            self.__database.write(items)
        else: raise IndexError


    def set_unseen(self, index: int) -> None:
        """Unsets the seen key of the item in true

        Args:
            index (int): index of the unseen item.

        Raises:
            IndexError if the list is empty or the index is out of the range.
        """
        items = self.list_archive()
        items_amount = len(items)
        if 0 <= index < items_amount and items_amount:
            items[index]["seen"] = True
            self.__database.write(items)
        else: raise IndexError

    def delete_by_index(self, index: int) -> dict:
        """Deletes the item of the index.

        Args:
            index (int): index of the item.

        Returns:
            item (dict): the items that was delete form the database.

        Raises:
            IndexError if the list is empty or the index is out of the range.
        """
        items = self.list_archive()
        items_amount = len(items)
        if 0 <= index < items_amount and items_amount:
            item = items.pop(index)
            self.__database.write(items)
            return item
        else: raise IndexError

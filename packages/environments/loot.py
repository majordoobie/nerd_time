class Loot:

    def __init__(self, name: str, desc: str, has_item: bool = False, qty: int = 0):
        self._desc = name
        self._name = desc
        self._has_item = has_item
        self._quantity = qty

    @property
    def name(self):
        """
        Return the name of the loot object
        :return: Name of loot
        :rtype: str
        """
        return self._name
    
    @property
    def description(self):
        return self._desc

    @property
    def exists(self) -> bool:
        """
        Return whether the item has been completely consumed/decremented
        :return: Bool if item exists
        :rtype: bool
        """
        return self._has_item

    def _set_quantity(self) -> None:
        """
        Private method to set the has_item bool

        :return: None
        """
        if (self._quantity > 0) and (self._has_item is False):
            self._has_item = True
        elif (self._quantity < 1) and (self._has_item is True):
            self._has_item = False

    def add_qty(self) -> None:
        """
        Public function to increment the amount of "this" loot

        :return: None
        """
        self._quantity += 1
        self._set_quantity()

    def decrement_qty(self) -> None:
        """
        Public funtion to decrement the amount of "this" item

        :return: None
        :raises ValueError: If an attempt to decrement an item that does not exist, raise error
        """
        if self._has_item is False:
            raise ValueError("Cannot decrement quantity of loot, it does not exist.")

        self._quantity -= 1
        self._set_quantity()


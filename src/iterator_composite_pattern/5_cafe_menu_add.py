from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class ArrayList(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T):
        self.items.append(item)

    def get(self, index: int) -> T:
        return self.items[index]

    def size(self) -> int:
        return len(self.items)


class ArrayListIterator(Iterator[T]):
    def __init__(self, array_list: ArrayList[T]) -> None:
        self.array_list = array_list
        self.index = 0

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if self.index >= self.array_list.size():
            raise StopIteration
        item = self.array_list.get(self.index)
        self.index += 1
        return item


class List(Generic[T]):
    MAX_ITEMS = 6
    NUMBER_OF_ITEMS = 0

    def __init__(self) -> None:
        self.items: list[T | None] = [None] * self.MAX_ITEMS

    def append(self, item: T):
        if self.NUMBER_OF_ITEMS >= self.MAX_ITEMS:
            print("Sorry, menu is full!  Can't add item to menu")
        else:
            self.items[self.NUMBER_OF_ITEMS] = item
            self.NUMBER_OF_ITEMS += 1

    def get_item(self, index: int) -> T:
        if index >= self.NUMBER_OF_ITEMS:
            print("Sorry, out of range")
            raise IndexError
        return self.items[index]  # type: ignore

    def length(self) -> int:
        return len(self.items)


class ListIterator(Iterator[T]):
    def __init__(self, lst: List[T]) -> None:
        self.lst = lst
        self.index = 0

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if self.index >= self.lst.length():
            raise StopIteration
        item = self.lst.get_item(self.index)
        self.index += 1
        return item


class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def __str__(self):
        return f"{self.name}, {self.price} -- {self.description}"


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items: ArrayList[MenuItem] = ArrayList()

        self.add_item(
            "K&B's Pancake Breakfast",
            "Pancakes with scrambled eggs, and toast",
            True,
            2.99,
        )
        self.add_item(
            "Regular Pancake Breakfast",
            "Pancakes with fried eggs, sausage",
            False,
            2.99,
        )
        self.add_item(
            "Blueberry Pancakes",
            "Pancakes made with fresh blueberries, and blueberry syrup",
            True,
            3.49,
        )
        self.add_item(
            "Waffles",
            "Waffles, with your choice of blueberries or strawberries",
            True,
            3.59,
        )

    def add_item(self, name, description: str, vegetarian: bool, price: float) -> None:
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.add(menu_item)

    def create_iterator(self) -> Iterator[MenuItem]:
        return ArrayListIterator(self.menu_items)


class DinerMenu:
    def __init__(self):
        self.menu_items: List[MenuItem] = List()

        self.add_item(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
        self.add_item(
            "BLT",
            "Bacon with lettuce & tomato on whole wheat",
            False,
            2.99,
        )
        self.add_item(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
        self.add_item(
            "Hotdog",
            "A hot dog, with saurkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )
        self.add_item(
            "Steamed Veggies and Brown Rice",
            "Steamed vegetables over brown rice",
            True,
            3.99,
        )
        self.add_item(
            "Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True,
            3.89,
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def create_iterator(self) -> Iterator[MenuItem]:
        return ListIterator(self.menu_items)


class CafeMenu:
    def __init__(self):
        self.menu_items: dict[str, MenuItem] = {}

        self.add_item(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
        self.add_item(
            "Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False,
            3.69,
        )
        self.add_item(
            "Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True,
            4.29,
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items[name] = menu_item

    def create_iterator(self) -> Iterator[MenuItem]:
        return self.menu_items.values()


class Waitress:
    def __init__(self, pancake_house_menu: PancakeHouseMenu, diner_menu: DinerMenu, cafe_menu: CafeMenu):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu
        self.cafe_menu = cafe_menu

    def print_menu(self) -> None:
        pancake_house_menu_iterator = self.pancake_house_menu.create_iterator()
        diner_menu_iterator = self.diner_menu.create_iterator()
        cafe_menu_iterator = self.cafe_menu.create_iterator()

        print("MENU\n----\nBREAKFAST")
        self._print_menu(pancake_house_menu_iterator)
        print("\nLUNCH")
        self._print_menu(diner_menu_iterator)
        print("\nDINNER")
        self._print_menu(cafe_menu_iterator)

    def _print_menu(self, iterator: Iterator[MenuItem]) -> None:
        for menu_item in iterator:
            print(f"{menu_item.get_name()}, {menu_item.get_price()} -- {menu_item.get_description()}")


if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    cafe_menu = CafeMenu()

    waitress = Waitress(pancake_house_menu, diner_menu, cafe_menu)
    waitress.print_menu()

from __future__ import annotations

from abc import ABC
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


class MenuComponent(ABC):
    def add(self, menu_component: MenuComponent):
        raise NotImplementedError

    def remove(self, menu_component: MenuComponent):
        raise NotImplementedError

    def get_child(self, index: int) -> MenuComponent:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError

    def get_price(self) -> float:
        raise NotImplementedError

    def is_vegetarian(self) -> bool:
        raise NotImplementedError

    def create_iterator(self) -> Iterator[MenuComponent]:
        raise NotImplementedError

    def print(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def print(self):
        return f"{self.name}, {'(v) ' if self.vegetarian else ''}{self.price} -- {self.description}"


class Menu(MenuComponent):
    name: str
    description: str
    menu_items: list[MenuComponent]

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.menu_items = []

    def add(self, menu_component: MenuComponent):
        self.menu_items.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self.menu_items.remove(menu_component)

    def get_child(self, index: int) -> MenuComponent:
        return self.menu_items[index]

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def create_iterator(self) -> Iterator[MenuComponent]:
        return iter(self.menu_items)

    def print(self):
        print(f"{self.name}, {self.description}")
        print("---------------------")

        for menu_item in self.create_iterator():
            menu_item.print()


class PancakeHouseMenu(Menu):
    def __init__(self, name, description):
        self.name = name
        self.description = description
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


class DinerMenu(Menu):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
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


class CafeMenu(Menu):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
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
    def __init__(self, all_menus: MenuComponent) -> None:
        self.all_menus = all_menus

    def print_menu(self) -> None:
        self.all_menus.print()


if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = DinerMenu("DINER MENU", "Lunch")
    cafe_menu = CafeMenu("CAFE MENU", "Dinner")

    all_menus = Menu("ALL MENUS", "All menus combined")
    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    waitress = Waitress(all_menus)
    waitress.print_menu()

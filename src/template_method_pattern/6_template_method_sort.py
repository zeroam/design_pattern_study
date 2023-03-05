from __future__ import annotations

from typing import Any, Protocol


class Comparable(Protocol):
    def compare_to(self, other: Any) -> int:
        ...


def bubble_sort(arr: list[Comparable]):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j].compare_to(arr[j - 1]) < 0:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


class Duck(Comparable):
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

    # TODO: mention Liskov Substitution Principle
    def compare_to(self, other: Duck) -> int:
        if self.weight < other.weight:
            return -1
        elif self.weight == other.weight:
            return 0
        else:
            return 1

    def __repr__(self) -> str:
        return f"Duck(name={self.name}, weight={self.weight})"


if __name__ == "__main__":
    ducks = [
        Duck("Daffy", 8),
        Duck("Dewey", 2),
        Duck("Howard", 7),
        Duck("Louie", 2),
        Duck("Donald", 10),
        Duck("Huey", 2),
    ]
    print(bubble_sort(ducks))  # type: ignore

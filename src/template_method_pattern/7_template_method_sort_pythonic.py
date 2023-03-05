from __future__ import annotations


class Duck:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

    def __lt__(self, other: Duck):
        return self.weight < other.weight

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
    print(sorted(ducks))

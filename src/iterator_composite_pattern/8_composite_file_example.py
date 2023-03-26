from __future__ import annotations

import os
from abc import ABC


class FileComponent(ABC):
    def add(self, file_component: FileComponent) -> None:
        raise NotImplementedError

    def remove(self, file_component: FileComponent) -> None:
        raise NotImplementedError

    def get_child(self, i: int) -> FileComponent:
        raise NotImplementedError

    def print(self, depth: int) -> None:
        raise NotImplementedError


class Folder(FileComponent):
    def __init__(self, path: str) -> None:
        self.path = path
        self.children: list[FileComponent] = []
        for item in os.listdir(path):
            if os.path.isdir(os.path.join(path, item)):
                self.children.append(Folder(os.path.join(path, item)))
            else:
                self.children.append(File(os.path.join(path, item)))

    def print(self, depth: int = 0) -> None:
        indent = "- " * depth
        print(f"{indent}Folder, {self.path}")
        for child in self.children:
            child.print(depth + 1)


class File(FileComponent):
    def __init__(self, path: str) -> None:
        self.path = path

    def print(self, depth: int = 0) -> None:
        indent = "- " * depth
        print(f"{indent}File, {os.path.basename(self.path)}")


if __name__ == "__main__":
    folder = Folder("/Users/dante/git/design_pattern_study")
    folder.print()

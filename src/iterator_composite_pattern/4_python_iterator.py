import itertools
from abc import ABCMeta, abstractmethod
from types import GenericAlias


# === Built-in Modules ===#
def _check_methods(C, *methods):
    mro = C.__mro__
    for method in methods:
        for B in mro:
            if method in B.__dict__:
                if B.__dict__[method] is None:
                    return NotImplemented
                break
        else:
            return NotImplemented
    return True


class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            return _check_methods(C, "__iter__")
        return NotImplemented

    __class_getitem__ = classmethod(GenericAlias)


class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        "Return the next item from the iterator. When exhausted, raise StopIteration"
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            return _check_methods(C, "__iter__", "__next__")
        return NotImplemented


# === Built-in Modules ===#


l = list((1, 2, 3, 4, 5))
print(l)
d = dict([("a", 1), ("b", 2), ("c", 3)])
print(d)
t = tuple((1, 2, 3, 4, 5))
print(t)

for item in itertools.chain(l, d.values(), t):
    print(item)


print(issubclass(list, Iterable))
print(issubclass(list, Iterator))

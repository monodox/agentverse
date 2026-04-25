from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def batch(items: Iterable[T], size: int) -> Iterator[list[T]]:
    current: list[T] = []
    for item in items:
        current.append(item)
        if len(current) == size:
            yield current
            current = []
    if current:
        yield current


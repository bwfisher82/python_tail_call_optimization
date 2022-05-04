import sys

from itertools import count


def stack_size(size_hint: int = 8) -> int | None:
    get_frame = sys._getframe
    frame = None
    try:
        while True:
            frame = get_frame(size_hint)
            size_hint *= 2
    except ValueError:
        if frame:
            size_hint //= 2
        else:
            while not frame:
                size_hint = max(2, size_hint // 2)
                try:
                    frame = get_frame(size_hint)
                except ValueError:
                    continue

    for size in count(size_hint):
        frame = frame.f_back
        if not frame:
            return size

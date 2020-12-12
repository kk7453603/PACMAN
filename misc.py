import os
from random import randint


def get_nonzero_random_value(max_abs_value: int) -> int:
    return randint(1, max_abs_value) if randint(0, 1) else randint(-max_abs_value, -1)


def get_image_path(*filepath: str) -> str:
    return os.path.join('images', *filepath)


def get_ghost_path(*filepath: str) -> str:
    return get_image_path('ghost', *filepath)


def get_eyes_path(*filepath: str) -> str:
    return get_ghost_path('crazy_ghost', *filepath)

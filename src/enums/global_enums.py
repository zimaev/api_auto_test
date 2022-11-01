from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Статус код не равен ожидаемому"
    WRONП_COUNT_POSTS = "Количество полученных постов отличается от ожидаемго"

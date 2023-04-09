MINUTES_PER_HOUR = 60
HORS_PER_DAY = 24
SECONDS_PER_MINUTE = 60

SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
SECONDS_PER_DAY = SECONDS_PER_HOUR * HORS_PER_DAY

DRAGON_RARITYS = {
    "c": "COMMON",
    "r": "RARE",
    "v": "VERY_RARE",
    "e": "EPIC",
    "l": "LEGENDARY",
    "h": "HEROIC"
}

DRAGON_ELEMENTS = {
    "w": "sea",
    "p": "nature",
    "f": "flame",
    "d": "dark",
    "e": "terra",
    "el": "electric",
    "m": "metal",
    "i": "ice",
    "wr": "war",
    "l": "legend",
    "li": "light",
    "pu": "pure",
    "bt": "beauty",
    "ch": "chaos",
    "mg": "magic",
    "hp": "happy",
    "dr": "dream",
    "so": "soul",
    "pr": "primal",
    "wd": "wind",
    "ti": "time"
}

__all__ = [
    "DRAGON_ELEMENTS",
    "DRAGON_RARITYS",
    "MINUTES_PER_HOUR",
    "HORS_PER_DAY",
    "SECONDS_PER_MINUTE",
    "SECONDS_PER_HOUR",
    "SECONDS_PER_DAY"
]
#!/usr/bin/env python3
from sys import argv
from pathlib import Path

from packages.game_utils.game_controller import DungeonDudes

ASCII_PATH = "data/.dd_ascii"

def _get_username() -> str:
    """Fetch the users username"""
    print("Enter your desired username for the game:")
    return input("DungeonDudes > ")


def main(dice: bool):
    path = Path(ASCII_PATH)
    if path.exists():
        with path.open("rt", encoding="UTF-8") as infile:
            print(infile.read())

    username = _get_username()
    DungeonDudes(username, dice)


if __name__ == "__main__":
    if len(argv) not in [1, 2]:
        exit("Invalid options used. The only optional argument supported is '--dice'")

    elif len(argv) == 2:
        if argv[1] != "--dice":
            exit("Invalid options used. The only optional argument supported is '--dice'")

    if len(argv) == 1:
        main(dice=False)
    else:
        main(dice=True)




"""
Module is responsible for the game logic. All in game interactions occur here
"""
from collections import namedtuple
from json import load
from pathlib import Path
from random import choice, random
from textwrap import wrap
from typing import List

from packages.characters.hero import Hero
from packages.environments.consumable_loot import ConsumableLoot
from packages.environments.environment import Environment
from packages.game_utils.cli_display import display_no_combat_init, display_hero_bag, display_no_loot, display_battle, \
    display_boarder_attack, display_boarder_attack_end, display_no_combat_start
from packages.game_utils.combat_functions import duel
from packages.game_utils.utils import get_user_input

ENV_FILE = "data/.dd_environments"
EnvironmentRecord = namedtuple("EnvironmentRecord", "name, desc, habitable")


class DungeonDudes:
    def __init__(self, username: str, show_dice=True):
        self._level = 1
        self.hero = Hero(username)
        self.environment_template = _get_environments()
        self._initial = True
        self._show_dice = show_dice
        self._buffs = []
        self.run_game()

    @property
    def level(self) -> int:
        """
        Set difficulty level. This value is used to increase the number of spawns
        :return: level
        """
        return self._level

    @level.setter
    def level(self, value: int):
        self._level = value

    def run_game(self) -> None:
        """
        Run game handles the initial welcoming screen. Control is then handed off the the load_map method
        :return: None
        """
        decision = 0
        if self._initial:
            while decision != 1:
                try:
                    display_no_combat_init(self.hero)
                    decision = get_user_input([1, 2, -1])
                    if decision == -1:
                        self._quit()
                    elif decision == 2:
                        self._show_bag()
                    else:
                        break
                except KeyboardInterrupt:
                    print("[!] If you want to quit, use the provided user interface")

        while not self.hero.is_dead:
            try:
                self._load_map()
            except KeyboardInterrupt:
                print("[!] If you want to quit, use the provided user interface")

    def _quit(self) -> None:
        """
        Called when the use quits or the user dies
        """
        self._show_bag(True)
        print("Thanks for playing!")
        exit()

    def _load_map(self):
        """Responsible for loading the map for the player"""
        map = choice(self.environment_template)
        environment = Environment(map.name, map.desc, map.habitable, self.level)

        # Display map description
        description = environment.description.format(noise=environment.monster_ctrl.monsters[0].noise)
        description = "\n".join(wrap(description, width=80, fix_sentence_endings=True, initial_indent="  ",
                                subsequent_indent="  ", break_long_words=False))
        print("\n", description, "\n")
        input("Press any key to continue...")

        initiative_monster = "Monster has" if environment.monster_ctrl.monster_count == 1 else "Monsters have"
        first_attacker = "Hero has" if environment.initiative.value == 0 else initiative_monster

        while environment.monster_ctrl.monster_count > 0:
            display_battle(self.hero, environment, first_attacker)
            decision = get_user_input([1, 2, 3])
            if decision == 1:
                self._duels(environment)

            elif decision == 2:
                self._show_bag()

            else:
                if random() < self.hero.health * .1:
                    print("[+] Successfully ran away!")
                    return
                else:
                    print("[!] Bummer, you just loss two dice rolls for your next round.")
                    self.hero.dice_count -= 2
                    self._duels(environment)

        self.level += 1
        display_no_combat_start(self.hero, environment)

        decision = 0
        # Keep iterating until user decides to move on
        while decision != 1:
            if environment.has_loot:
                decision = get_user_input([1, 2, 3, -1])
            else:
                decision = get_user_input([1, 2, -1])

            if decision == -1:
                self._quit()
            elif decision == 2:
                self._show_bag()
                display_no_combat_start(self.hero, environment)
            elif decision == 3:
                print("[+] Looted")
                for loot in environment.loot_room():
                    self.hero.set_loot(loot)
                display_no_combat_start(self.hero, environment)
            else:
                return

    def _duels(self, environment: Environment):
        """Responsible for performing the actual duels between attacker and defender"""
        display_boarder_attack()
        for monster in environment.monster_ctrl.monsters:
            if environment.initiative.value == 0:
                duel(self.hero, monster, environment, self._show_dice)
                environment.monster_ctrl.clean_up()
                if monster.is_dead:
                    continue
                duel(monster, self.hero, environment, self._show_dice)
                if self.hero.is_dead:
                    self._quit()
            else:
                duel(monster, self.hero, environment, self._show_dice)
                if self.hero.is_dead:
                    self._quit()
                duel(self.hero, monster, environment, self._show_dice)
                environment.monster_ctrl.clean_up()

        display_boarder_attack_end()
        environment.round += 1
        if self.hero.dice_count == 1:
            self.hero.dice_count = 3
        self.hero.clear_buffs()

    def _show_bag(self, exiting: bool = False):
        """Display the users bag"""
        if self.hero.has_loot:
            junk = [loot for loot in self.hero.loot if not isinstance(loot, ConsumableLoot)]
            consumable = [loot for loot in self.hero.loot if isinstance(loot, ConsumableLoot)]

            display_hero_bag(self.hero, junk, consumable, exiting)
            if exiting:
                return

            options = [index for index in range(0, len(consumable))]
            options.append(-1)
            decision = get_user_input(options)
            if decision == -1:
                return
            else:
                self.hero.consume_loot(consumable[decision])

        else:
            display_no_loot()


def _get_environments() -> List[EnvironmentRecord]:
    """Load the environments from disk to a namedtuple for easy access"""
    env_path = Path(__file__).parent.resolve().parents[1] / Path(ENV_FILE)

    if not env_path.exists():
        raise FileNotFoundError(f"Program requires the environments file to function. Expect "
                                f"file in\n{env_path.as_posix()}")

    environments = []
    try:
        with env_path.open("rt", encoding="utf-8") as infile:
            json = load(infile)
            for environment in json["environments"]:
                environments.append(EnvironmentRecord(**environment))
    except KeyError as error:
        print(f"Key \"{error}\" not found. Invalid file format")
        exit(-1)

    return environments


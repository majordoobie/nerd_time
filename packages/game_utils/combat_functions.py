from typing import List

from packages.characters.character_abstract import Character
from packages.characters.monster import Monster
from packages.environments.environment import Environment


def duel(attacker: Character, defender: Character, env: Environment, display_rolls: bool = False,
         debug: bool = False) -> bool:
    """
    Function handles the individual conflict between a single attacker and single defender. The function determines
    if the attacker is able to land a hit on the defender

    :param env:
    :param display_rolls:
    :param debug: Debugger is only used for running unittests
    :param attacker: Character doing the attacking
    :type attacker: Character
    :param defender: Character doing the defending
    :type defender: Character
    :return: Return if attack was successful
    :rtype: bool
    """
    attack_success = False

    # roll for combat
    if not debug:
        attacker.combat_roll()
        defender.combat_roll()

        if display_rolls:
            print(f"{attacker.name} rolled: [{', '.join(map(str, attacker.combat_rolls))}]")
            print(f"{defender.name} rolled: [{', '.join(map(str, defender.combat_rolls))}]")

    if _is_attack_successful(attacker, defender):
        attack_success = True
        print(f" [HIT] ({attacker.name}) -> hits -> ({defender.name}) for {attacker.damage}!")

        defender.takes_hit(attacker.damage)
        if defender.is_dead:
            print(f"[!] {defender.name} dies with that hit!")

            # add loot to environment if defender is a monster
            if isinstance(defender, Monster):
                if defender.has_loot:
                    print(f"[*] {defender.name} dropped loot!")
                    for loot in defender.loot:
                        env.add_loot(loot)

    else:
        print(f"[MISS] ({attacker.name}) -> misses -> ({defender.name})!")

    print("\n")

    return attack_success


def _is_attack_successful(attacker: Character, defender: Character) -> bool:
    """
    Function iterates over the combat rolls of the duelists and determine if the attacker successfully landed an
    attack.

    :param attacker: Character doing the attacking
    :type attacker: Character
    :param defender: Character doing the defending
    :type defender: Character
    :return: Return if attack was successful
    :rtype: bool
    """
    attack_successful = False

    # get max count to iter
    count = _min_die(attacker.combat_rolls, defender.combat_rolls)

    # Iterate to check if attacker won rolls
    for _round in range(0, count):
        if attacker.combat_rolls[_round] > defender.combat_rolls[_round]:
            attack_successful = True
            break

    return attack_successful


def _min_die(die_list: List[int], die_list2: List[int]) -> int:
    """Return the smallest number of dice of either character"""
    return min(len(die_list), len(die_list2))

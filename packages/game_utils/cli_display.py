"""
Module is responsible for displaying text to the terminal
"""

from math import log10
from textwrap import dedent, wrap
from typing import List

from packages.characters.hero import Hero
from packages.characters.monster import Monster
from packages.environments.consumable_loot import ConsumableLoot
from packages.environments.environment import Environment
from packages.environments.loot import Loot

BOARDER = "-" * 80


def display_no_combat_init(hero: Hero):
    panel = f"""
    Below you will see some of your stats. When you are ready to begin, press 1...
    {BOARDER}
    Your stats:
    Hero:        {hero.name}
    Health:      {hero.health}
    Bag Items:   {hero.loot_count}
    
    Actions:
    --------
    1) Walk into first environment 
    2) Show Bag
    q) Quit
    
    {BOARDER}
    """
    print(dedent(panel))


def display_no_combat_start(hero: Hero, env: Environment):
    loot_nearby = None
    pickup_loot = None
    if env.has_loot:
        loot_nearby = f"Loot Nearby: {env.has_loot}"
        pickup_loot = "3) Pickup loot"

    panel = f"""
    {BOARDER}
    Your stats:
    Hero:         {hero.name}
    Health:       {hero.health}
    Damage:       {hero.damage}
    Dice Count:   {hero.dice_count}
    Pierce Shot:  {'Enabled' if hero.pierce_shot else 'Disabled'}
    Bag Items:    {hero.loot_count}
    {loot_nearby if loot_nearby else ""}

    Actions:
    --------
    1) Enter the next environment 
    2) Show Bag
    {pickup_loot if pickup_loot else ""}
    q) Quit

    {BOARDER}
    """
    print(dedent(panel))


def display_hero_bag(hero: Hero, junk: List[Loot], consumable: List[Loot], exiting: bool = False):
    # calculate the largest space needed for the quantity field
    longest_qty_num = max((loot.quantity for loot in hero.loot))
    qty_space = (int(log10(longest_qty_num)) + 1) + 3

    longest_name = max((len(loot.name) for loot in hero.loot))
    name_space = longest_name + 3

    header = f"{'Index':<5} {'Qty':<{qty_space}} {'Name':<{name_space}} Description"
    action_on = '\n'.join((f"{index:<1}) Consume {loot.name}" for index, loot in enumerate(consumable)))

    _quit = "q) Go back"

    # create list of junks
    junk_items = '\n'.join(
        (f"{'x':<5} {loot.quantity:<{qty_space}} {loot.name:<{name_space}} {loot.description}" for loot in junk))

    # create list of consumables
    consumable_items = '\n'.join(
        (
            f"{index:<5} {loot.quantity:<{qty_space}} {loot.name:<{name_space}} {loot.description}"
            for index, loot in enumerate(consumable)
        )
    )

    panel = f"""
    {hero.name} inventory:
    {BOARDER}
    """
    if not exiting:
        print(dedent(panel), header, junk_items, "", consumable_items, BOARDER, "Choose a potion to consume",
              action_on, _quit, sep="\n")
    else:
        print(dedent(panel), header, junk_items, "", consumable_items, BOARDER, sep="\n")


def display_battle(hero: Hero, env: Environment, initiative: str) -> None:
    monsters_string = "Monster" if env.monster_ctrl.monster_count == 1 else "Monsters"

    monster_list = "\n".join(
        (_monster_format(monster, index + 1) for index, monster in enumerate(env.monster_ctrl.monsters)))

    panel = f"""
    Battle in {env.room_name}
    {initiative} the initiative!
    {BOARDER}
    Round {env.round}:
    
    {hero.name} stats:
    ------------------
        Hero:         {hero.name}
        Health:       {hero.health}
        Damage:       {hero.damage}
        Dice Count:   {hero.dice_count}
        Pierce Shot:  {'Enabled' if hero.pierce_shot else 'Disabled'}
        Bag Items:    {hero.loot_count}
    
    vs.
   
    {monsters_string} stats:
    ------------------------
        {monster_list}
        
    Actions:
    --------
    1) Battle!
    2) Show Bag
    3) Run Away (Chance of success: %{(hero.health * .1) * 100:.0f})
    """
    print(dedent(panel))


def display_no_loot() -> None:
    print("[!] You have no loot to display...\n")
    input("Press enter to continue....")


def display_boarder_attack() -> None:
    print("Attack Log:\n", BOARDER)


def display_boarder_attack_end() -> None:
    print(BOARDER)


def _monster_format(monster: Monster, count: int) -> str:
    return f"""
    Monster {count}
    ----------------
        Monster:    {monster.name}
        Health:     {monster.health}
        Dice Count: {monster.dice_count}
    """

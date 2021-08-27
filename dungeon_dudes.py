from packages.characters.monster import Monster, ImpMonster
from packages.characters.character_abstract import Character


def main():
    imp = ImpMonster("Ivil imp")
    print(f"Imp has loot? {imp.has_loot()}")

    print(isinstance(imp, Character))
    print(isinstance(imp, Monster))
    print(isinstance(imp, ImpMonster))
    print(type(imp))
    print(imp.name)
    print(imp.health)
    print(imp.takes_hit())
    print(imp.health)



if __name__ == "__main__":
    main()

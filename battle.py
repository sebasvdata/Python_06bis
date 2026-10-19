import ex3


def verify(factory: ex3.CreatureFactory) -> None:
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(flame: ex3.CreatureFactory, water: ex3.CreatureFactory) -> None:
    base_flame = flame.create_base()
    base_water = water.create_base()

    print(base_flame.describe())
    print("vs")
    print(base_water.describe())
    print("fight!")

    print(base_flame.attack())
    print(base_water.attack())


def main() -> None:
    flame_factory = ex3.FlameFactory()
    shiftling = ex3.TransformingCreatureFactory()

    print("Testing factory")
    verify(flame_factory)

    print("\nTesting factory")
    verify(shiftling)

    print("\nTesting battle")
    battle(flame_factory, shiftling)


if __name__ == "__main__":
    main()

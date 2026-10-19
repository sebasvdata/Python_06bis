import ex3


def TransformFactory(factory: ex3.TransformingCreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())

    print("evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


def main() -> None:
    transform = ex3.TransformingCreatureFactory()

    print("Testing Creature with transform capability")
    TransformFactory(transform)


if __name__ == "__main__":
    main()

import ex3
import ex4


def battle(
        opponents: list[tuple[ex3.CreatureFactory, ex4.BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f" {len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            entity_a = factory_a.create_base()
            entity_b = factory_b.create_base()

            print(" * Battle *")
            print(entity_a.describe())
            print(" vs.")
            print(entity_b.describe())
            print(" now fight!")

            try:
                print(strategy_a.act(entity_a))
                print(strategy_b.act(entity_b))
            except ex4.InvalidCreatureError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([
        (ex3.FlameFactory(), ex4.NormalStrategy()),
        (ex3.TransformingCreatureFactory(), ex4.AggressiveStrategy()),
    ])

    print("\nTournament 1 (error)")
    print(" [ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([
        (ex3.TransformingCreatureFactory(), ex4.AggressiveStrategy()),
        (ex3.FlameFactory(), ex4.AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from ex3.abs_creature import Creature, TransformCapability


class InvalidCreatureError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise InvalidCreatureError(
                f"Invalid Creature '{creature._name}' "
                "for this aggressive strategy"
            )
        return "\n".join(
            [creature.transform(), creature.attack(), creature.revert()]
        )

from .abs_creature import Creature, TransformCapability, CreatureFactory


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self._is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        if self._is_transformed:
            return "Creature already transformed"
        self._is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        if not self._is_transformed:
            return "Creature is in base form, can't revert"
        self._is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self._is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        if self._is_transformed:
            return "Creature already morphed"
        self._is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        if not self._is_transformed:
            return "Creature is in base form, can't revert"
        self._is_transformed = False
        return "Morphagon stabilizes its form."


class TransformingCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()

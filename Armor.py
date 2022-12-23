class Armor:

    def __init__(self, armor_multiplier, durability, condition) -> None:
        self.multiplier = armor_multiplier
        self.durability = durability
        self.condition = condition

    def effective_durability(self):
        return self.durability * self.multiplier
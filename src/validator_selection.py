import random


class ValidatorSelection:
    def __init__(self, validators):
        self.validators = validators

    def select_validator(self):
        total_stake = sum(self.validators.values())
        pick = random.uniform(0, total_stake)
        current = 0
        for node_id, stake in self.validators.items():
            current += stake
            if current >= pick:
                return node_id

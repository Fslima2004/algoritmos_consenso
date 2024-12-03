import unittest
from src.validator_selection import ValidatorSelection


class TestValidatorSelection(unittest.TestCase):
    def test_select_validator(self):
        validators = {1: 50, 2: 30, 3: 20}
        selection = ValidatorSelection(validators)
        validator = selection.select_validator()
        self.assertIn(validator, validators.keys())


if __name__ == "__main__":
    unittest.main()

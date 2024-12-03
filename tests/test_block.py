import unittest
from src.block import Block


class TestBlock(unittest.TestCase):

    def test_block_creation(self):
        block = Block(index=1, transactions=["tx1", "tx2"], previous_hash="abc123", proposer=2)
        self.assertEqual(block.index, 1)
        self.assertEqual(block.transactions, ["tx1", "tx2"])
        self.assertEqual(block.previous_hash, "abc123")
        self.assertEqual(block.proposer, 2)
        self.assertIsNotNone(block.hash)  # O hash deve ser gerado automaticamente.

    def test_block_hash(self):
        block = Block(index=1, transactions=["tx1"], previous_hash="xyz789", proposer=3)
        calculated_hash = block.calculate_hash()
        self.assertEqual(block.hash, calculated_hash)  # O hash armazenado deve corresponder ao calculado.


if __name__ == "__main__":
    unittest.main()

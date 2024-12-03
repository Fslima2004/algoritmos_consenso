import unittest
from src.blockchain import Blockchain
from src.block import Block


class TestBlockchain(unittest.TestCase):
    def test_add_block(self):
        blockchain = Blockchain()
        genesis_block = Block(index=0, transactions=[], previous_hash="0", proposer=None)
        blockchain.add_block(genesis_block)
        self.assertEqual(len(blockchain.chain), 1)

    def test_invalid_chain(self):
        blockchain = Blockchain()
        block1 = Block(index=0, transactions=[], previous_hash="0", proposer=None)
        block2 = Block(index=1, transactions=[], previous_hash="wrong_hash", proposer=None)
        blockchain.add_block(block1)
        with self.assertRaises(Exception):
            blockchain.add_block(block2)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.node import Node
from src.block import Block


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node(node_id=1, stake=100)
        self.assertEqual(node.node_id, 1)
        self.assertEqual(node.stake, 100)
        self.assertTrue(node.is_active)

    def test_propose_block(self):
        node = Node(node_id=1, stake=100)
        block = node.propose_block(transactions=["tx1"], previous_hash="abc123")
        self.assertEqual(block["proposed_by"], 1)
        self.assertEqual(block["transactions"], ["tx1"])
        self.assertEqual(block["previous_hash"], "abc123")

    def test_validate_block(self):
        node = Node(node_id=1, stake=100)
        block = Block(index=1, transactions=["tx1"], previous_hash="abc123", proposer=2)
        self.assertTrue(node.validate_block(block))


if __name__ == "__main__":
    unittest.main()

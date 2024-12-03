import unittest
from src.network import Network
from src.node import Node


class TestNetwork(unittest.TestCase):
    def test_network_failure(self):
        nodes = [Node(node_id=i, stake=100) for i in range(3)]
        network = Network(nodes)
        network.simulate_failure(1)
        self.assertFalse(nodes[1].is_active)

    def test_network_recovery(self):
        nodes = [Node(node_id=i, stake=100) for i in range(3)]
        network = Network(nodes)
        network.simulate_failure(1)
        network.recover_node(1)
        self.assertTrue(nodes[1].is_active)


if __name__ == "__main__":
    unittest.main()

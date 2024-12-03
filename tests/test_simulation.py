import unittest
from src.simulation import run_simulation


class TestSimulation(unittest.TestCase):
    def test_simulation_runs(self):
        try:
            run_simulation()
        except Exception as e:
            self.fail(f"Simulação falhou com erro: {e}")


if __name__ == "__main__":
    unittest.main()

from .node import Node
from .block import Block
from .blockchain import Blockchain
from .validator_selection import ValidatorSelection
from .network import Network
from .logger import Logger
import random


def run_simulation():

    nodes = [Node(node_id=i, stake=random.randint(10, 100)) for i in range(5)]
    validator_stakes = {node.node_id: node.stake for node in nodes}

    blockchain = Blockchain()
    selector = ValidatorSelection(validator_stakes)
    network = Network(nodes)
    logger = Logger()

    genesis_block = Block(index=0, transactions=[], previous_hash="0", proposer=None)
    blockchain.add_block(genesis_block)
    logger.log_event("Bloco gênese criado.")

    for round in range(1, 6):
        logger.log_event(f"Rodada {round} iniciada.")

        validator_id = selector.select_validator()
        validator_node = next(node for node in nodes if node.node_id == validator_id)

        transactions = [f"Transação {i}" for i in range(random.randint(1, 5))]
        proposed_block = Block(index=round, transactions=transactions,
                               previous_hash=blockchain.chain[-1].hash, proposer=validator_id)

        if all(node.validate_block(proposed_block) for node in nodes if node.is_active):
            blockchain.add_block(proposed_block)
            logger.log_event(f"Bloco {round} validado por {validator_id}.")
        else:
            logger.log_event(f"Bloco {round} rejeitado.")

        if round == 3:
            network.simulate_failure(validator_id)
        if round == 4:
            network.recover_node(validator_id)

    print("\nBlockchain final:")
    print(blockchain)


if __name__ == "__main__":
    run_simulation()

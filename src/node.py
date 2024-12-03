class Node:
    def __init__(self, node_id, stake):
        self.node_id = node_id
        self.stake = stake
        self.is_active = True

    def propose_block(self, transactions, previous_hash):
        if not self.is_active:
            raise Exception(f"Nó {self.node_id} está inativo e não pode propor blocos.")
        return {
            "proposed_by": self.node_id,
            "transactions": transactions,
            "previous_hash": previous_hash
        }

    def validate_block(self, block):
        if not self.is_active:
            raise Exception(f"Nó {self.node_id} está inativo e não pode validar blocos.")
        return block.transactions and block.previous_hash is not None

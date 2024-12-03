import hashlib


class Block:
    def __init__(self, index, transactions, previous_hash, proposer):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proposer = proposer
        self.hash = self.calculate_hash()  

    def calculate_hash(self):
        data = f"{self.index}{self.transactions}{self.previous_hash}{self.proposer}"
        return hashlib.sha256(data.encode()).hexdigest()

    def __repr__(self):
        return f"Bloco {self.index}: {self.hash[:10]}... proposto por {self.proposer}"

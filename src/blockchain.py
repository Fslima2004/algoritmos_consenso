class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        if not self.chain or block.previous_hash == self.chain[-1].hash:
            self.chain.append(block)
        else:
            raise Exception("Bloco inválido: hash do bloco anterior não corresponde.")

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True

    def __repr__(self):
        return "\n".join([str(block) for block in self.chain])

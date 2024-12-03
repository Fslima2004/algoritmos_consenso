class Network:
    def __init__(self, nodes):
        self.nodes = nodes

    def broadcast_message(self, message):
        for node in self.nodes:
            if node.is_active:
                print(f"[Mensagem] Para {node.node_id}: {message}")

    def simulate_failure(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                node.is_active = False
                print(f"Nó {node_id} entrou em falha.")

    def recover_node(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                node.is_active = True
                print(f"Nó {node_id} se recuperou da falha.")

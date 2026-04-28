from src_antigo.models.pedido import Pedido

class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido: Pedido):
        """Adiciona um pedido à lista de pedidos."""
        self.pedidos.append(pedido)

    def processar_pedidos(self):
        """Processa todos os pedidos e calcula o valor final com desconto."""
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")


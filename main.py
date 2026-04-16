from src.models.desconto import DescontoVIP
from src.models.pedido import Pedido

if __name__ == "__main__":
    pedido = Pedido("Alexandre", DescontoVIP())

    valor_final = pedido.valor_final(100.0)
    print(f"Cliente: {pedido.cliente}")
    print(f"Valor final: {valor_final}")
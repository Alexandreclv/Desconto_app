from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController


def build_controller() -> PedidoController:
    database = MemoryDatabase()
    repository = MemoryPedidoRepository(database)
    use_case = CriarPedido(repository)
    return PedidoController(use_case)

def main() -> None:
    controller = build_controller()

    controller.criar_pedido("Cliente A", 100.0, "normal")
    controller.criar_pedido("Cliente B", 200.0, "vip")
    controller.criar_pedido("Cliente C", 300.0, "premium")

    for pedido in controller.listar_pedidos():
        print(
            f"Cliente: {pedido.cliente} | "
            f"Valor original: R$ {pedido.valor_original:.2f} | "
            f"Desconto: R$ {pedido.valor_desconto():.2f} | "
            f"Valor final: R$ {pedido.valor_final():.2f}"
        )

if __name__ == "__main__":
    main()
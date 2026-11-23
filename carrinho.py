from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        if not isinstance(produto, Produto):
            raise TypeError("O produto deve ser uma instância de Produto.")

        if (
            not isinstance(quantidade, int)
            or isinstance(quantidade, bool)
            or quantidade < 1
        ):
            raise ValueError("A quantidade deve ser um inteiro maior ou igual a 1.")

        if produto.nome in self._itens:
            self._itens[produto.nome][1] += quantidade
        else:
            self._itens[produto.nome] = [produto, quantidade]

    def remover(self, nome: str) -> None:
        del self._itens[nome]

    def subtotal(self) -> float:
        valor = sum(
            produto.preco * quantidade
            for produto, quantidade in self._itens.values()
        )
        return round(valor, 2)

    def total_impostos(self) -> float:
        valor = sum(
            produto.imposto() * quantidade
            for produto, quantidade in self._itens.values()
        )
        return round(valor, 2)

    def total(self) -> float:
        return round(self.subtotal() + self.total_impostos(), 2)

    def economia(self) -> float:
        imposto_padrao = sum(
            round(produto.preco * ALIQUOTA_PADRAO, 2) * quantidade
            for produto, quantidade in self._itens.values()
        )
        return round(imposto_padrao - self.total_impostos(), 2)

    def __len__(self) -> int:
        return sum(quantidade for _, quantidade in self._itens.values())

    def __contains__(self, nome: str) -> bool:
        return nome in self._itens


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print("Total:", c.total())
    print("Economia:", c.economia())

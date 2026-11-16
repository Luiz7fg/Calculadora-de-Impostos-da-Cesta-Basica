```python
"""
Semana 2 — O carrinho de compras (Orientação a Objetos: composição)
"""

from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        # Cada nome aponta para [produto, quantidade].
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        """Adiciona um produto ou soma unidades a um cadastro existente."""
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
        """Remove o produto inteiro. Lança KeyError se não existir."""
        del self._itens[nome]

    def subtotal(self) -> float:
        """Soma dos preços de todas as unidades, sem impostos."""
        valor = sum(
            (produto.preco * quantidade
             for produto, quantidade in self._itens.values()),
            0.0,
        )
        return round(valor, 2)

    def total_impostos(self) -> float:
        """Soma o imposto unitário de cada produto vezes sua quantidade."""
        valor = sum(
            (produto.imposto() * quantidade
             for produto, quantidade in self._itens.values()),
            0.0,
        )
        return round(valor, 2)

    def total(self) -> float:
        """Soma do subtotal e dos impostos."""
        return round(self.subtotal() + self.total_impostos(), 2)

    def economia(self) -> float:
        """Diferença entre o imposto pela alíquota padrão e o valor cobrado."""
        imposto_padrao = sum(
            round(produto.preco * ALIQUOTA_PADRAO, 2) * quantidade
            for produto, quantidade in self._itens.values()
        )
        return round(imposto_padrao - self.total_impostos(), 2)

    def __len__(self) -> int:
        """Total de unidades no carrinho."""
        return sum(quantidade for _, quantidade in self._itens.values())

    def __contains__(self, nome: str) -> bool:
        """Verifica se o nome está no carrinho."""
        return nome in self._itens


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print("Total:", c.total())
    print("Economia:", c.economia())
```

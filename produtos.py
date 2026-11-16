"""
Semana 1 — Modelando produtos (Orientação a Objetos)
"""

ALIQUOTA_PADRAO = 0.25  # alíquota padrão hipotética (IBS + CBS)


class Produto:
    """Classe base de todos os produtos do supermercado."""

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self) -> float:
        """Preço do produto SEM imposto."""
        return self._preco

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    def aliquota(self) -> float:
        """Cada subclasse define sua própria alíquota."""
        raise NotImplementedError

    def imposto(self) -> float:
        """Imposto de uma unidade."""
        return round(self.preco * self.aliquota(), 2)

    def preco_final(self) -> float:
        """Preço mais imposto, arredondado em duas casas."""
        return round(self.preco + self.imposto(), 2)

    def __str__(self) -> str:
        return (
            f"{self.nome} - R$ {self.preco:.2f} "
            f"(imposto: R$ {self.imposto():.2f})"
        )


class ProdutoCestaBasica(Produto):
    """Item da Cesta Básica Nacional com alíquota zero."""

    def aliquota(self) -> float:
        return 0.0


class ProdutoReduzido(Produto):
    """Alimento que paga 40% da alíquota padrão."""

    def aliquota(self) -> float:
        return ALIQUOTA_PADRAO * 0.40


class ProdutoPadrao(Produto):
    """Produto que paga a alíquota padrão."""

    def aliquota(self) -> float:
        return ALIQUOTA_PADRAO


if __name__ == "__main__":
    # Área livre para testes manuais
    arroz = ProdutoCestaBasica("Arroz 5kg", 25.90)
    refri = ProdutoPadrao("Refrigerante 2L", 9.00)
    print(arroz)
    print(refri)

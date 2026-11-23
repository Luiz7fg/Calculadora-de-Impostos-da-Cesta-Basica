ALIQUOTA_PADRAO = 0.25


class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    def aliquota(self) -> float:
        raise NotImplementedError

    def imposto(self) -> float:
        return round(self.preco * self.aliquota(), 2)

    def preco_final(self) -> float:
        return round(self.preco + self.imposto(), 2)

    def __str__(self) -> str:
        return (
            f"{self.nome} - R$ {self.preco:.2f} "
            f"(imposto: R$ {self.imposto():.2f})"
        )


class ProdutoCestaBasica(Produto):
    def aliquota(self) -> float:
        return 0.0


class ProdutoReduzido(Produto):
    def aliquota(self) -> float:
        return ALIQUOTA_PADRAO * 0.40


class ProdutoPadrao(Produto):
    def aliquota(self) -> float:
        return ALIQUOTA_PADRAO


if __name__ == "__main__":
    arroz = ProdutoCestaBasica("Arroz 5kg", 25.90)
    refri = ProdutoPadrao("Refrigerante 2L", 9.00)
    print(arroz)
    print(refri)

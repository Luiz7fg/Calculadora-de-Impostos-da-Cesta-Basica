from collections import namedtuple


ALIQUOTA_PADRAO = 0.25
ALIQUOTAS = {
    "cesta_basica": 0.0,
    "reduzido": 0.10,
    "padrao": ALIQUOTA_PADRAO,
}

Item = namedtuple("Item", ["nome", "preco", "categoria", "quantidade"], defaults=[1])


def aliquota(categoria):
    try:
        return ALIQUOTAS[categoria]
    except KeyError:
        raise ValueError(f"Categoria inválida: {categoria!r}.") from None


def imposto_item(item):
    imposto_unitario = round(item.preco * aliquota(item.categoria), 2)
    return round(imposto_unitario * item.quantidade, 2)


def total_impostos(itens):
    return round(sum(map(imposto_item, itens), 0.0), 2)


def total_compra(itens):
    subtotal = sum(item.preco * item.quantidade for item in itens)
    return round(subtotal + total_impostos(itens), 2)


def filtrar_por_categoria(itens, categoria):
    return list(filter(lambda item: item.categoria == categoria, itens))


def ordenar_por_preco(itens, decrescente=False):
    return sorted(itens, key=lambda item: item.preco, reverse=decrescente)


def economia_total(itens):
    imposto_padrao = sum(
        round(item.preco * ALIQUOTA_PADRAO, 2) * item.quantidade
        for item in itens
    )
    return round(imposto_padrao - total_impostos(itens), 2)


def criar_calculadora(aliquota_padrao):
    if aliquota_padrao < 0:
        raise ValueError("A alíquota padrão não pode ser negativa.")

    taxas = {
        "cesta_basica": 0.0,
        "reduzido": aliquota_padrao * 0.40,
        "padrao": aliquota_padrao,
    }

    def calcular(item):
        try:
            taxa = taxas[item.categoria]
        except KeyError:
            raise ValueError(f"Categoria inválida: {item.categoria!r}.") from None

        imposto_unitario = round(item.preco * taxa, 2)
        return round(imposto_unitario * item.quantidade, 2)

    return calcular


def compor(*funcoes):
    from functools import reduce

    def composta(valor):
        return reduce(
            lambda resultado, funcao: funcao(resultado),
            reversed(funcoes),
            valor,
        )

    return composta


def gerar_relatorio(itens):
    return {
        "por_categoria": {
            categoria: total_compra(filtrar_por_categoria(itens, categoria))
            for categoria in ALIQUOTAS
        },
        "total_impostos": total_impostos(itens),
        "total": total_compra(itens),
        "economia": economia_total(itens),
    }

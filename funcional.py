Chefe, a opção de salvar direto na `main` está certa. **Clica em Cancel primeiro**. Pelo print, o editor atrás da janela parece estar vazio.

Cole este código no editor do **`funcional.py`**:

```python
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
```

Depois, abra **Commit changes** de novo, escreva `Completa a Semana 3` no campo **Commit message**, deixe a primeira opção marcada e clique no botão verde. Na aba **Actions**, confira o resultado dos testes da Semana 3.

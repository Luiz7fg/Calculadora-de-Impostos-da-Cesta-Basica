# Respostas — Reflexão sobre os paradigmas

**Nome:** Luiz Eduardo Freire Gonçalves  
**Matrícula:** 2528451

## 1. Orientação a objetos

A principal vantagem foi concentrar na classe `Produto` a validação do preço e o cálculo do imposto. Cada subclasse define sua própria alíquota e reaproveita o cálculo da classe base. O `Carrinho` guarda os produtos e suas quantidades e calcula os totais da compra. A maior dificuldade foi usar o setter no construtor para validar o preço desde a criação e somar as quantidades quando um produto com o mesmo nome já estava no carrinho.

## 2. Programação funcional

A vantagem foi dividir o cálculo em funções que posso testar separadamente. `map` aplica o cálculo de imposto aos itens, `filter` seleciona os itens de uma categoria e `sorted` devolve uma lista ordenada sem modificar a original. A maior dificuldade foi combinar essas operações sem laços explícitos e entender a ordem em que `compor` aplica as funções. Por exemplo, `compor(f, g)(x)` executa `g(x)` primeiro e passa o resultado para `f`.

## 3. Comparação

Uma redução de 30% faria o produto pagar 70% da alíquota padrão. Com a alíquota de 25% usada no trabalho, a nova taxa seria de 17,5%.

Na versão orientada a objetos, eu criaria uma subclasse de `Produto` cujo método `aliquota()` retornaria `ALIQUOTA_PADRAO * 0.70`. O carrinho já conseguiria calcular o imposto dessa nova categoria usando o mesmo método.

Na versão funcional, eu adicionaria a categoria ao dicionário `ALIQUOTAS` e também ao dicionário de taxas de `criar_calculadora`. O relatório incluiria a categoria automaticamente porque percorre as chaves de `ALIQUOTAS`. Na implementação atual, a versão com classes seria mais fácil de alterar porque a nova regra ficaria em um único lugar.

## 4. Alíquota zero

O produto da cesta básica executa `imposto()` porque sua regra é aplicar uma alíquota de 0% ao preço. Por exemplo, para um arroz de R$ 25,90, `round(25.90 * 0.0, 2)` retorna `0.0`. Assim, o carrinho pode chamar o mesmo método para todos os produtos, e cada produto usa a alíquota da sua categoria.

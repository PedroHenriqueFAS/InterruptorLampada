# InterruptorLampada

## Problema

Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem duas lâmpadas. Vamos chamá-las de A e B. No hotel há dois interruptores, que chamaremos de I1 e I2. Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver apagada e apaga se estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado. As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você. Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado final das lâmpadas A e B.

Entrada
A primeira linha contém um número N que representa quantas vezes seu amigo irá apertar algum interruptor. Nas linhas seguintes seguirão números, que pode ser 1, se o interruptor I1 foi apertado, ou 2, se o interruptor I2 foi apertado.

Saída
Seu programa deve imprimir dois valores, em linhas separadas. Na primeira linha, imprima 1 se a lâmpada A estiver acesa no final das operações e 0 caso contrário. Na segunda linha, imprima 1 se a lâmpada B estiver acesa no final das operações e 0 caso contrário.

## Descrição
Este programa em Python recebe um número inteiro `n`, seguido de `n` valores inteiros. Dependendo dos valores fornecidos, ele alterna os estados de duas variáveis booleanas (`l1` e `l2`).

## Pré-requisitos
- Python 3 instalado em seu sistema.

2. No terminal, execute o seguinte comando:
   ```bash
   python script.py
   ```
3. Insira os valores conforme solicitado.

## Exemplo de Entrada e Saída

### Entrada:
```
5
1
2
1
2
1
```

### Processamento:
- `1` -> Alterna `l1` (True)
- `2` -> Alterna `l1` (False) e `l2` (True)
- `1` -> Alterna `l1` (True)
- `2` -> Alterna `l1` (False) e `l2` (False)
- `1` -> Alterna `l1` (True)

### Saída:
```
1
0
```

## Observações
- O código utiliza lógica simples para alternar estados booleanos.
- Pode ser adaptado para outras aplicações que envolvem alternância de estados.

## Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificar e distribuir conforme necessário.

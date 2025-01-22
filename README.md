Não sei muito bem o que colocar em um arquivo README. Perdoe se ele acabar ficando meio confuso.

A criação desse programa veio de um desavio que meu professor de programação da faculdade de Ciência da Computação me propoz. Como envolve bastante manipulação de lista e MUUUITA matemática, 
foi um desafio divertido de fazer. Indo atrás de como é gerado um, me deparei no site [[https://atitudereflexiva.wordpress.com/2021/05/05/entenda-como-e-gerado-o-numero-do-cpf/]], onde explica
perfeitamente a matemágica por trás da criação. \
Um resumo:

xxx.xxx.xxR-YZ \
Os números nas posições 'x' são gerados aleatóriamente. Provávelmente deve ter uma lógica por trás das escolhas de certos padrões, mas eles em sí podem ser aleatórios. \
O número 'R' varia conforme a região que foi criado. Se você nasceu no Paraná ou em Santa Catarina, seu 9° dígito será '9'. A lista das regiões está no link acima. \
A magia acontece nos digitos Y e Z. Eles são números "verificadores", criados a partir de uma conta maluca. \
    ->  Primeiro é feito a soma: (primeiro digito * 10) + (segundo digito * 9) + (terceiro digito * 8) + ... + (nono dígito * 2); \
    -> O resultado dessa soma é dividida por 11 e pego o resto da divisão. Se `resto <= 1`, então o número é `0`, se não, é o resultado de `11 - resto`; \
    -> Depois de descoberto o 'Y', é feito o mesmo tipo de soma, porém com um dígito pra frente: \
            (segundo digito * 10) + (terceiro digito * 9) + (quarto digito * 8) + ... + (décimo dígito * 2); \
    -> Repete a etapa da divisão. 
  
Então no caso do CPF 123.456.789-YZ:\
  -> $(1 \times 10) + (2 \times 9) + (3 \times 8) + (4 \times 7) + (5 \times 6) + (6 \times 5) + (7 \times 4) + (8 \times 3) + (9 \times 2) = 210$ \
  -> $210 \\% 11 = 1$ \
  -> $Y = 0$

  -> $(2 \times 10) + (3 \times 9) + (4 \times 8) + (5 \times 7) + (6 \times 6) + (7 \times 5) + (8 \times 4) + (9 \times 3) + (0 \times 2) = 244$ \
  -> $244 \\% 11 = 2$ \
  -> $Z = 11 - \text{resto} = 11 - 2 = 9$

**Resultado:** 123.456.789-09

Enfim, bem chato, né? Por isso automatizei essa bagaça. É uma matemágica muito genial, mas beem complicada de fazer na mão. Por sorte, tudo isso que você viu pode ser programado assim:
```
x = 10
for i in range(0 if len(cpf) == 9 else 1, 9 if len(cpf) == 9 else 10):
  soma += (cpf[i] * x)
  x = x - 1

resto = soma % 11
if resto > 1:
    validador = 11 - resto
elif resto <= 1:
    validador = 0
```

A primeira versão do programa apenas validava se o CPF está correto, retornando um booleano. Porém, principalmente no meu trampo, me deparava com situações em que o CPF estava incorreto
por conta de um erro na hora de escrever, ouviu '6' e escreveu '7', enfim. O que eu sempre fazia era indo dígito por dígito e testando as possibilidades até achar a correta.
Foi aí que caiu a ficha: o que eu estava fazendo era um simples "for", coisa que o meu próprio programa poderia fazer também...

Lhe apresento a versão 3.3 da Validacao-cpf.py: onde você digita um CPF e, se errou 1 digíto, trocou dois dígitos de lugar (tipo, em vez de 123, digitou 132), ele vai fazer várias validações e mostrar
possíveis resultados.

Vale a pensa ressaltar que: meu programa somente faz uma conta por cima de uma sequência de números. Em nenhum momento tive o intuito de salvar ou utilizar os CPFs de maneira imprópria.

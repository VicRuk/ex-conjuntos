# Exercício 1 - Conjuntos
Exercício da disciplina: Resolução de Problemas de Natureza Discreta<br><br>

<h1>INSTRUÇÕES</h1>
Na pasta 'entradas', coloque arquivos .txt (pode ser o quanto quiser) para o código detectar e realizar os cálculos. Ao colocar os arquivos, rode o programa Python 'main.py'. O resultado sairá no terminal e em outros arquivos .txt dentro da pasta 'resultado'.<br><br>

<h1>ENUNCIADO</h1>
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.<br>
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:<br><br>

![image](https://github.com/user-attachments/assets/cb144a37-3597-4849-8716-0750f9dbb7e9)<br><br>

Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e {𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).<br>
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir:<br>
<b>União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}</b><br>
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima. <br>
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.

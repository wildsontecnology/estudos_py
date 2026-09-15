# 1. Comentários: Este é um arquivo de exemplo para demonstrar conceitos básicos em Python, os comentários são iniciados com o símbolo 
# # e não são executados pelo interpretador.
#  Eles são usados para explicar o código e torná-lo mais legível.

"""
O que está entre aspas triplas é uma string de documentação (docstring) 
que pode ser usada para fornecer informações sobre o módulo, 
função ou classe.

"""

'''
2. Função Print: A função print() é usada para exibir informações 
na saída padrão (geralmente o console).

'''

# Exemplo 1:
print("Olá, mundo!")  # Exibe a mensagem "Olá, mundo!" no console.

# Dentro da função print(), você pode passar múltiplos 
# argumentos separados por vírgulas, e eles serão exibidos 
# na mesma linha, separados por espaços.

# Exemplo 2:
print("Python", "é", "uma", "linguagem", "de", "programação.")  # Exibe várias palavras na mesma linha.
print(12,13,14, sep=" - ")  # Exibe os números separados por " - ".

'''
 Tipos de argumentos que podem ser passados para a função print():
- Strings: Sequências de caracteres, como "Olá, mundo!".
- Números: Inteiros (int) e números de ponto flutuante (float), como 42 ou 3.14.
- Variáveis: Você pode passar variáveis que armazenam valores.
- Listas e tuplas: Estruturas de dados que podem conter múltiplos valores.
- Dicionários: Estruturas de dados que armazenam pares chave-valor.
- Objetos: Instâncias de classes definidas pelo usuário.
- Funções: Você pode passar o resultado de funções que retornam valores.
- Expressões: Qualquer expressão que produza um valor,
  como operações matemáticas ou chamadas de função.
- sep: Um argumento opcional que define o separador entre os valores passados para print().
- end: Um argumento opcional que define o que será impresso no final da linha (por padrão, é uma nova linha).
- file: Um argumento opcional que define o arquivo onde a 
  saída será escrita (por padrão, é sys.stdout).
- flush: Um argumento opcional que, se definido como True, 
força a saída a ser escrita imediatamente.  

'''

'''

3. Tipos de dados:

Python: Tem tipagem Dinâmica e forte, 
o que significa que você não precisa declarar o tipo de uma variável 
explicitamente, e o tipo é determinado automaticamente 
com base no valor atribuído.

A) Strings: Sequências de caracteres, como "Olá, mundo!".

B) Números: Inteiros (int) e números de ponto flutuante (float), 
como 42 ou 3.14.

C) Listas: Estruturas de dados que podem conter múltiplos valores,  
como [1, 2, 3] ou ["maçã", "banana", "laranja"].

D) Tuplas: Estruturas de dados imutáveis que podem 
conter múltiplos valores,
como (1, 2, 3) ou ("maçã", "banana", "laranja").

E) Dicionários: Estruturas de dados que armazenam pares chave-valor,
como {"nome": "Alice", "idade": 30}.

F) Booleanos: Valores lógicos True ou False, usados para controle 
de fluxo e condições.

G) Conjuntos: Estruturas de dados que armazenam valores únicos,
como {1, 2, 3} ou {"maçã", "banana", "laranja"}.

H) None: Um tipo especial que representa a ausência de valor ou
a falta de um objeto, usado para indicar que uma variável não
tem valor atribuído.

I) Tipos de dados compostos: Python também permite a criação de 
tipos de dados compostos, como listas de listas, dicionários de listas,
tuplas de dicionários, etc., permitindo a construção de estruturas

J) Tipos de dados personalizados: Você pode criar seus próprios tipos
de dados definindo classes, permitindo a modelagem de objetos 
e comportamentos específicos.

H) Tipos de dados imutáveis e mutáveis: Alguns tipos de dados, como
strings e tuplas, são imutáveis, o que significa que 
seus valores não podem ser alterados após a criação. Outros tipos, 
como listas e dicionários, são mutáveis, permitindo
a modificação de seus valores.

'''
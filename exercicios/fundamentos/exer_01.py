# Exibir nome, sobrenome, idade, ano de nascimento, maior de idade? altura

name = "Wildson"
surname = "Romeu"
age = 34
birth_year = 1991
height = 1.70
major_of_age = age >= 18  # Verifica se a pessoa é maior de idade.

print("Nome:", name)
print("Sobrenome:", surname)
print("Idade:", age)
print("Ano de Nascimento:", birth_year)
print(f"Altura: {height}") #usando f-string para exibir a altura
print("Maior de idade?", major_of_age)  # Exibe True se a pessoa for maior de idade, caso contrário, exibe False.
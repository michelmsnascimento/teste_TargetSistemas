"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

palavra = input("Digite uma palavra: ")
novaString = ""

index = len(palavra)
while index:
        index = index - 1                 
        novaString = novaString + palavra[index] 
    
print(novaString)

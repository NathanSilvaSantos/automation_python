# Exemplo de utilização do pipe | em expressões regulares
# Podemos usá-lo em qualquer lugar em que quisermos fazer a correspondência de uma entre várias expressões.
import re

# Irá sempre retornar a primeira ocorrência encontrada
heroRegex = re.compile(r'Batman|Superman')
mo1 = heroRegex.search('Batman vs Superman')
# Imprime Batman pois foi o primeiro encontrado
print(mo1.group())

# Imprime Superman pois foi o primeiro encontrado
mo2 = heroRegex.search('Superman and Batman')
print(mo2.group())
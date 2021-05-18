import re

# Podemos utilizar o caractere ? para marcar um grupo
# como sendo uma parte opicional do padrão buscado
batRegex = re.compile(r'Bat(wo)?man')
batman = batRegex.search("Batman begins")
print(batman.group())

batwoman = batRegex.search('The adventures of Batwoman')
print(batwoman.group())
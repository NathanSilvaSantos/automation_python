import re

# Podemos utilizar o caractere ? para marcar um grupo
# como sendo uma parte opicional do padrão buscado
batRegex = re.compile(r'Bat(wo)?man')
# o caractere sempre vai se referir ao grupo que antecede a ele
# comoo sendo um parametro opicional dentro do padrão
batman = batRegex.search("Batman begins")
print(batman.group())

batwoman = batRegex.search('The adventures of Batwoman')
print(batwoman.group())

# Usando * temos o mesmo efeito, porém ele se aplica caso o grupo
# apareça mais vezes no texto
newBatRegex = re.compile(r'Bat(wo)*man')
mo = newBatRegex.search('The adventures of Batwowowowoman')
print(mo.group())

# Com o caractere + o grupo não é opicional e deve aparecer ao
# menos uma vez na string

superRegex = re.compile(r'Super(wo)+man')
superwoman = superRegex.search('The New Superwoman')
print(superwoman.group())
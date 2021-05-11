# Verificar se uma string é um número de telefone
# de acordo com o padrão brasileiro (00)00000-0000

# Permite a criação de expressões regulares
import re

message = "Meu número é (19)99999-0000."

# Retorna um objeto regex de acordo com o padrão
phoneNumRegex = re.compile(r'\(\d{2}\)\d{5}-\d{4}') 

# Procura por um número dentro da string. De acordo com o padrão especificado
matchNumber = phoneNumRegex.search(message)

print("Número de telefone encontrado: " + matchNumber.group())
        
print("Finalizado")
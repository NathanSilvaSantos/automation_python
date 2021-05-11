# Verificar se uma string é um número de telefone
# de acordo com o padrão brasileiro (00)00000-0000

# Permite a criação de expressões regulares
import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True


message = "Meu número é (19)99999-0000."

phoneNumRegex = re.compile(r'\(\d{2}\)\d{5}-\d{4}') # Retorna um objeto regex de acordo com o padrão

matchNumber = phoneNumRegex.search(message)

print("Número de telefone encontrado: " + matchNumber.group())
        
print("Finalizado")
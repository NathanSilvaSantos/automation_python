# Verificar se uma string é um número de telefone
# de acordo com o padrão estadunidense 000-000-0000

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


message = "Me ligue em 415-555-1011 amanhã. 415-555-9999 é meu escritório"

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Número de telefone encontrado: " + chunk)
        
print("Finalizado")
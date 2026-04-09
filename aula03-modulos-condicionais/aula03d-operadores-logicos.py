# Logica E (and) / precisa que as duas consdições sejam atendidas para ser True

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Loga certo ai sua menina...")

# Logica OR (OU) / precisa que uma das condições sejam atendidas para ser True
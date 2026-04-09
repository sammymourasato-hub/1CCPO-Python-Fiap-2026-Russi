# CONDICIONAIS IF(se)/ELSE(se não)
nota_final = 7

if nota_final < 4:
    print("Reprovado")

else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("FIM")

# Algortimo bom
nota_final = 7

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")
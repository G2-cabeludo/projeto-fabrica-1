nome = input("digite seu nome: ")

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_media(media):
    if media >= 7.0:
        return "Aprovado(a) ✅"
    elif media >= 5.0 and media < 7.0:
        return "Recuperação ⚠️"
    else:
        return "Reprovado(a) ❌"
def executar_calculo():
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    nota3 = float(input("digite sua terceira nota: "))
    nota4 = float(input("digite sua quarta nota: "))

    media = calcular_media([nota1,nota2,nota3,nota4])

    print(f"\nMédia: {media:.2f}")
    print(classificar_media(media))

executar_calculo()
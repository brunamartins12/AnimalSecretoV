print("hello world!")
animal_secreto = "Mamute"

dicas = ['grande', 'come mato', 'tem tromba', 'aparece no filme do Era do gelo']
tentativa = 0
palpite = ""
while palpite != animal_secreto:
    print(f"Dica nº{tentativa}: o animal {dicas[tentativa]}")
    palpite = input("Adivinhe o animal que estou pensando:")
    tentativa += 1
    if tentativa == 4:
        print("game over!")
        break
    elif palpite == animal_secreto:
        print("você acertou!!")
def cifra():
    texto = input("Digite uma palavra: ").lower()
    deslocamento = 3
    resultado = ""

    for letra in texto:
        if letra.isalpha():

            posicao = ord(letra) - ord('a')

            nova_posicao = (posicao + deslocamento) % 26  # CIFRAR (+3)

            nova_letra = chr(nova_posicao + ord('a'))

            resultado += nova_letra

        else:
            resultado += letra

    print("Texto cifrado:", resultado)
    original = ""

    for letra in resultado:
        if letra.isalpha():

            posicao = ord(letra) - ord('a')

            nova_posicao = (posicao - deslocamento) % 26 # DECIFRAR (-3)

            nova_letra = chr(nova_posicao + ord('a'))

            original += nova_letra

        else:
            original += letra

    print("Texto original:", original)
cifra()
def contarCaracteres(texto: str) -> int:
    return len(texto)

def contarVogais(palavra: str) -> int:
    qtd_vogais = 0
    for letra in palavra:
        if letra.lower() in 'aeiou':
            qtd_vogais += 1
    return qtd_vogais
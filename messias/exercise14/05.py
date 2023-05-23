def encontra_palavras(lista_palavras, letra):
    return [palavra for palavra in lista_palavras if palavra.startswith(letra)]

palavras = ["hamilton", "verstappen", "senna", "prost"]
letra = "a"
print(encontra_palavras(palavras, letra))

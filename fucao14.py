#palindromo -  palavra oi frase que se pode ler,
#indeferentemente, da esquerda para a direitaou vice-versa

def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
    
#texti[::-1] inverte o texto

texto = "socorram-me, subi no ônibus em Marrocos"
if verificar_palindromo(texto):
    print(texto, "é um palíndromo.")
else:
    print(texto, "não é um palindromo.")
    
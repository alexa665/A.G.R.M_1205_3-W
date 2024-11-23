print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas y comparamos con su inversa
    return palabra.lower() == palabra.lower()[::-1]

print(es_palindromo("alexa"))  
print(es_palindromo("palindromo"))   
print(es_palindromo("arroz"))  


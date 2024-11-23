print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
def sum_lista(lista):              #funcion para suma y lista 
    resultado = 0                  #bucle for
    for num in lista:
        resultado += num
    return resultado               #imprime resultado de lista 

def multip_lista(lista):           #funcion para mult y lista 
    resultado = 1
    for num in lista:              #bucle for
        resultado *= num
    return resultado               #imprime resultado de lista 

print(sum_lista([1, 2, 3, 4]))     #imprime la suma y mult de las listas para dar los resultados pedidos
print(multip_lista([1, 2, 3, 4]))  
print(" ")


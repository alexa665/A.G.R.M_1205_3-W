print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
def superposicion(lista1, lista2):
    for elem1 in lista1:            #bucle de listas
        for elem2 in lista2:
            if elem1 == elem2:      # Si encontramos un elemento común, retornamos True
                return True
    return False                    # Si no encontramos elementos comunes, retornamos False
print(superposicion([1, 2, 3], [3, 4, 5]))    #impresion de listas

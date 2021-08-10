def verifica(cadena,caracter):
    for i in range(len(cadena)):
        if(cadena[i]==caracter):
            encontro=True
    return encontro

caracter=input("ingrese caracter: ")
cadena=input("ingrese cadena: ")

resultado=verifica(cadena,caracter)
print(resultado)

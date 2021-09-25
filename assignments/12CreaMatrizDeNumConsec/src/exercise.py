def main():
    #escribe tu código abajo de esta línea

    #Cantidad de renglones
    r = int(input())
    c = int(input())

    if r >= 2 and c >=2:
        #Matriz vacía
        matriz = []
        #Crear la matriz 
        num = 1
        for x in range(r):
            #Renglon vacío
            renglon = []
            #Crear un renglon
            for x in range(c):
                renglon.append(num)
                num = num + 1
            matriz.append(renglon)
        #Imprime la matriz
        print(matriz)
    else:
        print("Error")




if __name__=='__main__':
    main()

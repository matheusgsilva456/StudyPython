def quadradocomLoop():


    numEnt = int(input("Entre com nro de elementos: "))

    if (numEnt == 0 or numEnt<=0):
        print("Valor Invalido, tente novamente! ")

    else:

        cont = 0
        while cont != numEnt:
            nro = int(input("Entre com o nroº"))
            quadrado = nro * nro
            print("o quadrado é: ", quadrado)
            cont+=1

quadradocomLoop()

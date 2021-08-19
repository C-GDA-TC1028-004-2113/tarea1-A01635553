def main():
    #escribe tu código abajo de esta línea
    mes=float(input("Dame el número de mensajes: "))
    megas=float(input("Dame el número de megas: "))
    minutos=float(input("Dame el número de minutos: "))
    mes=mes*0.80
    megas=megas*0.80
    minutos=minutos*0.80
    resultado=minutos+megas+mes
    print("El costo mensual es:",resultado)




if __name__ == '__main__':
    main()

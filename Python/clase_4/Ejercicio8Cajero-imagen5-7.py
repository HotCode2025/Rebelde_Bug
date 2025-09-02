#Ejercicio 8: Menú interactivo – Cajero automático
# Hacer un programa que simule un cajero automático con un saldo inicial de 1000 $
# y tendrá el siguiente menú de opciones:
#               1- Ingresar dinero en la cuenta
#               2- Retirar dinero de la cuenta
#               3- Mostrar dinero disponible
#               4- Salir

saldo = 1000  # variable saldo inicial con 100 (saldo inicial)

while True:# Se ejecuta infinitamente hasta que se oprima la opción 4 donde está el break
    print("\n               ------- Cajero Automático -------")
    print("\n               ------------- MENÚ --------------")
    print("                 1. Ingresar dinero en la cuenta")
    print("                 2. Retirar dinero de la cuenta")
    print("                 3. Mostrar dinero disponible")
    print("                 4. Salir")

    opcion = input("\n                 Elige una opción (1-4): ")# la variable opción almacena el valor ingresado

    if opcion == "1":# Condicional si el usuario ingresó la opción 1, quiere ingresar dinero
        ingreso = float(input("Ingrese la cantidad de dinero a depositar: "))# se almacena en la variable ingreso el dinero a ingresar
        saldo += ingreso# le suma el contenido de la variable ingreso al saldo existente
        print(f"Has ingresado ${ingreso}, tu saldo actual es: ${saldo}")# Muestra mje del valor ingresado y el saldo actualizado
    elif opcion == "2": # opción 2, desea retirar dinero
        retiro = float(input("Ingrese la cantidad de dinero a retirar: "))# almacena el valor a retirar en la varible retiro
        if retiro > saldo:# Si el valor ingresado en la variable retiro es mayor al saldo existente
            print("Fondos insuficientes")# muestra mje fondos insuficientes
        else:
            saldo -= retiro # si el saldo alcanza, se le resta el retiro a la variable saldo
            print(f"Has retirado ${retiro}, tu saldo actual es: ${saldo}")# muestra mensaje con saldo actualizado

    elif opcion == "3":# opción 3, mostrar dinero disponible
        print(f"Tu saldo disponible es: ${saldo}")# muestra mje por pantalla del valor almacenado en saldo

    elif opcion == "4":# opción 4, salir
        print("Muchas Gracias por usar el cajero, que tengas un líndo día!")# mje de despedida
        break# con break se sale del menú

    else:
        print("Opción no válida, debes ingresar números del 1 a 4")#si la opción no es 1-2-3 ó 4, muestra mje de error
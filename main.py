import calculator as cal

opcion = 'x'
while opcion != '0':
    print('\n\t1- Suma \n\t2- Resta \n\t3- Multiplicacion \n\t4- Divicion \n\t0- Salir' )
    opcion = input('Seleccione una operacion: ')
    if opcion == '1':
        cal.suma(input('ingrese numero 1: '), input('Ingrese numero 2: '))
        
    elif opcion == '2':
        cal.resta(input('ingrese numero 1: '), input('Ingrese numero 2: '))
        
    elif opcion == '3':
        cal.multiplicacion(input('ingrese numero 1: '), input('Ingrese numero 2: '))
        
    elif opcion == '4':
        cal.divicion(input('ingrese numero 1: '), input('Ingrese numero 2: '))
        
    elif opcion == '0':
        print('Saliendo...')
        exit()
    else:
        print('La opcion ingresada no es valida, porfavor vuelva a intentarlo')

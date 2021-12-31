
def validacion(numero1, numero2):
    try:
        numero1 = int(numero1)
    except:
        numero1 = 'NaN'

    if (numero1 == 'NaN'):
        print('El  dato ingresado es incorrecto, intente un numero')
        import main


    try:
        numero2 = int(numero2)
    except:
        numero2 = 'NaN'

    if (numero2 == 'NaN'):
        print('El dato ingresado es incorrecto, intente un numero')
        import main


def suma(numero1, numero2):
    validacion(numero1, numero2)
    print('resultado = ', int(numero1)+int(numero2))
    import main

def resta(numero1, numero2):
    validacion(numero1, numero2)
    print('resultado =', int(numero1)-int(numero2))
    import main

def multiplicacion(numero1, numero2):
    validacion(numero1, numero2)
    print('resultado =', int(numero1)*int(numero2))
    import main
def divicion(numero1, numero2):
    validacion(numero1, numero2)
    if (numero2 == '0' or numero2 == 0):
        print('No puedes dividir entre "0", No intentes romper el universo como lo conocemos')
        import main

    print('resultado =', float(numero1)/float(numero2))
    import main

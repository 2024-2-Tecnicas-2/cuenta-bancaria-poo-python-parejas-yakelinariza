
import cuenta_bancaria

if __name__ == '__main__':
    # TODO: Adiciona aquí el código que deseas para la Cuenta Bancaria.

    cuenta = cuenta_bancaria.CuentaBancaria("Yakelin","123", 1000)

    print("Titular:", cuenta.get_titular())
    print("Numero de cuenta:", cuenta.get__numero_cuenta())
    print("Saldo inicial:", cuenta.get_saldo())

    ingresar = float(input("Ingresar la cantidad deseada: ")) 
    cuenta.ingresar(ingresar)
    print(f"Saldo despues de ingresar {ingresar} es {cuenta.get_saldo()}")

    retirar= float(input("Ingresar la cantidad que deseas retirar: ")) 
    cuenta.retirar(retirar)
    print(f"Saldo despues de retirar {retirar} es {cuenta.get_saldo()}")

    retirarD= float(input("Ingresar la cantidad que deseas retirar: ")) 
    cuenta.retirar(retirarD)
    print(f"Intento de retirar {retirarD} (no debería cambiar el saldo): {cuenta.get_saldo()}")

    print("Saldo con interés aplicado:", cuenta.calcularInteres())

    interes = float(input("Ingrese el nuevo tipo de interés: "))
    if 0 <= interes <= 10:
        cuenta.set_tipo_interes(interes)
        print(f"Nuevo saldo con interés aplicado ({interes}%): {cuenta.calcularInteres()}")
    else:
        print("No se puede establecer un interés negativo ni superior al 10%")



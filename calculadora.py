# calculadora.py
import sys

def multiplicar(num1, num2):
    """Multiplica dos números y devuelve el resultado."""
    return num1 * num2

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            numero1 = float(sys.argv[1])
            numero2 = float(sys.argv[2])
            resultado = multiplicar(numero1, numero2)
            print(f"El resultado de {numero1} * {numero2} es: {resultado}")
        except ValueError:
            print("Error: Por favor, introduce dos números válidos.")
    else:
        print("Uso: python calculadora.py <numero1> <numero2>")

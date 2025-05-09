# RA5.1-Jenkins
Ejercicios de psegarrac, jenkins.
# Proyecto de Calculadora en Python con Integración Continua

¡Bienvenidos a nuestro proyecto de calculadora en Python! En este repositorio, encontraréis un programa simple que multiplica dos números proporcionados como argumentos desde la línea de comandos, junto con un conjunto de pruebas unitarias para asegurar su correcto funcionamiento. Además, hemos configurado una pipeline de Integración Continua (CI) con Jenkins para automatizar la ejecución de estas pruebas con cada cambio en nuestro código.

## Tarea 1: Programa de Multiplicación en Python y Pruebas Unitarias

Nuestro primer objetivo fue desarrollar un programa en Python capaz de multiplicar dos números que le pasamos como argumentos al ejecutarlo desde la terminal. Para garantizar la calidad y fiabilidad de nuestro programa, también creamos pruebas unitarias exhaustivas.

### Pasos Realizados:

1.  **Creamos el archivo `calculadora.py`:** Este archivo contiene la lógica principal de nuestro programa. Definimos una función llamada `multiplicar` que toma dos números y devuelve su producto. También incluimos la lógica para obtener los argumentos de la línea de comandos y manejar posibles errores.

    ```python
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
    ```
![calculadora](/assets/calculadora.png)
2.  **Desarrollamos el archivo `test_calculadora.py`:** En este archivo, implementamos pruebas unitarias para la función `multiplicar` utilizando el módulo `unittest` de Python. Creamos varios casos de prueba para cubrir diferentes escenarios, incluyendo la multiplicación de números positivos, negativos, cero y decimales.

    ```python
    # test_calculadora.py
    import unittest
    from calculadora import multiplicar

    class TestCalculadora(unittest.TestCase):

        def test_multiplicar_positivos(self):
            self.assertEqual(multiplicar(2, 3), 6)

        def test_multiplicar_negativos(self):
            self.assertEqual(multiplicar(-2, 3), -6)
            self.assertEqual(multiplicar(-2, -3), 6)

        def test_multiplicar_cero(self):
            self.assertEqual(multiplicar(5, 0), 0)
            self.assertEqual(multiplicar(0, -3), 0)

        def test_multiplicar_decimales(self):
            self.assertEqual(multiplicar(2.5, 2), 5.0)
            self.assertEqual(multiplicar(1.5, 0.5), 0.75)

        def test_multiplicar_mixtos(self):
            self.assertEqual(multiplicar(-1.5, 4), -6.0)

    if __name__ == '__main__':
        unittest.main()
    ```

3.  **Ejecutamos el programa y las pruebas:** Verificamos que nuestro programa funciona correctamente ejecutándolo desde la línea de comandos con diferentes entradas. También nos aseguramos de que todas nuestras pruebas unitarias pasaran al ejecutarlas con el módulo `unittest`.

4.  **Subimos nuestro código a GitHub:** Creamos un nuevo repositorio en GitHub y subimos los archivos `calculadora.py` y `test_calculadora.py`.

## Tarea 2: Pipeline de Integración Continua con Jenkins

Nuestro siguiente paso fue configurar una pipeline de Integración Continua (CI) en Jenkins para nuestro proyecto. Esto nos permite automatizar la ejecución de nuestras pruebas unitarias cada vez que realizamos un cambio en el código.

### Pasos Realizados:

1.  **Creamos el archivo `Jenkinsfile`:** En la raíz de nuestro repositorio, definimos nuestra pipeline de CI en un archivo llamado `Jenkinsfile`. Esta pipeline contiene una etapa para ejecutar nuestras pruebas unitarias de Python.

    ```groovy
    pipeline {
        agent any

        stages {
            stage('Ejecutar pruebas unitarias') {
                steps {
                    sh 'python -m unittest test_calculadora.py'
                }
            }
        }

        post {
            always {
                echo 'Pipeline finalizada'
            }
            success {
                echo '¡Las pruebas unitarias pasaron!'
            }
            failure {
                echo '¡Las pruebas unitarias fallaron!'
            }
        }
    }
    ```

2.  **Subimos el `Jenkinsfile` a nuestro repositorio:** Agregamos y commiteamos el archivo `Jenkinsfile` a nuestro repositorio en GitHub.

3.  **Configuramos la pipeline en Jenkins:** Creamos una nueva pipeline en Jenkins y la configuramos para obtener la definición de la pipeline desde nuestro repositorio Git, especificando la URL del repositorio y la ruta al `Jenkinsfile`.

4.  **Configuramos el disparador automático:** Activamos el "GitHub hook trigger for GITScm polling" en la configuración de nuestra pipeline en Jenkins. Esto permite que Jenkins se active automáticamente al recibir una notificación de GitHub sobre nuevos commits en nuestro repositorio. (Es importante asegurarse de que el webhook esté configurado correctamente en nuestro repositorio de GitHub apuntando a nuestra instancia de Jenkins).

5.  **Observamos la ejecución de la pipeline:** Realizamos commits en nuestro repositorio y observamos cómo Jenkins automáticamente ejecuta la pipeline, mostrando el estado de cada etapa (en nuestro caso, la ejecución de las pruebas unitarias).

6.  **Experimentamos con fallos en las pruebas:** Introdujimos errores intencionadamente en nuestras pruebas unitarias para verificar que la pipeline en Jenkins detectara los fallos y nos alertara de ellos.

¡Con esto, hemos establecido un flujo de trabajo de integración continua básico para nuestro proyecto de calculadora en Python, asegurando que nuestras pruebas se ejecuten automáticamente con cada cambio en el código!

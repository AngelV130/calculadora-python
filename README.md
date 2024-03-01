**Proyecto Calculadora**

---

### Descripción del Proyecto:

Esat aplicacion esta echa para resolver problemas de
- Euler Mejorado
- Newton-Raphson
- Runge Kutta de Cuarto Orden

Proyecto en [GitHub](https://github.com/AngelV130/calculadora-python).

---

### Instalación:

Para comenzar a utilizar el Proyecto Calculadora, sigue estos pasos de instalación:

1. **Librerias Necesarias:**
```bash

# Installa con estos comandos:

pip install flask
pip install sympy
```
2. **Iniciar Proyecto:**
```bash

# Iniciar con:

python3 serve.py
```
La aplicacion se iniciaria en http://localhost:5000/.

En (http://localhost:5000/) Se encuatra la vista de la app.

## Rutas de Documentación

El proyecto incluye varias rutas de documentación que proporcionan información detallada sobre su funcionamiento y uso. A continuación se enumeran estas rutas:

- **GET /api:** Esta ruta proporciona acceso a la documentación general del proyecto, que incluye una descripción de las características.

- **GET /api/documentacion:** Esta ruta ofrece documentación específica sobre la API del proyecto. Aquí encontrarás detalles sobre los puntos finales disponibles, los parámetros esperados, los formatos de respuesta y ejemplos de solicitudes.


> ### Importante  
> Reglas.
> - Indicar con " * " las multiplicaciones, no se aceptan dos caracteres juntos como "xy".<br> 
> Ejemplo:<br>
> Funcion Incorrecta: 2 * x y<br>
> Funcion Correcta: 2 * x * y
> - Indicar con " ** " las potencias, no se aceptan otros caracteres para indicarla como "^".<br> 
> Ejemplo:<br>
> Funcion Incorrecta: 2 * ( x ^ 2 ) y<br>
> Funcion Correcta: 2 * ( x * * 2 ) * y
> - Indicar con " e**(operacin) " el calculo del euler, no se aceptan "e(operacion)".<br> 
> Ejemplo:<br>
> Funcion Incorrecta: 2 * e( x ^ 2 x ) y<br>
> Funcion Correcta: 2 * e**( ( x ^ 2 ) * x) * y
> - Indicar con " √(operacin) " el calculo de la raiz, no se aceptan otras formas para calcular raiz.<br> 
> Ejemplo:<br>
> Funcion Incorrecta: 2 * √xy<br>
> Funcion Correcta: 2 * √(x*y)
> <br>
> En el archivo ejemplos.txt estan algunos ejemplos de para probar los 3 metodos.


## Propietario del Proyecto

El propietario y mantenedor principal de este proyecto es.
[Angel Moises Vargas Ramirez](https://github.com/AngelV130).


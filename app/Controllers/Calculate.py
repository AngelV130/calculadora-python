from ast import dump
from flask import jsonify, request, Response
import math
import sympy
import re
import os
from app.Validators import Validate

def view():
    # Ruta al archivo HTML
    file_path = os.path.join(os.getcwd(), 'res', 'index.html')
    
    # Leer el contenido del archivo HTML
    with open(file_path, 'r') as file:
        html_content = file.read()
    
    # Crear una respuesta HTTP con el contenido del archivo HTML
    response = Response(html_content, status=200, content_type='text/html')
    
    return response

def index():
    return jsonify({
        'message': 'Api para Resolver Problemas De Euler Mejorado, Newton Raphson y Runge Kutta de Cuarto 4to Orden!',
        'rutas': {
            'euler-mejorado': '/api/euler-mejorado',
            'newton-raphson': '/api/newton-raphson',
            'runge-kutta': '/api/runge-kutta',
            'documentacion': '/api/documentacion'
        },
        'status': 200
        })

def documentacion():
    return jsonify({
        'message': 'Documentación de la API para Resolver Problemas De Euler Mejorado, Newton Raphson y Runge Kutta de Cuarto 4to Orden!',
        'rutas': {
            'euler-mejorado': {
                'metodo': 'POST',
                'ruta': '/api/euler-mejorado',
                'parametros': {
                    'n': 'Número de pasos',
                    'x': 'Punto inicial',
                    'y': 'Valor inicial',
                    'h': 'Tamaño del paso',
                    'f': 'Función f(x, y)'
                }
            },
            'newton-raphson': {
                'metodo': 'POST',
                'ruta': '/api/newton-raphson',
                'parametros': {
                    'valor_inicial': 'Valor inicial',
                    'funcion': 'Función f(x)',
                    'decimal': 'Cantidad de decimales'
                }
            },
            'runge-kutta': {
                'metodo': 'POST',
                'ruta': '/api/runge-kutta',
                'parametros': {
                    'n': 'Número de pasos',
                    'x': 'Punto inicial',
                    'y': 'Valor inicial',
                    'h': 'Tamaño del paso',
                    'f': 'Función f(x, y)'
                }
            }
        },
        'status': 200
        })

def euler_mejorado():
    data = request.get_json()
    errors = Validate.validate(data,[
        {'name': 'n','type': float,},
        {'name': 'y','type': float,},
        {'name': 'x','type': float,},
        {'name': 'h','type': float,},
        {'name': 'f','type': str,}
    ])
    if errors:
        return jsonify({'message': 'No se encontró un valor inicial para la función.', 'errors': errors, 'status': 402}), 402
    if not es_funcion_valida(data['f']):
        return jsonify({'message': 'La función no es válida.', 'status': 402}), 402

    n = data['n']             # Número de pasos
    x = data['x']             # Punto inicial
    y = data['y']             # Valor inicial
    h = data['h']             # Tamaño del paso
    f = data['f']       # Función f(x, y)

    e  = ['0.0']                        # Lista para almacenar los errores
    yn = [f"{y:.5f}"]                   # Lista para almacenar las aproximaciones de y
    yr = [f"{calcular_euler(y):.5f}"]   # Lista para almacenar los valores reales
    xn = [f"{x:.1f}"]                   # Lista para almacenar los valores de x
    yp = ['0.0']

    while x <= n:
        func_res = float(eval(f.replace('x', str(x)).replace('y', str(y))))
        y_pred = y + h * func_res  # Predicción utilizando el método de Euler
        y_corr = y + h / 2 * (func_res + float(eval(f.replace('x', str(x+h)).replace('y', str(y_pred)))))  # Corrección
        y = round(y_corr,8)  # Actualización de y
        x += h # Actualización de x

        euler = round(calcular_euler(x),8) # Cálculo del valor real de y
        yn.append(f"{y:.5f}") # Almacenamiento de la aproximación de y
        e.append(f"{abs(euler - y):.5f}") # Almacenamiento del error
        yr.append(f"{euler:.5f}") # Almacenamiento del valor real de y
        xn.append(f"{x:.1f}") # Almacenamiento del valor de x
        yp.append(f"{y_pred:.8f}") # Almacenamiento de la predicción de y
    return jsonify({'yn': yn, 'yr': yr, 'e': e, 'x': xn, 'yp': yp})

def newton_raphson():

    data = request.json
    errors = Validate.validate(data,[
        {
            'name': 'valor_inicial',
            'type': float,
        },
        {
            'name': 'funcion',
            'type': str,
        }
    ])
    if errors:
        return jsonify({'message': 'No se encontró un valor inicial para la función.', 'errors': errors, 'status': 402}), 402
    if not es_funcion_valida(data['funcion']):
        return jsonify({'message': 'La función no es válida.', 'status': 402}), 402

    f = cambiar_lado_ecuacion(data["funcion"]) # Función f(x, y)
    x = data['valor_inicial']  #valor inicial
    decimal =  data['decimal'] if 'decimal' in data and isinstance(data['decimal'], int) else 5 # Cantidad de decimales
    x1 = [x] # Lista para almacenar las aproximaciones de x
    
    while x1[-1] != x1[x1.__len__() - 2] or x1.__len__() < 5:
        x1.append(function_recursive(f, x1[-1], decimal))
    return jsonify({'x': x1})

def runge_kutta_4th_order():
    data = request.get_json()
    errors = Validate.validate(data,[
        {'name': 'x','type': float,},
        {'name': 'y','type': float,},
        {'name': 'h','type': float,},
        {'name': 'n','type': float,},
        {'name': 'f','type': str,}
    ])
    if errors:
        return jsonify({'message': 'No se encontró un valor inicial para la función.', 'errors': errors, 'status': 402}), 402
    if not es_funcion_valida(data['f'].replace('√', '*')):
        return jsonify({'message': 'La función no es válida.', 'status': 402}), 402

    x_values = [data['x']] # Valores de la variable independiente
    y_values = [data['y']] # Valores de la variable dependiente
    h = data['h'] # Tamaño del paso
    f = data['f'] # Función que describe la EDO
    limit = data['n'] # Número de pasos

    k_s = {'k1': [], 'k2': [], 'k3': [], 'k4': []} # Valores de las constantes k1, k2, k3 y k4
    

    while x_values[-1] <= limit:
        k1 = float(
            eval(
                f.replace('x', str(x_values[-1])).
                replace('y', str(y_values[-1])).
                replace('√', 'sympy.sqrt').
                replace('e**','math.exp')
                )
            )
        k2 = float(
            eval(
                f.replace('x', str(float(x_values[-1] + (h/2)))).
                replace('y', str(float(y_values[-1] + (h/2*k1)))).
                replace('√', 'sympy.sqrt').
                replace('e**','math.exp')
            )
            )
        k3 = float(
            eval(
                f.replace('x', str(float(x_values[-1] + (h/2)))).
                replace('y', str(float(y_values[-1] + (h/2*k2)))).
                replace('√', 'sympy.sqrt').
                replace('e**','math.exp')
                )
            )
        k4 = float(
            eval(
                f.replace('x', str(float(x_values[-1] + h))).
                replace('y', str(float(y_values[-1] + (h*k3)))).
                replace('√', 'sympy.sqrt').
                replace('e**','math.exp')
            )   
            )
        
        y_next = y_values[-1] + (1/6) * (k1 + 2*k2 + 2*k3 + k4) * h
        y_values.append(round(y_next, 5))
        k_s['k1'].append(round(k1, 5))
        k_s['k2'].append(round(k2, 5))
        k_s['k3'].append(round(k3, 5))
        k_s['k4'].append(round(k4, 5))
        x_values.append(round(x_values[-1] + h,5))
    k1 = float(
        eval(
            f.replace('x', str(x_values[-1])).
            replace('y', str(y_values[-1])).
            replace('√', 'sympy.sqrt').
            replace('e**','math.exp')
            )
        )
    k2 = float(
        eval(
            f.replace('x', str(float(x_values[-1] + (h/2)))).
            replace('y', str(float(y_values[-1] + (h/2*k1)))).
            replace('√', 'sympy.sqrt').
            replace('e**','math.exp')
        )
        )
    k3 = float(
        eval(
            f.replace('x', str(float(x_values[-1] + (h/2)))).
            replace('y', str(float(y_values[-1] + (h/2*k2)))).
            replace('√', 'sympy.sqrt').
            replace('e**','math.exp')
            )
        )
    k4 = float(
        eval(
            f.replace('x', str(float(x_values[-1] + h))).
            replace('y', str(float(y_values[-1] + (h*k3)))).
            replace('√', 'sympy.sqrt').
            replace('e**','math.exp')
        )   
        )
    
    k_s['k1'].append(round(k1, 5))
    k_s['k2'].append(round(k2, 5))
    k_s['k3'].append(round(k3, 5))
    k_s['k4'].append(round(k4, 5))
    
    return jsonify({'x': x_values, 'y': y_values, 'k_s': k_s})


# Funciones auxiliares privadas
def calcular_euler(a):
    resultado = math.exp(( 0.2 * ( a ** 2 ) ) - 0.2)
    return resultado

def function_recursive(func:str, x, decimal=5):
    # Define metodo newton raphson
    e = math.e
    # Define la derivada de la función
    derivada = str(sympy.diff(sympy.sympify(func.replace("e**x", str(sympy.exp(sympy.symbols('x'))))), sympy.symbols('x'))).replace('exp(x)', 'e**x')

    # Define division de la función entre la derivada
    division = "(" + func + ")" + "/" + "(" + derivada + ")"

    # Evalua la division
    result = round(float(eval(division.replace('x', str(x)))), decimal)

    # Evalua la función
    return round(x - result, decimal)

def cambiar_lado_ecuacion(ecuacion):
    # Separa la ecuación en sus partes
    partes = ecuacion.split('=')
    lado_izquierdo = partes[0].strip()  # Lado izquierdo de la ecuación
    lado_derecho = partes[1].strip()  # Lado derecho de la ecuación

    # Si el lado izquierdo de la ecuación es 0, la ecuación no cambia
    if lado_izquierdo == "0":
        return ecuacion
    
    # Cambia los signos de los términos en el lado derecho de la ecuación
    nuevo_lado_derecho = ""
    for termino in lado_derecho.split():
        if termino.startswith('-'):  # Si el término es negativo, convierte el signo a positivo
            nuevo_lado_derecho += " + " + termino[1:]
        elif termino.startswith('+'):  # Si el término es positivo, convierte el signo a negativo
            nuevo_lado_derecho += " - " + termino[1:]
        else:  # Si el término no tiene signo, se convierte en negativo
            nuevo_lado_derecho += "" + termino
    
    # Elimina el primer signo si es positivo
    if nuevo_lado_derecho.startswith('+'):
        nuevo_lado_derecho = nuevo_lado_derecho[2:]
    
    # Construye la nueva ecuación
    nueva_ecuacion = lado_izquierdo + " - " + nuevo_lado_derecho
    
    return nueva_ecuacion

def verify_euler(func: str):
    if 'e' in func:
        return re.split('(e)', func)
    return func

def es_funcion_valida(cadena):
    try:
        # Intenta analizar la cadena como una expresión matemática
        func = cadena.replace("(",'').replace(")",'').replace('=','-').replace("e**x", str(sympy.exp(sympy.symbols('x'))))
        x = sympy.symbols('x')
        print(func)
        sympy.sympify(func)
        # Verifica si la cadena contiene la variable x
        if 'x' not in sympy.latex(sympy.sympify(func)):
            return False
        return True
    except (sympy.SympifyError, TypeError):
        return False
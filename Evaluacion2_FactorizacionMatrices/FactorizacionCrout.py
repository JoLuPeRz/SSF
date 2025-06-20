# Programa de factorización de Crout para sistemas lineales tridiagonales.

def dimension_n_mat_coef():
    """
    Pide al usuario que indique la dimensión n de la matriz cuadrada de 
    coeficientes A, de tamaño n x n.

    Evalua si la entrada proporcionada es un número entero positivo.
    En caso de que la entrada no sea correcta, solicita que se ingrese un número válido.

    Devuelve la dimensión "n". 
    """
    # Se inicia la variable n en -1, para garantizar que el while se pueda ejecutar al menos una vez.
    n_mat_coef = -1

    # Se utiliza un while para que se solicite la dimensión, hasta que se proporcione un número entero positivo.
    while n_mat_coef <= 0:
        n_dim = input("Por favor introduce, como número entero positivo, la dimensión n de la matriz cuadrada de coeficientes A: ")
        if n_dim.isdigit(): # Verifica si la entrada es un dígito. 
            n_mat_coef = int(n_dim)
            if n_mat_coef <= 0:
                print("La dimensión debe corresponder a un número mayor que cero.")
                print("Por favor, ingresa un n > 0.")
        else:
            print("Se ha proporcionado una dimensión inválida.")
            print("Por favor, ingresa un número entero positivo.")
    return n_mat_coef

def tridiagonalidad(matriz, dimension):
    """
    Parámetros:
    - matriz: Matriz a evaluar su tridiagonalidad.
    - dimension: Dimensión de la matriz a evaluar su tridiagonalidad.

    Se verifica si una matriz es tridiagonal.

    Devuelve True si la matriz proporcionada es tridiagonal.
    
    En caso de no serlo, devuelve False y menciona el elemento de la matriz
    que genera error.
    """
    for i in range(dimension):
        for j in range(dimension):
            if abs(i - j) > 1 and matriz[i][j] != 0: # Evalua si alguna entrada a_{ij} es distitinta de cero, si se cumple que |i-j|>1
                print(f"ERROR: La entrada [{i+1}][{j+1}] de la matriz {matriz} = {matriz[i][j]} debería ser 0.")
                print("\nPor tanto, la matriz no es tridiagonal.")
                return False
    return True

def ingresar_matA_aumentada(dim_mat_coef):
    """
    Parámetros:
    - dim_mat_coef: Dimension de la matriz de coeficientes A, indicado por un número entero positivo.

    Pide que se ingrese la matriz aumentada A, ya sea por medio de sus entradas (una por una),
    o por medio de su representación en forma de lista anidada.

    La matriz aumetada A es una matriz de tamaño n x (n+1), que contiene las entradas de la matriz de 
    coeficientes A y las entradas del vector columna de términos independientes (a_{1,n+1}, ..., a_{n,n+1}).

    Devuelve la matriz aumentada A proporcionada.
    """

    print("Ahora, es necesario que se indique la matriz aumentada A\n")
    print("Para ello, se puede hacer de dos formas: ingresar una por una sus entradas, o bien, \ningresar de forma completa la matriz A (como lista anidada).\n")
    print("Así, las opciones disponibles son:\n")
    print("Opción 1. Ingresar manualmente cada elemento a_ij y a_{i,n+1} de la matriz aumentada A.")
    print("Opción 2. Introducir la matriz aumentada A completa, como lista anidada.\n")

    # Se guarda la opción elegida en la variable opcion_ingreso_matA_aumentada
    opcion_ingreso_matA_aumentada = input("Selecciona la opción preferida (indica únicamente ya sea el número 1 o 2): ")

    A_aumentada = [] # Se inicializa la matriz aumentada A como una lista vacía, para después poder agregarle los elementos.

    # Dependiendo de la elección, se proporcionará la matriz aumentada $A$,
    # ya sea por medio de sus entradas o en su forma matricial por medio de listas anidadas:

    if opcion_ingreso_matA_aumentada == "1": # Selección de ingresar los elementos de la matriz aumentada A uno a uno.
        print("\nPor favor, ingresa los elementos a_ij y a_{i,n+1} \nde la matriz aumentada A, uno por uno:")
        for i in range(dim_mat_coef):
            fila_A = []
            for j in range(dim_mat_coef + 1):
                if j < dim_mat_coef:
                    entrada_matriz = float(input(f"a_{i+1}{j+1} = ")) # Se utiliza float, en caso de que la matriz contenga números decimales.
                else:
                    entrada_matriz = float(input(f"a_({i+1},n+1) (término independiente) ="))
                fila_A.append(entrada_matriz)
            A_aumentada.append(fila_A)
    elif opcion_ingreso_matA_aumentada == "2": # Selección de ingresar la matriz aumentada A completa como lista anidada.
        print("\nPor favor, ingresa la matriz aumentada A como una lista anidada: ")
        print("\nComo recordatorio y a manera de ejemplo, siendo los coeficientes de la matriz A los siguientes: \n")
        print("[[1, 2, 3], [4, 5, 6], [7, 8, 9]] \n")
        print("Y el vector columna de términos independientes: \n")
        print("[10, 11, 12] \n")
        print("La matriz aumentada A se introduciría como: \n")
        print("[[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]] \n")
        A_aumentada = eval(input("Proporciona la Matriz aumentada A: "))
        for i in range(dim_mat_coef):
            if len(A_aumentada[i]) != dim_mat_coef + 1: # Se verifica que se haya introducido la matriz aumentada A con n+1 columnas, y no la matriz de coeficientes A.
                print("La matriz aumentada A debe tener n+1 columnas.")
                print("Por favor, introduce tambíen las entradas de los términos independientes.")
                exit()
    else:
        print("No se ingresaron los datos correctamte (o se ingresó una entrada no válida).")
        print("\nPor favor, revisar errores. Se saldrá del programa.")
        exit()
    
    # Se extrae únicamente la matriz de coeficientes A.
    mat_coef_A = []
    for i in range(dim_mat_coef):
        fila_mat_coef_A = []
        for j in range(dim_mat_coef):
            fila_mat_coef_A.append(A_aumentada[i][j])
        mat_coef_A.append(fila_mat_coef_A)

    # Se verifica que la matriz de coeficientes A sea tridiagonal.
    tridiagonal_verdadero =  tridiagonalidad(mat_coef_A, dim_mat_coef)
    if tridiagonal_verdadero == False:
        print("La matriz de coeficientes A dada, no es tridiagonal.")
        print("Por favor, revisar la tridiagonaidad.")
        print("Se saldrá del programa.")
        exit()

    return A_aumentada

def algoritmo_Crout(dimension, matriz_aumentada):
    """
    Parámetros:
    - dimension: Dimensión de la matriz cuadrada de coeficientes, de tamaño n x n.
    - matriz_aumentada: Matriz aumentada de tamaño n x (n+1), la cual se obtiene a 
    partir de la función ingresar_matA_aumentada(dim_mat_coef). Contiene las entradas a_{ij} 
    de la matriz de coeficientes A, y las entradas a_{i,n+1} del vector columna de 
    términos independientes del sistema lineal de ecuaciones n x n.

    Realiza el algoritmo correspondiente de la factorizacion de Crout para sistemas lineales tridiagonales.

    Factoriza la matriz aumentada dada en las matrices L y U, donde U tiene unos en su diagonal principal.

    Devuelve la solución x_1, ..., x_n del sistema lineal de ecuaciones n x n.
    """
    L = [[0.0] * dimension for _ in range(dimension)]  # Inicializa L como una matriz n x n con ceros
    U = [[0.0] * dimension for _ in range(dimension)]  # Inicializa U como una matriz n x n con ceros
    z = [0.0] * dimension  # Inicializa el vector z (de tamaño n) con ceros
    x = [0.0] * dimension  # Inicializa el vector x (de tamaño n) con ceros

    # Fijar elementos de la diagonal principal de U a 1
    for i in range(dimension):
        U[i][i]= 1.0
    

    # CONFIGURACIÓN Y SOLUCIÓN DE Lz = b

    # Paso 1:
    L[0][0] = matriz_aumentada[0][0]  # Se establece l_{11} = a_{11}
    U[0][1] = matriz_aumentada[0][1] / L[0][0]  # Se establece u_{12} = a_{12} / l_{11}
    z[0] = matriz_aumentada[0][dimension] / L[0][0]  # Se establece z_1 = a_{1,n+1} / l_{11}

    # Paso 2:
    for i in range(1, dimension -1):
        L[i][i-1] = matriz_aumentada[i][i-1]  # Se establece l_{i,i-1} = a_{i,i-1}
        L[i][i] = matriz_aumentada[i][i] - L[i][i-1] * U[i-1][i] # Se establece l_{ii} = a_{ii} - l_{i,i-1}  u_{i-1,i}
        U[i][i+1] = matriz_aumentada[i][i+1] / L[i][i] # Se establece u_{i,i+1} = a_{i,i+1} / l_{ii}
        z[i] = (matriz_aumentada[i][dimension] - L[i][i-1] * z[i-1]) / L[i][i] # Se establece z_i = (a_{i,n+1} - l_{i,i-1} z_{i-1}) / l_{ii}

    # Paso 3:
    L[dimension-1][dimension-2] = matriz_aumentada[dimension-1][dimension-2] # Se determina l_{n,n-1} = a_{n,n-1}
    L[dimension-1][dimension-1] = matriz_aumentada[dimension-1][dimension-1] - L[dimension-1][dimension-2] * U[dimension-2][dimension-1] # Se determina l_{nn} = a_{nn} - l_{n,n-1} u_{n-1,n}
    z[dimension-1] = (matriz_aumentada[dimension-1][dimension] - L[dimension-1][dimension-2] * z[dimension-2]) / L[dimension-1][dimension-1] # Se determina z_n = (a_{n,n+1} - l_{n,n-1} z_{n-1}) / l_{nn}

    # SOLUCIÓN DE U x= z

    # Paso 4:
    x[dimension-1] = z[dimension-1]  # Se establece x_n = z_n

    # Paso 5:
    for i in range(dimension - 2, -1, -1):
        x[i] = z[i] - U[i][i+1] * x[i+1]  # Se determina x_i = z_i - u_{i,i+1} x_{i+1}
    

    return x, L, U

# Se inicia solicitando la dimensión "n" de la matriz cuadrada de coeficientes A (que se busca factorizar), de tamaño n x n.
n_Crout = dimension_n_mat_coef()

# Se solicita que se ingrese la matriz aumentada A, de tamaño n x (n+1), la cual contiene 
# las entradas a_{ij} de la matriz de coeficientes A, y las entradas a_{i,n+1} del vector columna de términos independientes.
A_Crout = ingresar_matA_aumentada(n_Crout)

# Se realizan los pasos del algoritmo de factorización de Crout, para sistemas lineales tridiagonales.
solucion_x, L, U = algoritmo_Crout(n_Crout, A_Crout)

# Se muestra la solución x_1, ..., x_n del sistema lineal de ecuaciones n x n.
print("\nLa solución del sistema lineal n x n, está dado por:")
for i in range(len(solucion_x)):
    print(f"x_{i+1} = {solucion_x[i]:.2f}") # Se muestran las soluciones con únicamente dos decimales.

# Matrices L y U resultantes de la factorización

print("\nLa matriz L, resultante de la factorización de la matriz de coeficientes A, es:")
for filas_L in L:
    print(filas_L)

print("\nLa matriz U, resultante de la factorización de la matriz de coeficientes A, es:")
for filas_U in U:
    print(filas_U)

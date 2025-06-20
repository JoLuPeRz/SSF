# Programa para realizar la factorización LU de una matriz cuadrada A,
# de dimensión n x n, que es ingresada por el usuario.

def dimension_matA_FactLU():
    """
    Pide al usuario que indique la dimensión de la matriz A.

    Evalua si la entrada proporcionada es un número entero positivo.
    En caso de que la entrada no sea correcta, solicita que se ingrese un número válido.

    Devuelve la dimensión "n" de la matriz A. 
    """
    # Se inicia la variable n en -1, para garantizar que el while se pueda ejecutar al menos una vez.
    n = -1

    # Se utiliza un while para que se solicite la dimensión, hasta que se proporcione un número entero positivo.
    while n <= 0:
        n_dim = input("Por favor introduce, como número entero positivo, la dimensión de la matriz cuadrada A")
        if n_dim.isdigit(): # Verifica si la entrada es un dígito. 
            n = int(n_dim)
            if n <= 0:
                print("La dimensión debe corresponder a un número mayor que cero.")
                print("Por favor, ingresa un n > 0.")
        else:
            print("Se ha proporcionado una dimensión inválida.")
            print("Por favor, ingresa un número entero positivo.")
    return n

def ingresar_matA(dimension):
    """
    Parámetro:
    - dimension: Dimensión de la matriz cuadrada A, en número entero positivo.

    Pide que se ingrese la matriz A, ya sea por medio de sus entradas (una por una), o por medio de su representación en forma de lista anidada.

    Verifica que la matriz A no contenga entradas iguales a cero en la diagonal principal.

    Devuelve la matriz A proporcionada.
    """
    print("Ahora, es necesario que se indique la matriz A\n")
    print("Para ello, se puede hacer de dos formas: ingresar una por una sus entradas, o bien, \ningresar de forma completa la matriz A (como lista anidada).\n")
    print("Así, las opciones disponibles son:\n")
    print("1. Ingresar manualmente cada elemento a_ij de la matriz A.")
    print("2. Introducir la matriz A completa, como lista anidada.\n")

    # Se guada la opción elegida en la variable opcion_ingreso_matA
    opcion_ingreso_matA = input("Selecciona 1 o 2 (indica únicamente ya sea el número 1 o 2): ")

    A = [] # Se inicializa la matriz A como una lista vacía, para después poder agregarle los elementos.

    # Dependiendo de la elección, se proporcionará la matriz $A$ ya sea por medio de sus entradas o en su forma matricial por medio de listas anidadas:

    if opcion_ingreso_matA == "1": # Selección de ingresar los elementos de la matriz A uno a uno.
        print("\nPor favor, ingresa los elementos a_ij \nde la matriz A, uno por uno:")
        for i in range(dimension):
            fila_A = []
            for j in range(dimension):
                entrada_matriz = float(input(f"a_{i+1}{j+1} = ")) # Se utiliza float, en caso de que la matriz contenga números decimales.
                fila_A.append(entrada_matriz)
            A.append(fila_A)
    elif opcion_ingreso_matA == "2": # Selección de ingresar 
        print("\nPor favor, ingresa la matriz A como una lista anidada: ")
        print("\nComo recordatorio, la matriz identidad para dimensión n=3, se introduciría como: \n")
        print("[[1, 0, 0], [0, 1, 0], [0, 0, 1]] \n")
        A = eval(input("Proporciona la Matriz A: "))
    else:
        print("No se ingresó correctamte la matriz (o una entrada válida). \nSe saldrá del programa.")
        exit()
    
    # Se verifica que la matriz A no contenga entradas iguales a cero en la diagonal principal.
    for i in range(dimension):
        if A[i][i] == 0:
            print(f"ERROR: la entrada a_{i+1}{i+1} de la matriz A, es cero. \n La matriz podría no ser factorizable.")
            print("Para evitar errores, se saldrá del programa.")
            exit()

    return A

def eleccion_diagonal_unos():
    """
    Se pide al usuario que seleccione cuál matriz (L o U) tenga su diagnonal principal con unos.

    Devuelve dos valores booleanos: diagonal_L y diagonal_U, los cuales indican la elección de la matriz que tendrá unos en su diagonal principal.

    Es decir, si diagonal_L es True, la matriz L tendrá unos en su diagonal principal. 
    Si diagonal_U es True, la matriz U tendrá unos en su diagonal principal.

    """
    print("\nPor favor, selecciona qué matriz dentrá su diagnonal principal únicamente con unos:\n")
    print("Opción 1. En la matriz L (triangular inferior)")
    print("Opción 2. En la matriz U (triangular superior)\n")
    eleccion_diagonal = input("Por favor, indica únicamente el número de la opción preferida (1 o 2): ")

    if eleccion_diagonal == "1":
        diagonal_L = True
        diagonal_U = False
        print("\nSe ha seleccionado que la matriz L tenga en su diagonal principal, únicamente unos.")
    elif eleccion_diagonal == "2":
        diagonal_L = False
        diagonal_U = True
        print("\nSe ha seleccionado que la matriz U tenga en su diagonal principal, únicamente unos.")
    else:
        print("Opción inválida. Saliendo del programa.")
        exit()
    
    return diagonal_L, diagonal_U

def factorizacion_LU(A, n, diag_L, diag_U):
    """
    Parámetros:
    - A: Matriz cuadrada de dimensión n x n a factorizar.
    - n: Dimensión de la matriz A.
    - diag_L: Booleano (True o False) que indica si la matriz L fue la seleccionada para tener unos en su diagonal principal.
    - diag_U: Booleano (True o False) que indica si la matriz U fue la seleccionada para tener unos en su diagonal principal.
    
    Realiza el algoritmo correspondiente a la factorización LU, de la matriz A dada.

    Devuelve las matrices L y U resultantes de la factorización.
    """
    L = [[0.0] * n for _ in range(n)]  # Se inicializa la matriz L como una matriz n x n que contiene únicamente ceros
    U = [[0.0] * n for _ in range(n)]  # Se inicializa la matriz U como una matriz n x n que contiene únicamente ceros

    # PASOS DEL ALGORITMO 6.4

    # Paso 1:
    if diag_L: # En caso que se elija que la matriz L tenga unos en la diagonal principal
        L[0][0] = 1.0  # Se asigna 1 a la entrada l_{11}, representado por L[0][0]
        U[0][0] = A[0][0] # Ya que l_{11} = 1, entonces l_{11} u_{11} = a_{11} -> 1 * u_{11} = a_{11}
    elif diag_U:
        U[0][0] = 1.0  # Se asigna 1 a la entrada u_{11}, representado por U[0][0]
        L[0][0] = A[0][0]  # Ya que u_{11} = 1, entonces l_{11} u_{11} = a_{11} -> l_{11} * 1 = a_{11}

    if L[0][0] * U[0][0] == 0:
        print("ERROR: La entrada a_11 de la matriz A es cero.")
        print("\nPor tanto, no es posible realizar la factorización.")
        return None, None # Ya que la función devuelve las matrices L y U, se devuelve None para indicar que no se pudo realizar.

    # Paso 2:
    for j in range(1, n):
        if diag_L: # En caso que se haya seleccionado la matriz L como la que tenga unos en la diagonal principal
            U[0][j] = A[0][j] / L[0][0] # Se establece que u_{1j} = a_{1j} / l_{11}
            L[j][0] = A[j][0] / U[0][0] # Se establece que l_{j1} = a_{j1} / u_{11}
        elif diag_U: # En caso que se haya seleccionado la matriz U como la que tenga unos en la diagonal principal
            U[0][j] = A[0][j] / L[0][0] # Se establece que u_{1j} = a_{1j} / l_{11}
            L[j][0] = A[j][0] / U[0][0] # Se establece que l_{j1} = a_{j1} / u_{11}

    # Paso 3-5:
    for i in range(1, n-1):
        sum_k = 0.0 # Se inicializa la sumatoria en cero.
        for k in range(i):
            sum_k += L[i][k] * U[k][i] # Se calcula la sumatoria de l_{ik} u_{ki} para k desde 0 hasta i-1
            valor_aii = A[i][i] - sum_k  # Se actualiza la entrada a_{ii}, al restar la suma de los productos L[i][k] * U[k][i]
        
        if diag_L: # En caso que se haya seleccionado la matriz L como la que tenga unos en la diagonal principal
            L[i][i] = 1.0 # Se establece que l_{ii} = 1
            U[i][i] = valor_aii / L[i][i]  # Se despeja u_{ii}
        elif diag_U: # En caso que se haya seleccionado la matriz U como la que tenga unos en la diagonal principal
            U[i][i] = 1.0 # Se establece que u_{ii} = 1
            L[i][i] = valor_aii / U[i][i]  # Se despeja l_{ii}

        if L[i][i] * U[i][i] == 0:
            print("ERROR: No es posiblie realizar la factorización.")
            return None, None

        for j in range(i+1, n): # Paso 5
            sum_k1 = 0.0 
            for k in range(i):
                sum_k1 += L[i][k] * U[k][j] # Se calcula la sumatoria de l_{ik} u_{kj} para k desde 0 hasta i-1
            U[i][j] = (A[i][j] - sum_k1) / L[i][i]  # Se despeja u_{ij}

            sum_k2 = 0.0 
            for k in range(i):
                sum_k2 += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - sum_k2) / U[i][i] # Se despeja l_{ji}
    
    # Paso 6:
    suma_k = 0.0
    for k in range(n-1):
        suma_k += L[n-1][k] * U[k][n-1]  # Se calcula la sumatoria de l_{n,k} u_{k,n} para k desde 1 hasta n-1
    valor_lnn_unn = A[n-1][n-1] - suma_k  # Se obtiene l_{nn} u_{nn} = a_{nn} - sum_{k=1}^{n-1} l_{nk} u_{kn}
    if diag_L:
        L[n-1][n-1] = 1.0 
        U[n-1][n-1] = valor_lnn_unn / L[n-1][n-1]
    elif diag_U:
        U[n-1][n-1] = 1.0
        L[n-1][n-1] = valor_lnn_unn / U[n-1][n-1]

    return L, U

# Se inicia el programa solicitando la dimensión de la matriz A
n = dimension_matA_FactLU()

# Después, se solicita que se ingrese la matriz A, ya sea en forma de sus entradas a_{ij}
# o en forma explicíta como lista anidada
A = ingresar_matA(n)

# A fin de ser explícitos, se imprime la matriz A propocionada
print("\nLa matriz A ingresada es: ")
print(A)

# Luego, se pide que se elija cuál matriz (L o U) tendrá su diagonal principal con unos.
diag_L, diag_U = eleccion_diagonal_unos()

# Se procede a realizar cada uno de los pasos del algoritmo de factorización LU.
L, U = factorizacion_LU(A, n, diag_L, diag_U)

# Se imprimen las matrices L y U, resultantes de la factorización LU.
if L is not None and U is not None:
    print("\nLa matriz L, resultante de la factorización LU, es:")
    for fila in L:
        print(fila)

    print("\nLa matriz U, resultante de la factorización LU, es:")
    for fila in U:
        print(fila)
else:
    print("No se pudo llevar a cabo la factorización LU.")
    print("Por tanto, no se pudieron obtener las matrices L y U.")
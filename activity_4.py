# Bubble sort.

# List of sample lists to test the.
ejemplos = [
    [3, 7, 2, 9, 5],
    [4, 51, 52, 0, 20],
    [10, 27, 42, 9, 100],
    [23, 67, 22, 99, 2],
    [1, 7, 28, 9, 5],
    [],                     
    [42],                   
    [5, 4, 3, 2, 1],       
    [1, 2, 3, 4, 5],        
]

def bubble_sort(lista): # Implementation of the bubble sort algorithm.
    n = len(lista)
    # If the list has 0 or 1 element → it is already “sorted”.
    if n <= 1:
        return lista
    
    for pasada in range(n - 1):
        hubo_cambio = False
        
        for j in range(n - pasada - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        
        # Optimization: if there was no exchange → the list is already sorted.
        if not hubo_cambio:
            break
    
    return lista


def mostrar_ordenamiento(lista_original): # Function to display the original and sorted list.
    copia = lista_original.copy()
    
    print(f"Original : {lista_original}")
    bubble_sort(copia)
    print(f"Ordenada : {copia}")
    print("-" * 50)


def main():
    print(" BUBBLE SORTC DEMONSTRATION".center(50, "="))
    print()
    
    for i, lista in enumerate(ejemplos, 1):
        print(f" Example {i}/{len(ejemplos)} ".center(50, "-"))
        mostrar_ordenamiento(lista)
    
    print("End of demonstration".center(50, "="))


if __name__ == "__main__": 
    main()  # Call to main function to start the program.
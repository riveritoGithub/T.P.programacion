def solicitar_receta():
    nombre_receta = input("¿Cuál es el nombre de la receta? ")
    ingredientes = input("¿Cuáles son los ingredientes? (separados por comas) ")
    tiempo_preparacion = input("¿Cuál es el tiempo de preparación en minutos? ")
    dificultad = input("¿Cuál es la dificultad (Fácil, Media, Alta)? ")
    print("\n--- Detalles de la receta ---")
    print(f"Nombre de la receta: {nombre_receta}")
    print(f"Ingredientes: {ingredientes}")
    print(f"Tiempo de preparación: {tiempo_preparacion} minutos")
    print(f"Dificultad: {dificultad}")
solicitar_receta()

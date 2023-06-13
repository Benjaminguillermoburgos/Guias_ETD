class acciones_frutas(): 
    frutas = ("manzana", "platano", "pera", "naranja", "frutilla", "manzana")
    frutas_sin_repetir = list(set(frutas))

    fruta_nueva = input("Ingrese la fruta a agregar: ")
    frutas_sin_repetir.append(fruta_nueva)

    frutas_sin_repetir.remove("platano")

    cantidad_frutas = len(frutas_sin_repetir)
    print("La cantidad de frutas es:", cantidad_frutas)

    frutas = ("manzana", "platano", "pera", "naranja", "frutilla", "manzana")
    frutas_sin_repetir = list(set(frutas))

    fruta_nueva = input("Ingrese la fruta a agregar: ")
    frutas_sin_repetir.append(fruta_nueva)

    frutas_sin_repetir.remove("platano")

    cantidad_frutas = len(frutas_sin_repetir)
    print("La cantidad de frutas es:", cantidad_frutas)




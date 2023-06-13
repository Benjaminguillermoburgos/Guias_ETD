pacientes = []

# Agregar información de los pacientes
for i in range(4):
    paciente = {}
    print(f"Ingrese la información del paciente {i+1}:")
    paciente["nombre"] = input("Nombre: ")
    paciente["edad"] = int(input("Edad: "))
    paciente["peso"] = float(input("Peso: "))
    sintomas = input("Síntomas (separados por comas): ")
    paciente["sintomas"] = sintomas.split(",")
    pacientes.append(paciente)

# Búsqueda de un paciente por nombre
nombre_buscar = input("\nIngrese el nombre del paciente a buscar: ")
encontrado = False

for paciente in pacientes:
    if paciente["nombre"].lower() == nombre_buscar.lower():
        print("\nFicha personal:")
        print(f"Nombre: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Peso: {paciente['peso']}")
        print("Síntomas:", ", ".join(paciente['sintomas']))
        encontrado = True
        break

if not encontrado:
    print("\nEl paciente no se encuentra en la lista.")


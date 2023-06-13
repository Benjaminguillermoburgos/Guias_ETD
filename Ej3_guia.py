class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.items[-1]


def imprimir_pila(pila):
    if pila.esta_vacia():
        print("La pila está vacía.")
    else:
        print("Documentos en la pila:")
        for documento in pila.items[::-1]:
            print(documento)


# Crear la pila
pila_documentos = Pila()

# a) Imprimir el listado de documentos actual de la pila
imprimir_pila(pila_documentos)

# b) Agregar documentos a la pila
pila_documentos.apilar("Informe Final")
pila_documentos.apilar("Guia de Estudio")
pila_documentos.apilar("Tesis 4")
pila_documentos.apilar("Seminario Osorno")
pila_documentos.apilar("Avance Tesis")
pila_documentos.apilar("Proyecto Integrador")

# c) Obtener el último elemento superior de la pila
ultimo_documento = pila_documentos.ver_tope()
print("Último documento superior:", ultimo_documento)

# d) Eliminar el documento de la parte superior
pila_documentos.desapilar()

# e) Imprimir la pila de documentos actualizada
imprimir_pila(pila_documentos)

# f) Verificar si la pila de documentos está vacía
if pila_documentos.esta_vacia():
    print("La pila está vacía.")
else:
    print("La pila no está vacía.")

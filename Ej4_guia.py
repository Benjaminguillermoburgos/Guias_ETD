from collections import deque

class Supermercado:
    def __init__(self):
        self.cola_productos = deque()

    def agregar_producto(self, producto):
        self.cola_productos.append(producto)

    def eliminar_producto(self):
        if len(self.cola_productos) > 0:
            return self.cola_productos.popleft()
        else:
            return "La cola de productos está vacía."

    def mostrar_productos(self):
        for producto in self.cola_productos:
            print(producto)

    def invertir_productos(self):
        self.cola_productos.reverse()

    def vaciar_cola(self):
        self.cola_productos.clear()

# Ejemplo de uso
supermercado = Supermercado()

# Agregar productos a la cola
supermercado.agregar_producto("Leche")
supermercado.agregar_producto("Pan")
supermercado.agregar_producto("Huevos")
supermercado.agregar_producto("Frutas")
supermercado.agregar_producto("Verduras")
supermercado.agregar_producto("Carne")

# Mostrar los productos en la cola
print("Productos en la cola:")
supermercado.mostrar_productos()

# Eliminar el primer producto de la cola
producto_eliminado = supermercado.eliminar_producto()
print("Producto eliminado:", producto_eliminado)

# Mostrar los productos en la cola después de eliminar uno
print("Productos en la cola después de eliminar uno:")
supermercado.mostrar_productos()

# Invertir el orden de los productos
supermercado.invertir_productos()
print("Productos en la cola después de invertir el orden:")
supermercado.mostrar_productos()

# Vaciar la cola de productos
supermercado.vaciar_cola()
print("Productos en la cola después de vaciarla:")
supermercado.mostrar_productos()

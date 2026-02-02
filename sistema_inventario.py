class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)
    
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = float(nuevo_precio)
    
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = int(nueva_cantidad)
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:.2f}€ | Cantidad: {self.cantidad} | Valor total: {self.calcular_valor_total():.2f}€"


class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto")
        self.productos.append(producto)
    
    def buscar_producto(self, nombre):
        nombre_buscar = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscar:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        total = 0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total
    
    def listar_productos(self):
        if len(self.productos) == 0:
            print("\nEl inventario está vacío")
            return
        
        print("\n--- PRODUCTOS EN INVENTARIO ---")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")
        print(f"\nTotal de productos: {len(self.productos)}")


def menu_principal(inventario):
    salir = False
    while not salir:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        try:
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                print("\n[Agregar nuevo producto]")
                nombre = input("Nombre del producto: ").strip()
                precio = input("Precio: ").strip()
                cantidad = input("Cantidad: ").strip()
                
                try:
                    nuevo_producto = Producto(nombre, float(precio), int(cantidad))
                    inventario.agregar_producto(nuevo_producto)
                    print(f"\nProducto '{nombre}' agregado correctamente")
                except ValueError as e:
                    print(f"\nError al crear el producto: {e}")
                except Exception as e:
                    print(f"\nError inesperado: {e}")
            
            elif opcion == "2":
                print("\n[Buscar producto]")
                nombre = input("Nombre del producto a buscar: ").strip()
                
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"\nProducto encontrado:")
                    print(producto)
                else:
                    print(f"\nNo se encontró ningún producto con el nombre '{nombre}'")
            
            elif opcion == "3":
                inventario.listar_productos()
            
            elif opcion == "4":
                valor_total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: {valor_total:.2f}€")
            
            elif opcion == "5":
                print("\nSaliendo del sistema...")
                salir = True
            
            else:
                print("\nOpción no válida. Por favor, elige una opción del 1 al 5")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario")
            salir = True
        except Exception as e:
            print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)

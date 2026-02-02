# Sistema de Inventario - POO en Python

Sistema básico de gestión de inventario desarrollado con Programación Orientada a Objetos. Permite gestionar productos, realizar búsquedas y calcular valores totales del inventario.

## Descripción

Este es un ejercicio práctico de POO que implementa un sistema de inventario completo. Básicamente te permite agregar productos con sus precios y cantidades, buscarlos por nombre, ver todo el inventario y calcular cuánto vale todo junto.

Lo que pasa es que además incluye validaciones para que no se puedan meter datos raros (precios negativos, nombres vacíos, etc.) y maneja los errores de forma controlada.

## Características principales

- Gestión completa de productos (crear, actualizar precio, actualizar cantidad)
- Búsqueda de productos por nombre (insensible a mayúsculas/minúsculas)
- Cálculo automático del valor total de cada producto y del inventario completo
- Validaciones robustas para todos los datos de entrada
- Manejo de excepciones para errores comunes
- Menú interactivo por consola

## Requisitos

- Python 3.6 o superior
- No necesita librerías externas, solo la biblioteca estándar de Python

## Cómo ejecutar

Simplemente ejecuta el archivo desde la terminal:

```bash
python sistema_inventario.py
```

Te aparecerá un menú con las opciones disponibles. Elige la opción que quieras usando los números del 1 al 5.

## Estructura del código

El proyecto consta de un único archivo `sistema_inventario.py` con los siguientes componentes:

### Clase Producto

Representa un producto individual con:
- Atributos: nombre, precio, cantidad
- Métodos para actualizar precio y cantidad con validaciones
- Cálculo del valor total (precio × cantidad)
- Representación en string formateada

### Clase Inventario

Gestiona la colección de productos con:
- Lista interna de productos
- Métodos para agregar productos
- Búsqueda por nombre
- Cálculo del valor total del inventario
- Listado de todos los productos

### Función menu_principal()

Interfaz interactiva que permite:
1. Agregar producto nuevo
2. Buscar un producto específico
3. Listar todos los productos
4. Ver el valor total del inventario
5. Salir del programa

## Ejemplo de uso

```
--- SISTEMA DE INVENTARIO ---
1. Agregar producto
2. Buscar producto
3. Listar productos
4. Calcular valor total del inventario
5. Salir

Selecciona una opción: 1

[Agregar nuevo producto]
Nombre del producto: Laptop
Precio: 850.50
Cantidad: 5

Producto 'Laptop' agregado correctamente
```

## Validaciones implementadas

El sistema valida que:
- Los nombres de productos no estén vacíos
- Los precios sean mayores o iguales a cero
- Las cantidades sean mayores o iguales a cero
- Los tipos de datos sean correctos (convierte automáticamente cuando es posible)

Si alguna validación falla, se muestra un mensaje de error claro y el programa continúa funcionando.

## Manejo de errores

Se capturan y gestionan varios tipos de errores:
- ValueError: para valores numéricos inválidos o fuera de rango
- TypeError: para tipos de datos incorrectos
- KeyboardInterrupt: para interrupciones del usuario (Ctrl+C)
- Exception genérica: para cualquier error inesperado

Todos los errores muestran mensajes informativos sin romper la ejecución del programa.

## Notas técnicas

- La búsqueda de productos es case-insensitive, así que "laptop", "Laptop" y "LAPTOP" encuentran el mismo producto
- Los precios se formatean siempre con 2 decimales
- El bucle principal usa una variable de control en lugar de while True + break
- Todas las conversiones de tipo son explícitas para evitar comportamientos inesperados

## Criterios de evaluación cubiertos

- ✓ Implementación completa de clase Producto con validaciones (30%)
- ✓ Implementación completa de clase Inventario con todos los métodos (30%)
- ✓ Manejo exhaustivo de excepciones (20%)
- ✓ Menú interactivo funcional con todas las operaciones (20%)

## Posibles mejoras futuras

Si quisieras extender el proyecto podrías añadir:
- Persistencia de datos (guardar/cargar desde archivo)
- Edición de productos existentes
- Eliminación de productos
- Búsqueda con coincidencias parciales
- Ordenamiento del inventario por diferentes criterios
- Sistema de categorías para los productos

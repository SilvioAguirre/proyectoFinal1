menu = {
    'bebidas': {
        'latte': ('Café con leche espumosa', 3.5),
        'submarino': ('Chocolate caliente con una barra de chocolate', 3.0),
        'capuchino': ('Café con espuma de leche y canela', 3.75),
        'espresso': ('Café concentrado y fuerte', 2.25)
    },
    'comidas': {
        'muffin': ('Muffin de arándanos', 1.75),
        'medialuna': ('Medialuna dulce', 1.0),
        'tostado': ('Tostado de jamón y queso', 3.5),
        'chipitas': ('Pequeños panes de queso', 2.0)
    }
}

def mostrar_menu():
    print("Menú de Code & Coffee")
    print("\nBebidas:")
    for bebida, (descripcion, precio) in menu['bebidas'].items():
        print(f"{bebida.title()}: {descripcion} - ${precio:.2f}")
    
    print("\nComidas:")
    for comida, (descripcion, precio) in menu['comidas'].items():
        print(f"{comida.title()}: {descripcion} - ${precio:.2f}")

def realizar_pedido():
    pedido = {}
    total = 0.0
    while True:
        mostrar_menu()
        print("\nPedido actual:")
        for item, cantidad in pedido.items():
            categoria = 'bebidas' if item in menu['bebidas'] else 'comidas'
            descripcion, precio = menu[categoria][item]
            print(f"{item.title()} x{cantidad} - ${precio * cantidad:.2f}")
        
        print("\nOpciones: \n1. Agregar producto\n2. Terminar pedido")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            producto = input("Ingresa el nombre del producto: ").lower()
            cantidad = input("Ingresa la cantidad: ")

            try:
                cantidad = int(cantidad)
                if producto in menu['bebidas']:
                    categoria = 'bebidas'
                elif producto in menu['comidas']:
                    categoria = 'comidas'
                else:
                    raise ValueError(f"Producto {producto} no encontrado en el menú.")

                if producto in pedido:
                    pedido[producto] += cantidad
                else:
                    pedido[producto] = cantidad

                total += menu[categoria][producto][1] * cantidad
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

    return pedido, total

def generar_recibo(pedido, total):
    with open("recibo.txt", "w") as f:
        f.write("Recibo de Code & Coffee\n")
        f.write("=======================\n")
        for item, cantidad in pedido.items():
            categoria = 'bebidas' if item in menu['bebidas'] else 'comidas'
            descripcion, precio = menu[categoria][item]
            f.write(f"{item.title()} x{cantidad} - ${precio * cantidad:.2f}\n")
        f.write(f"\nTotal: ${total:.2f}\n")
    
    with open("recibo.txt", "r") as f:
        print(f.read())

def main():
    while True:
        print("\nBienvenido a Code & Coffee")
        print("1. Mostrar Menú")
        print("2. Realizar Pedido")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_menu()
        elif opcion == '2':
            pedido, total = realizar_pedido()
            if pedido:
                generar_recibo(pedido, total)
        elif opcion == '3':
            print("Gracias por visitarnos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()

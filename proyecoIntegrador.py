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

pedidos = {}

def mostrar_menu():
    print("\nMenú de Code & Coffee")
    print("\nBebidas:")
    for bebida, (descripcion, precio) in menu['bebidas'].items():
        print(f'{bebida.capitalize()}: {descripcion} - ${precio:.2f}')
    
    print("\nComidas:")
    for comida, (descripcion, precio) in menu['comidas'].items():
        print(f'{comida.capitalize()}: {descripcion} - ${precio:.2f}')

def realizar_pedido(pedido):
    total = 0
    while True:
        print("\nPedido actual:")
        for item, cantidad in pedidos.items():
            categoria = 'bebidas' if item in menu['bebidas'] else 'comidas'
            descripcion, precio = menu[categoria][item]
            print(f"{item.capitalize()} x{cantidad} - ${precio * cantidad:.2f}")
        
        pedido = input("\nIngresa el nombre del producto (o 'terminar' para finalizar): ").lower()
        
        if pedido == 'terminar':
            break
    
        if pedido not in menu['bebidas'] and pedido not in menu['comidas']:
            print("El ítem solicitado no existe en el menú.")
            continue
    
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            
            categoria = 'bebidas' if pedido in menu['bebidas'] else 'comidas'
            descripcion, precio = menu[categoria][pedido]

            if pedido in pedidos:
                pedidos[pedido] += cantidad
            else:
                pedidos[pedido] = cantidad
            
            total += precio * cantidad
            print(f"Agregado {cantidad} {pedido.capitalize()} - ${precio * cantidad:.2f}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

    return total

def generar_recibo(total):
    with open("recibo.txt", "w") as f:
        f.write("Recibo de Code & Coffee\n")
        f.write("=======================\n")
        for item, cantidad in pedidos.items():
            categoria = 'bebidas' if item in menu['bebidas'] else 'comidas'
            descripcion, precio = menu[categoria][item]
            f.write(f"{item.capitalize()} x{cantidad} - ${precio * cantidad:.2f}\n")
        f.write(f"\nTotal: ${total:.2f}\n")
    
    with open("recibo.txt", "r") as f:
        print("\n" + f.read())

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
            total = realizar_pedido()
            if pedidos:
                generar_recibo(total)
        elif opcion == '3':
            if pedidos:
                total = sum(
                    menu['bebidas'][item][1] * cantidad if item in menu['bebidas'] else menu['comidas'][item][1] * cantidad
                    for item, cantidad in pedidos.items()
                )
                generar_recibo(total)
            print("Gracias por visitarnos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()

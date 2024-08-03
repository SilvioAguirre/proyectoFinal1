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

pedidos={}

def mosttar_menu():
    print("Bebidas")
    for bebida ,(descipcion, precio) in menu['bebidas'].items():
        print(f'{bebida.capitalize()}: {descipcion} - ${precio:.2f}')
        
    print("Comidas")
    for comida ,(descipcion, precio) in menu['comidas'].items():
        print(f'{bebida.capitalize()}: {descipcion} - ${precio:.2f}')


def realizar_pedido(pedido):
    total = 0
    try:
        if pedido in menu['bebidas']:
            descipcion, precio = menu['bebidas'][pedido]
            if pedido in pedidos:
                pedidos[pedido] += precio
            else:
                pedidos[pedido] = precio
            total += precio
            print(f"Pedido: {pedido.capitalize()} - {descipcion} - ${precio:.2f}")   

        elif pedido in menu['comidas']:
            descipcion, precio = menu['comidas'][pedido]
            if pedido in pedidos:
                pedidos[pedido] += precio
            else:
                pedidos[pedido] = precio
            total += precio
            print(f"Pedido: {pedido.capitalize()} - {descipcion} - ${precio:.2f}")
        else:
            print("el iteam solicitado no existe en el Menú")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f'Ha ocurrido un error {e}')
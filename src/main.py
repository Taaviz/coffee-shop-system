from cafes import *
from pedidos import *


def main():

    menu = [

        Coffee("Espresso", 6.5),

        Coffee("Cappucino", 17.9),

        Coffee("Mocaccino", 19.00),

        Coffee("Latte", 14.40),

        Coffee("Americano", 9.90)

    ]

    # Instanciando
    pedidos = Pedidos()

    while True:

        print("\n --- Coffee Shop Menu ---")

        for i, item in enumerate(menu, 1):
            print(f" {i}. {item.name} - R$ {item.price}")

        print(" 6. Remover")
        print(" 7. Conferir pedido")
        print(" 8. Checkout")
        print(" 9. Sair")

        opcao = str(input("\n - O quê deseja? ")).lower().strip()

        if opcao in ['1', '2', '3', '4', '5']:
            pedidos.add_pedido(menu[int(opcao) - 1])

        elif opcao == '6':
            pedidos.remove_pedido(menu)

        elif opcao == '7':
            pedidos.conferir_pedido()

        elif opcao == '8':
            pedidos.checkout()

        elif opcao == '9':
            print("\n Saindo...\n Volte sempre!")

            break

        else:
            print("\n Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
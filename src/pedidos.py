from cafes import *
from main import *

class Pedidos:


    # Inicializa o objeto Pedidos
    def __init__(self):

        self.pedidos = []


    # Adiciona pedidos ao carrinho
    def add_pedido(self, coffee):

        self.pedidos.append(coffee)

        print(f" Seu {coffee.name} foi adicionado com sucesso!")


    # Calcula o total dos pedidos no carrinho
    def total(self):

        return sum(pedido.price for pedido in self.pedidos)


    # Remove pedidos do carrinho
    def remove_pedido(self, menu):
        while True:

            if not self.pedidos:
                print(" Nada foi pedido até o momento.")

                return
            else:
                item_remove = int(input("\n - Digite o ID do item que deseja remover: "))

                if item_remove in [1, 2, 3, 4, 5] and menu[item_remove - 1] in self.pedidos:
                    qtd_remove = int(input(f" - Digite quantos {menu[item_remove - 1].name}(s) deseja remover: "))

                    if 0 >= qtd_remove or qtd_remove > self.pedidos.count(menu[item_remove - 1]):
                        print(f" Opção inválida! Você tem {self.pedidos.count(menu[item_remove - 1])} {menu[item_remove - 1].name}(s).")

                        continue
                    else:
                        for _ in range(qtd_remove):
                            self.pedidos.remove(menu[item_remove - 1])

                        print(f" Você removeu {qtd_remove} {menu[item_remove - 1].name}(s).")

                        return
                else:
                    resp_exit = str(input(" - Item não encontrado. Deseja sair? ( s / n ): "))

                    if resp_exit == "s":
                        return


    # Confere pedidos dentro do carrinho
    def conferir_pedido(self):

        if not self.pedidos:
            print(" Nada foi pedido até o momento.")

            return

        else:
            print("\n Seu pedido: ")
            for i, pedido in enumerate(self.pedidos, 1):
                print(f" {i}. {pedido.name} - R${pedido.price}")
            print(f" Total - R$ {self.total():.2f}")


    # Da continuidade ao pagamento
    def checkout(self):

        if not self.pedidos:
            print(" Nada foi pedido até o momento")

        else:
            self.conferir_pedido()

            while True:
                resp_cont = str(input("\n - Deseja continuar com o pagamento? ( s / n ): ")).lower().strip()
                if resp_cont == "n":
                    break

                elif resp_cont == "s":
                    print(" Pagamento confirmado. Obrigado(a), volte sempre!")
                    self.pedidos.clear()
                    return

                else:
                    print(" Digite novamente.")


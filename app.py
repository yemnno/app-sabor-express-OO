from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Laís', 18)
restaurante_praca.receber_avaliacao('m', 2)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
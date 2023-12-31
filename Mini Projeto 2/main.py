"""O importa usa as classes definidas em formas.py"""
from formas import Circulo, Quadrado, Triangulo

def main():
    """Função principal do código"""
    formas = []

    circulo = Circulo(5.0)
    quadrado = Quadrado(4.0)
    triangulo = Triangulo(3.0, 6.0)

    formas.extend([circulo, quadrado, triangulo])

    while True:
        print("Menu de Opções:")
        print("1. As medidas de todos os elementos")
        print("2. O elemento de maior área")
        print("3. O elemento de menor área")
        print("4. A quantidade de lados de cada elemento")
        print("5. Encerrar o programa")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            for forma in formas:
                print(f"Tipo: {forma.get_tipo()}, Área: {forma.calcular_area()}")

        elif opcao == 2:
            maior_area = max(formas, key=lambda forma: forma.calcular_area())
            print(f"Elemento de maior área: {maior_area.get_tipo()}")

        elif opcao == 3:
            menor_area = min(formas, key=lambda forma: forma.calcular_area())
            print(f"Elemento de menor área: {menor_area.get_tipo()}")

        elif opcao == 4:
            for forma in formas:
                if isinstance(forma, Circulo):
                    print("Círculo - 0 lados")
                elif isinstance(forma, Quadrado):
                    print("Quadrado - 4 lados")
                elif isinstance(forma, Triangulo):
                    print("Triângulo - 3 lados")

        elif opcao == 5:
            break

if __name__ == "__main__":
    main()

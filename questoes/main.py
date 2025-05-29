from algoritmo import BubbleSort, Fatorial, SomaMultiplos
from eleicao import Eleicao


def calcular_percentual_eleicao():
    total_eleitores = input("\nDigite o total de eleitores: ")
    validos = input("\nDigite o total de votos válidos: ")
    brancos = input("\nDigite o total de votos brancos: ")
    nulos = input("\nDigite o total de votos nulos: ")
    try:
        total_eleitores, validos, brancos, nulos = convert_input_to_integers(total_eleitores, validos, brancos, nulos)
    except ValueError:
        print("\nErro: Todos os valores devem ser números inteiros.")
        return
    if total_eleitores <= 0 or validos < 0 or brancos < 0 or nulos < 0:
        print("\nErro: Valores inválidos. Total de eleitores deve ser maior que zero e os outros valores não podem ser negativos.")
        return
    if validos + brancos + nulos > total_eleitores:
        print("\nErro: A soma dos votos válidos, brancos e nulos não pode ser maior que o total de eleitores.")
        return
    if validos + brancos + nulos < total_eleitores:
        print("\nAviso: A soma dos votos válidos, brancos e nulos é menor que o total de eleitores. Considerando os votos restantes como nulos.")
        nulos += total_eleitores - (validos + brancos)

    eleicao = Eleicao(total_eleitores, validos, brancos, nulos)

    print(f"\nPercentual de votos válidos: {eleicao.percentual_validos():.2f}%")
    print(f"\nPercentual de votos brancos: {eleicao.percentual_brancos():.2f}%")
    print(f"\nPercentual de votos nulos: {eleicao.percentual_nulos():.2f}%")


def convert_input_to_integers(total_eleitores, validos, brancos, nulos):
    total_eleitores = int(total_eleitores) if total_eleitores.strip() else 1000
    validos = int(validos) if validos.strip() else 800
    brancos = int(brancos) if brancos.strip() else 150
    nulos = int(nulos) if nulos.strip() else 50
    return total_eleitores, validos, brancos, nulos


def calcular_algotimo_bubble_sort():

    vetor = [5, 3, 2, 4, 7, 1, 0, 6]
    bubble = BubbleSort(vetor)
    resultado = bubble.ordenar(verbose=True)

    print("\nVetor final ordenado:", resultado)

def calcular_fatorial():
    numero = input("\nDigite um número inteiro para calcular o fatorial: ")
    try:
        numero = int(numero)
    except ValueError:
        print("\nErro: O valor deve ser um número inteiro.")
        return

    if numero < 0:
        print("\nErro: Fatorial não está definido para números negativos.")
        return

    fatorial = Fatorial(numero)
    resultado = fatorial.calcular_fatorial()
    print(f"\nO fatorial de {numero} é: {resultado}")
    

def calcular_soma_multiplos():
    limite = input("\nDigite o limite para calcular a soma dos múltiplos de 3 e 5: ")
    try:
        limite = int(limite)
    except ValueError:
        print("\nErro: O valor deve ser um número inteiro.")
        return

    if limite < 0:
        print("\nErro: O limite não pode ser negativo.")
        return

    soma_multiplos = SomaMultiplos(limite)
    resultado = soma_multiplos.calcular()
    print(f"\nA soma dos múltiplos de 3 e 5 abaixo de {limite} é: {resultado}")

if __name__ == "__main__":

    print("Iniciando o programa...")
    print("Selecione a opção de calculo para realizar ...")
    print("1 - Calcular percentuais da eleição")
    print("2 - Calcular algoritmo Bubble Sort")
    print("3 - Calcular fatorial de um número")
    print("4 - Calcular a soma dos múltiplos de 3 e 5")
    print("Digite 'sair' para encerrar o programa.")

    calcular = input()

    if calcular not in ['1', '2', '3', '4', 'sair']:
        print("\nOpção inválida. Encerrando o programa.")
        exit()
    if calcular == '1':
        print("\nVocê escolheu calcular percentuais da eleição.")
        calcular_percentual_eleicao()
    elif calcular == '2':
        print("\nVocê escolheu calcular o algoritmo Bubble Sort.")
        calcular_algotimo_bubble_sort()
    elif calcular == '3':
        print("\nVocê escolheu calcular o fatorial de um número.")
        calcular_fatorial()
    elif calcular == '4':
        print("\nVocê escolheu calcular a soma dos múltiplos de 3 e 5.")
        calcular_soma_multiplos()
    elif calcular.lower() == 'sair':
        print("\nEncerrando o programa.")
        exit()
    print("\nPrograma encerrado.")
class BubbleSort:
    def __init__(self, lista):
        self.lista = lista

    def ordenar(self, verbose=False):
        n = len(self.lista)
        for i in range(n - 1):
            trocou = False
            if verbose:
                print(f"\nPassagem {i + 1}:")
            for j in range(n - 1 - i):
                if verbose:
                    print(f"Comparando {self.lista[j]} e {self.lista[j + 1]}")
                if self.lista[j] > self.lista[j + 1]:
                    if verbose:
                        print(f"Trocando {self.lista[j]} com {self.lista[j + 1]}")
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
                    trocou = True
                elif verbose:
                    print("Sem troca")
            if verbose:
                print("Estado atual:", self.lista)
            if not trocou:
                if verbose:
                    print("Vetor já está ordenado. Encerrando.")
                break
        return self.lista


class Fatorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular_fatorial(self):
        return self._fatorial(self.numero)

    def _fatorial(self, n):
        if n < 0:
            raise ValueError("Fatorial não está definido para números negativos.")
        if n == 0:
            return 1
        return n * self._fatorial(n - 1)
    
class SomaMultiplos:
    def __init__(self, limite):
        self.limite = limite

    def calcular(self):
        return sum(i for i in range(self.limite) if i % 3 == 0 or i % 5 == 0)



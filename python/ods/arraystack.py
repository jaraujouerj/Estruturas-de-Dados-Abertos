"""Um ArrayStack implementa a interface de lista usando um array.

Uma implementação de lista baseada em matriz com tempo de atualização
amortizado de O(1 + n-i).

Armazena a lista em uma matriz, a, de modo que o i-ésimo item da lista
seja armazenado em a[(j+i)%len(a)].

Usa uma estratégia de duplicação para redimensionar a quando fica cheio
ou muito vazio.
"""
from .utils import new_array

from .base import BaseList


class ArrayStack(BaseList):
    """Um ArrayStack implementa a interface de lista usando um array.

    Métodos Públicos: get(i), set(i, x), add(i, x), remove(i).
    """

    def __init__(self, iterable=[]):
        """Inicializa ArrayStack.

        Args: iterable: lista de elementos (opcional)
        """
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def get(self, i):
        """Devolve elemento na posição i."""
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.a[i]

    def set(self, i, x):
        """Atribui x à posição i."""
        if i < 0 or i >= self.n:
            raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i, x):
        """Adiciona x na posição i, deslocando outros itens."""
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self._resize()
        self.a[i + 1 : self.n + 1] = self.a[i : self.n]
        self.a[i] = x
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[i]
        self.a[i:self.n-1] = self.a[i+1:self.n]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x

    def _resize(self):
        b = new_array(max(1, 2*self.n))
        b[0:self.n] = self.a[0:self.n]
        self.a = b

# Este arquivo contém explicações e exemplos de uso de vários métodos embutidos do Python.

# Método abs()
# Retorna o valor absoluto de um número.
# Exemplo:
num = -5
print(abs(num))  # Saída: 5

# Método all()
# Retorna True se todos os elementos de um iterável forem verdadeiros (ou se o iterável estiver vazio).
# Exemplo:
lista = [True, True, True]
print(all(lista))  # Saída: True

# Método any()
# Retorna True se algum elemento de um iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
# Exemplo:
lista = [False, True, False]
print(any(lista))  # Saída: True

# Método ascii()
# Retorna uma versão legível de um objeto, mas substitui caracteres não ASCII por escapes.
# Exemplo:
texto = 'Pythön'
print(ascii(texto))  # Saída: 'Pyth\xf6n'

# Método bin()
# Converte um número inteiro em uma string binária.
# Exemplo:
num = 5
print(bin(num))  # Saída: '0b101'

# Método bool()
# Converte um valor para um booleano, usando as regras padrão de verdade.
# Exemplo:
print(bool(0))  # Saída: False
print(bool(1))  # Saída: True

# Método bytearray()
# Retorna um objeto bytearray.
# Exemplo:
tamanho = 5
print(bytearray(tamanho))  # Saída: bytearray(b'\x00\x00\x00\x00\x00')

# Método bytes()
# Retorna um objeto bytes.
# Exemplo:
tamanho = 5
print(bytes(tamanho))  # Saída: b'\x00\x00\x00\x00\x00'

# Método callable()
# Retorna True se o objeto parecer chamável (como uma função).
# Exemplo:
def funcao():
    pass
print(callable(funcao))  # Saída: True

# Método chr()
# Retorna o caractere correspondente ao valor Unicode fornecido.
# Exemplo:
codigo = 97
print(chr(codigo))  # Saída: 'a'

# Método classmethod()
# Converte um método em um método de classe.
# Exemplo:
class MinhaClasse:
    @classmethod
    def meu_metodo(cls):
        print("Método de classe chamado")
MinhaClasse.meu_metodo()  # Saída: Método de classe chamado

# Método compile()
# Compila o código-fonte em um objeto de código que pode ser executado por exec() ou eval().
# Exemplo:
codigo = 'print("Olá, Mundo!")'
codigo_compilado = compile(codigo, '<string>', 'exec')
exec(codigo_compilado)  # Saída: Olá, Mundo!

# Método complex()
# Cria um número complexo.
# Exemplo:
num_complexo = complex(1, 2)
print(num_complexo)  # Saída: (1+2j)

# Método delattr()
# Exclui um atributo de um objeto.
# Exemplo:
class MinhaClasse:
    atributo = 10
obj = MinhaClasse()
delattr(obj, 'atributo')

# Método dict()
# Cria um dicionário.
# Exemplo:
dicionario = dict(a=1, b=2)
print(dicionario)  # Saída: {'a': 1, 'b': 2}

# Método dir()
# Retorna uma lista de atributos válidos do objeto.
# Exemplo:
print(dir([]))  # Saída: Lista de métodos e atributos de uma lista

# Método divmod()
# Retorna uma tupla contendo o quociente e o resto da divisão.
# Exemplo:
print(divmod(10, 3))  # Saída: (3, 1)

# Método enumerate()
# Retorna um objeto enumerado.
# Exemplo:
lista = ['a', 'b', 'c']
for indice, valor in enumerate(lista):
    print(indice, valor)
# Saída:
# 0 a
# 1 b
# 2 c

# Método eval()
# Avalia uma expressão Python a partir de uma string.
# Exemplo:
expressao = '2 + 2'
print(eval(expressao))  # Saída: 4

# Método exec()
# Executa um código Python dinamicamente.
# Exemplo:
codigo = 'for i in range(5): print(i)'
exec(codigo)
# Saída:
# 0
# 1
# 2
# 3
# 4

# Método filter()
# Filtra elementos de um iterável para os quais a função retorna True.
# Exemplo:
lista = [1, 2, 3, 4, 5]
def eh_par(num):
    return num % 2 == 0
print(list(filter(eh_par, lista)))  # Saída: [2, 4]

# Método float()
# Converte um número ou string para um número de ponto flutuante.
# Exemplo:
print(float('3.14'))  # Saída: 3.14

# Método format()
# Formata um valor usando uma especificação de formato.
# Exemplo:
print(format(1234.5678, '.2f'))  # Saída: '1234.57'

# Método frozenset()
# Retorna um objeto frozenset imutável.
# Exemplo:
conjunto = frozenset([1, 2, 3])
print(conjunto)  # Saída: frozenset({1, 2, 3})

# Método getattr()
# Retorna o valor de um atributo de um objeto.
# Exemplo:
class MinhaClasse:
    atributo = 10
obj = MinhaClasse()
print(getattr(obj, 'atributo'))  # Saída: 10

# Método globals()
# Retorna um dicionário representando a tabela de símbolos global atual.
# Exemplo:
print(globals())  # Saída: Dicionário de variáveis globais

# Método hasattr()
# Retorna True se o objeto tiver o atributo especificado.
# Exemplo:
class MinhaClasse:
    atributo = 10
obj = MinhaClasse()
print(hasattr(obj, 'atributo'))  # Saída: True

# Método hash()
# Retorna o valor de hash de um objeto.
# Exemplo:
print(hash('Python'))  # Saída: Valor de hash do string 'Python'

# Método help()
# Invoca o sistema de ajuda integrado.
# Exemplo:
help(print)  # Saída: Documentação da função print

# Método hex()
# Converte um número inteiro para uma string hexadecimal.
# Exemplo:
print(hex(255))  # Saída: '0xff'

# Método id()
# Retorna o identificador único de um objeto.
# Exemplo:
obj = 'Python'
print(id(obj))  # Saída: Identificador único do objeto

# Método input()
# Lê uma linha de entrada do usuário.
# Exemplo:
# nome = input('Digite seu nome: ')
# print('Olá,', nome)

# Método int()
# Converte um número ou string para um número inteiro.
# Exemplo:
print(int('10'))  # Saída: 10

# Método isinstance()
# Verifica se um objeto é uma instância de uma classe ou de uma tupla de classes.
# Exemplo:
print(isinstance(10, int))  # Saída: True

# Método issubclass()
# Verifica se uma classe é uma subclasse de outra classe ou de uma tupla de classes.
# Exemplo:
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))  # Saída: True

# Método iter()
# Retorna um iterador para um objeto.
# Exemplo:
lista = [1, 2, 3]
iterador = iter(lista)
print(next(iterador))  # Saída: 1

# Método len()
# Retorna o comprimento (número de itens) de um objeto.
# Exemplo:
print(len('Python'))  # Saída: 6

# Método list()
# Cria uma lista.
# Exemplo:
print(list('Python'))  # Saída: ['P', 'y', 't', 'h', 'o', 'n']

# Método locals()
# Retorna um dicionário representando a tabela de símbolos local atual.
# Exemplo:
def funcao():
    a = 10
    print(locals())
funcao()  # Saída: {'a': 10}

# Método map()
# Aplica uma função a todos os itens de um iterável.
# Exemplo:
lista = [1, 2, 3]
def quadrado(num):
    return num ** 2
print(list(map(quadrado, lista)))  # Saída: [1, 4, 9]

# Método max()
# Retorna o maior item de um iterável ou o maior de dois ou mais argumentos.
# Exemplo:
print(max([1, 2, 3]))  # Saída: 3

# Método memoryview()
# Retorna um objeto de visualização de memória.
# Exemplo:
v = memoryview(b'abc')
print(v[0])  # Saída: 97

# Método min()
# Retorna o menor item de um iterável ou o menor de dois ou mais argumentos.
# Exemplo:
print(min([1, 2, 3]))  # Saída: 1

# Método next()
# Recupera o próximo item de um iterador.
# Exemplo:
iterador = iter([1, 2, 3])
print(next(iterador))  # Saída: 1

# Método object()
# Retorna um novo objeto sem atributos.
# Exemplo:
obj = object()
print(obj)  # Saída: <object object at 0x...>

# Método oct()
# Converte um número inteiro para uma string octal.
# Exemplo:
print(oct(8))  # Saída: '0o10'

# Método open()
# Abre um arquivo e retorna um objeto de arquivo.
# Exemplo:
# arquivo = open('exemplo.txt', 'r')
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

# Método ord()
# Retorna o valor Unicode de um caractere.
# Exemplo:
print(ord('a'))  # Saída: 97

# Método pow()
# Retorna o valor de x elevado à potência y.
# Exemplo:
print(pow(2, 3))  # Saída: 8

# Método print()
# Imprime objetos no console.
# Exemplo:
print('Olá, Mundo!')  # Saída: Olá, Mundo!

# Método property()
# Retorna um objeto de propriedade.
# Exemplo:
class MinhaClasse:
    def __init__(self):
        self._atributo = 0

    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor

obj = MinhaClasse()
obj.atributo = 10
print(obj.atributo)  # Saída: 10

# Método range()
# Retorna um objeto iterável que gera uma sequência de números.
# Exemplo:
for i in range(5):
    print(i)
# Saída:
# 0
# 1
# 2
# 3
# 4

# Método repr()
# Retorna uma representação string de um objeto.
# Exemplo:
print(repr('Python'))  # Saída: "'Python'"

# Método reversed()
# Retorna um iterador que acessa a sequência dada em ordem reversa.
# Exemplo:
print(list(reversed([1, 2, 3])))  # Saída: [3, 2, 1]

# Método round()
# Retorna um número arredondado para n dígitos de precisão.
# Exemplo:
print(round(3.14159, 2))  # Saída: 3.14

# Método set()
# Cria um conjunto.
# Exemplo:
print(set([1, 2, 3]))  # Saída: {1, 2, 3}

# Método setattr()
# Define um atributo de um objeto.
# Exemplo:
class MinhaClasse:
    pass
obj = MinhaClasse()
setattr(obj, 'atributo', 10)
print(obj.atributo)  # Saída: 10

# Método slice()
# Retorna um objeto de fatia.
# Exemplo:
s = slice(1, 5, 2)
print([0, 1, 2, 3, 4, 5][s])  # Saída: [1, 3]

# Método sorted()
# Retorna uma lista ordenada dos itens de um iterável.
# Exemplo:
print(sorted([3, 1, 2]))  # Saída: [1, 2, 3]

# Método staticmethod()
# Converte um método em um método estático.
# Exemplo:
class MinhaClasse:
    @staticmethod
    def meu_metodo():
        print("Método estático chamado")
MinhaClasse.meu_metodo()  # Saída: Método estático chamado

# Método str()
# Converte um objeto em uma string.
# Exemplo:
print(str(123))  # Saída: '123'

# Método sum()
# Retorna a soma de um iterável.
# Exemplo:
print(sum([1, 2, 3]))  # Saída: 6

# Método super()
# Retorna um objeto proxy que delega chamadas de método para uma classe pai ou irmão.
# Exemplo:
class Pai:
    def metodo(self):
        print("Método do Pai")
class Filho(Pai):
    def metodo(self):
        super().metodo()
        print("Método do Filho")
obj = Filho()
obj.metodo()
# Saída:
# Método do Pai
# Método do Filho

# Método tuple()
# Cria uma tupla.
# Exemplo:
print(tuple([1, 2, 3]))  # Saída: (1, 2, 3)

# Método type()
# Retorna o tipo de um objeto.
# Exemplo:
print(type(123))  # Saída: <class 'int'>

# Método vars()
# Retorna o __dict__ de um objeto.
# Exemplo:
class MinhaClasse:
    def __init__(self):
        self.atributo = 10
obj = MinhaClasse()
print(vars(obj))  # Saída: {'atributo': 10}

# Método zip()
# Retorna um iterador de tuplas, onde o i-ésimo item de cada iterável passado é emparelhado.
# Exemplo:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
print(list(zip(lista1, lista2)))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]

# Método __import__()
# Função que é chamada pela instrução import.
# Exemplo:
modulo = __import__('math')
print(modulo.sqrt(4))  # Saída: 2.0
# Aquí irán las ANSI escape sequences para los colores que serán utilizados.

class Foo :
  def __init__(self, var) :
    self.var = var

foo = Foo(2)

lista = [foo]

def func(item) :
  lista.remove(item)

foo2 = Foo(2)

func(foo2)

print(lista)
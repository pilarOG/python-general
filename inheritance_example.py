# -*- coding: utf-8 -*-

import json

# Root

class Animal(object):
    def __init__(self):
        self.vivo = True
        self.transporte = ('Caminan', 'Se arrastran', 'Vuelan', 'Por flagelo')
        self.reproduccion = ('por huevos', 'por crias vivas', 'fision')

# First branch

class Vertebrado(Animal):
    def __init__(self):
        self.vertebrado = (True, 'Los vertebrados tienen columna vertebral')
        self.transporte = ('Caminan', 'Se arrastran', 'Vuelan')
        self.reproduccion = ('por huevos', 'por crias vivas')

# Terminal

class Reptil(Vertebrado):
    def __init__(self, iterable=(), **kwargs):

        super(Vertebrado, self).__init__()
        self.sangre_fria = (True, 'Los reptiles tienen sangre fria')
        self.reproduccion = ('por huevos')
        self.transporte = ('Caminan', 'Se arrastran')
        self.tiene_plumas = False

        for key, value in kwargs.items():
            setattr(self, key, value)

# Terminal

class Ave(Vertebrado):
    def __init__(self, iterable=(), **kwargs):

        super(Vertebrado, self).__init__()
        self.sangre_fria = (False, 'Las aves no tienen sangre fria')
        self.reproduccion = ('por huevos')
        self.transporte = ('Vuelan')
        self.tiene_plumas = True

        for key, value in kwargs.items():
            setattr(self, key, value)

# Second branch

class Invertebrado(Animal):
    def __init__(self):
        self.vertebrado = (False, 'Los invertebrados no tienen columna vertebral')
        self.transporte = ('Caminan', 'Se arrastran', 'Por flagelo')
        self.reproduccion = ('fision')

# Terminal

class Protozoo(Invertebrado):
    def __init__(self, iterable=(), **kwargs):

        super(Invertebrado, self).__init__()
        self.reproduccion = ('fision')
        self.transporte = ('Por flagelo')

        for key, value in kwargs.items():
            setattr(self, key, value)

# Terminal

class Molusco(Invertebrado):
    def __init__(self, iterable=(), **kwargs):

        super(Invertebrado, self).__init__()
        self.reproduccion = ('por huevos')
        self.transporte = ('Se arrastran')

        for key, value in kwargs.items():
            setattr(self, key, value)

# Set the terminal class

def inherite(nodo):
    if nodo['taxonomia'] == 'molusco':
        nodo.pop('taxonomia')
        return vars(Molusco(**nodo))
    elif nodo['taxonomia'] == 'protozoo':
        nodo.pop('taxonomia')
        return vars(Protozoo(**nodo))
    elif nodo['taxonomia'] == 'ave':
        nodo.pop('taxonomia')
        return vars(Ave(**nodo))
    elif nodo['taxonomia'] == 'reptil':
        nodo.pop('taxonomia')
        return vars(Reptil(**nodo))

# Main

if __name__ == '__main__':

    nodo = {'taxonomia': 'ave',
            'nombre': 'pinguino',
            'transporte': 'no vuela'}

    print json.dumps(inherite(nodo), indent=4)

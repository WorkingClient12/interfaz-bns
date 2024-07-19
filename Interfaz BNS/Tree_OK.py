# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:37:01 2024

@author: Samuel
"""

class Node:
       def __init__(self, data, distance=0):
           self.data = data
           self.sons = []
           self.father = None
           self.distance = distance  # Distancia desde el nodo padre hasta este nodo hijo

       def set_sons(self, son_list):
           self.sons = son_list

       def set_father(self, father_node):
           self.father = father_node

       def get_data(self):
           return self.data

       def get_sons(self):
           return self.sons

       def get_father(self):
           return self.father

       def get_distance(self):
           return self.distance

       def on_list(self, lst):
           for node in lst:
               if node.get_data() == self.get_data():
                   return True
           return False
       
class Node2:
        def __init__(self, data, sons=None, distance=0):
            self.data = data
            self.sons = []
            self.father = None
            self.set_sons(sons)
            self.distance = distance  # Distancia desde el nodo padre hasta este nodo hijo

        def set_sons(self, sons):
            if sons is not None:
                for son in sons:
                    son.father = self
                    self.sons.append(son)

        def get_sons(self):
            return self.sons

        def get_father(self):
            return self.father

        def set_father(self, father):
            self.father = father

        def set_data(self, data):
            self.data = data

        def get_data(self):
            return self.data
        
        def get_distance(self):
            return self.distance

        def __str__(self):
            return str(self.get_data())
    
class Node3:
        def __init__(self, data, distance=0, son = None):
            self.data = data
            self.sons = []
            self.father = None
            self.distance = distance
            self.son = None
            self.cost = None
            self.set_son(son)# Distancia desde el nodo padre hasta este nodo hijo

        def set_son(self, son):
            self.son = son
            if self.son is not None:
                for s in self.son:
                    s.father = self

        def set_father(self, father_node):
            self.father = father_node

        def get_data(self):
            return self.data

        def get_son(self):
            return self.son

        def get_father(self):
            return self.father

        def get_distance(self):
            return self.distance

        def on_list(self, lst):
            for node in lst:
                if node.get_data() == self.get_data():
                    return True
            return False
        
class Node4:
        def __init__(self, data, son=None):
            self.data = data
            self.son = None
            self.father = None
            self.cost = None
            self.set_son(son)

    #metodo set_son
        def set_son(self, son):
            self.son = son
            if self.son is not None:
                for s in self.son:
                    s.father = self
    #metodo get_son , retorna una lista con los hijos del nodo
        #self=hace referencia a los objetos que pertenezcan a la clase
        def get_son(self):
            return self.son

    #retorna el nodo padre
        def get_father(self):
            return self.father
        
        # asigna el nodo padre de este nodo

        def set_father(self, father):
            self.father = father
            
            #asigna un dato al nodo

        def set_data(self, data):
            self.data = data

    #Devuel el dato almacenado en el nodo
        def get_data(self):
            return self.data

    #metod que asigna un peso al nodo dentro del arbol
        def set_cost(self, cost):
            self.cost = cost

            #Devuelve el pseo del nodo dentro del arbol
        def get_cost(self):
            return self.cost

    #Devuleve verdadero si el dato contenido en el nodo es igual al nodo pasado comomparamtero
        def equal(self, node):
            if self.get_data() == node.get_data():
                return True
            else:
                return False

    #devuelve verdadero si el dato contenido en el nodo es = a algunos de los nodos contenidos en la lista de nodos
                #pasados como parametros.
        def on_list(self, node_list):
            listed = False
            for n in node_list:
                if self.equal(n):
                    listed = True
            return listed

        def __str__(self):
            return str(self.get_data())


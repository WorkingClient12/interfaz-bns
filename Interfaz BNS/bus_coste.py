# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:40:16 2024

@author: Samuel
"""

from Tree_OK import Node4
from Dibuja_Grafo import dibujar


class BusCost:
    def Compare(node):
       return node.get_cost()
    #def compare(x,y):
        #return x.get_cost() - y.get_cost

    def ucs(connections, init_state, solution):
        solved = False #solucionado
        visited_nodes = [] #nodos visitados
        frontier_nodes = [] #nodos frontera
        init_node = Node4(init_state) #nodo inicial
        init_node.set_cost(0)
        frontier_nodes.append(init_node)
        while (not solved) and len(frontier_nodes) != 0:
            # Ordenar lista de nodos frontera. Funcion sorted(ordena nodos frontear)
            frontier_nodes = sorted(frontier_nodes, key=BusCost.Compare)
            node = frontier_nodes[0]
            # Extraer nodo y añadirlo a visitados
            visited_nodes.append(frontier_nodes.pop(0))
            if node.get_data() == solution:
                # Solucion encontrada
                solved = True
                return node
            else:
                # Expandir nodos hijo (ciudades con conexion)
                node_data = node.get_data()
                child_list = []
                for achild in connections[node_data]:
                    child = Node4(achild)
                    cost = connections[node_data][achild]
                    child.set_cost(node.get_cost() + cost)
                    child_list.append(child)
                    if not child.on_list(visited_nodes):
                        # Si esta en la lista lo sustituimos con el nuevo valor de coste si es menor
                        if child.on_list(frontier_nodes):
                            for n in frontier_nodes:
                                if n.equal(child) and n.get_cost() > child.get_cost():
                                    frontier_nodes.remove(n)
                                    frontier_nodes.append(child)
                        else:
                            frontier_nodes.append(child)
                        node.set_son(child_list)

    def ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number):
        
        if solution_node is not None:
            result = []
            node = solution_node
            while node.get_father() is not None:
                result.append(node.get_data())
                node = node.get_father()
            result.append(init_state_number)
            ruta_mas_corta=result
            result.reverse()
            resultado_municipios=[]
            number_to_municipality = {v: k for k, v in municipality_to_number.items()}
    
            def obtener_municipio(numero):
                if numero in number_to_municipality:
                    return number_to_municipality[numero]
                else:
                    return None
    
            # Creamos el diccionario inverso
            number_to_municipality = {v: k for k, v in municipality_to_number.items()}
                    
            for i in result:
                variable=obtener_municipio(i)
                resultado_municipios.append(variable)
            etiqueta2 = self.ui.etiqueta2
           # Si hay una ruta más corta, mostrar la información
            coste = str(solution_node.get_cost())
            texto_resultado = f"Ruta desde {self.ui.origen.currentText()} hasta {self.ui.destino.currentText()}:\n{', '.join(resultado_municipios)}\nCoste: {coste}"
        else:
            texto_resultado = "Solución no encontrada"
            
        etiqueta2.setText(texto_resultado)
        dibujar(ruta_mas_corta)
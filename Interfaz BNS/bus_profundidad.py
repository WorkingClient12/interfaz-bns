# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:26:31 2020

@author: Samuel
"""

from Tree_OK import Node2
from Dibuja_Grafo import dibujar

class Bus:
   def search_solution_DFS(init_state_number, solution_number, connections_with_numbers):
        visited = set()
        frontier = [Node2(init_state_number)]

        while frontier:
            node = frontier.pop()

            if node.get_data() == solution_number:
                return node

            visited.add(node.get_data())
        
            for child_data in Bus.expand_node(node.get_data(), connections_with_numbers):
                if child_data not in visited:
                    child_node = Node2(child_data)
                    node.set_sons([child_node])
                    frontier.append(child_node)

        return None



   def expand_node(data_node, connections_with_numbers):
        expanded_nodes = []
        
        if data_node in connections_with_numbers:
            expanded_nodes = connections_with_numbers[data_node]

        return expanded_nodes


   def ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number):
        
        if solution_node:
            result = []
            node = solution_node
            
            # Recorrer desde el nodo solución hasta el nodo inicial
            while node is not None:
                # Obtener el número de ciudad del nodo
                city_number = node.get_data()
                result.append(city_number)
                
                # Moverse al nodo padre
                node = node.get_father()
            
            # Invertir el resultado para que esté en el orden correcto
            result.reverse()
            ruta_mas_corta = result
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
            texto_resultado = f"Ruta desde {self.ui.origen.currentText()} hasta {self.ui.destino.currentText()}:\n{', '.join(resultado_municipios)}"
        else:
            texto_resultado = "Solución no encontrada"
            
        etiqueta2.setText(texto_resultado)
        dibujar(ruta_mas_corta)


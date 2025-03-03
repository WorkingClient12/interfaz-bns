# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:49:27 2020

@author: Sergio

"""

from Tree_OK import Node3
from Dibuja_Grafo import dibujar
from Tree_OK
class BusIt:
    def search_DSF_prof_iter(node, solution, connections_with_numbers):
        for limit in range(0,100):
            #solved = False
            visited_nodes = []
            #frontrs_nodes = []
            sol = BusIt.search_DSF_solution(node, solution, visited_nodes, limit, connections_with_numbers)
            if sol != None:
                return sol       
            
    def search_DSF_solution(node, solution, visited_nodes, limit, connections_with_numbers):     
        if limit > 0:
            visited_nodes.append(node)
            if node.get_data() == solution:
                return node
            else:
                node_data = node.get_data()
                child_list = []
                for chld in connections_with_numbers[node_data]:
                    child = Node3(chld)
                    if not child.on_list(visited_nodes):
                        child_list.append(child)
                node.set_son(child_list)
                
                for node_son in node.get_son():
                    if not node_son.get_data() in visited_nodes:
                        sol = BusIt.search_DSF_solution(node_son, solution, visited_nodes, limit-1, connections_with_numbers)
                        if sol is not None:
                            return sol
                return None  # No se encontró la solución en este nodo ni en sus hijos
        else:
            return None  # Se alcanzó el límite de profundidad sin encontrar la solución

    def ejecucion(self, solution_node, init_state, solution, municipality_to_number):
        
        if solution_node is not None:
            result = []
            node = solution_node
            while node is not None:  # Modificamos la condición de terminación del bucle
                city_number = node.get_data()
                result.append(city_number)
                
                # Moverse al nodo padre
                node = node.get_father() # Mover al padre
            
            ruta_mas_corta=result
            result.reverse()  # Revertir el resultado para que esté en el orden correcto
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

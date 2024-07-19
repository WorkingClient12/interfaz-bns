
from Tree_OK import Node
from Dibuja_Grafo import dibujar


class Grafo:
    
    def search_BFS_solution(connections, init_state, solution):
        visited_nodes = []
        frontier_nodes = []

        init_node = Node(init_state)
        frontier_nodes.append(init_node)
        while len(frontier_nodes) != 0:
            node = frontier_nodes.pop(0)  # Obtener el primer nodo de la lista
            visited_nodes.append(node)
            if node.get_data() == solution:
                # solucion encontrada
                return node
            else:
                # expandir nodos hijo - ciudades con conexion
                node_data = node.get_data()
                child_list = []
                for child_municipality, distance in connections[node_data].items():
                    child = Node(child_municipality, distance)
                    child.set_father(node)
                    if not child.on_list(visited_nodes) and not child.on_list(frontier_nodes):
                        frontier_nodes.append(child)
                node.set_sons(child_list)

        return None
     
    def ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number):
        
            if solution_node:
                result = []
                distances = 0
                node = solution_node
                while node.get_father() is not None:
                    city_number = node.get_data()
                    result.append(city_number)
                    distances += node.get_distance()
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
                texto_resultado = f"Ruta desde {self.ui.origen.currentText()} hasta {self.ui.destino.currentText()}:\n{', '.join(resultado_municipios)}\nDistancia total recorrida: {distances} km"
            else:
                # Si no se encontró una solución válida, mostrar un mensaje de error
                texto_resultado = "No se encontró una solución válida."
            
            # Establecer el texto en la etiqueta
            etiqueta2.setText(texto_resultado)
            dibujar(ruta_mas_corta)

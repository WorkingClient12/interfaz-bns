# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:05:20 2024

@author: Samuel
"""

import networkx as nx
import matplotlib.pyplot as plt


def dibujar(ruta_mas_corta):    
    G = nx.Graph()
    
    # Añadimos aristas con peso al grafo
    G.add_edges_from([
        (1, 2, {'weight': 26}),
        (2, 3, {'weight': 28}),
        (2, 4, {'weight': 15}),
        (3, 5, {'weight': 17}),
        (3, 6, {'weight': 26}),
        (5, 6, {'weight': 26}),
        (5, 7, {'weight': 18}),
        (4, 8, {'weight': 18}),
        (4, 9, {'weight': 41}),
        (4, 10, {'weight': 32}),
        (8, 9, {'weight': 13}),
        (8, 10, {'weight': 32}),
        (9, 10, {'weight': 19}),
        (10, 11, {'weight': 31}),
        (11, 12, {'weight': 32}),
        (11, 13, {'weight': 5}),
        (13, 14, {'weight': 10}),
    ])
    
    # Configuramos la figura con mejor resolución
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    # Definimos las posiciones de los nodos manualmente
    posiciones_manuales = {
        1: (0.15, 2.1), 2: (0.90, 1.80), 3: (1.35, 1.75), 4: (0.5, 1.4),
        5: (1.60, 2.65), 6: (1.10, 2.90), 7: (2.20, 2.70), 8: (0.6, 0.65),
        9: (1.0, 0.15), 10: (1.5, 0.55), 11: (1.7, -0.1), 12: (1.95, 0.80),
        13: (2.3, 0.2), 14: (3.15, 0.2)
    }
    
    # Dibujamos el grafo con una ruta destacada
    nx.draw_networkx(G, pos=posiciones_manuales, with_labels=True, node_color='skyblue', edge_color='grey', font_color='black')
    
    if ruta_mas_corta:  # Verificar si ruta_mas_corta no está vacía
        path_edges = list(zip(ruta_mas_corta[:-1], ruta_mas_corta[1:]))
        nx.draw_networkx_nodes(G, posiciones_manuales, nodelist=ruta_mas_corta, node_color='red')
        nx.draw_networkx_edges(G, posiciones_manuales, edgelist=path_edges, edge_color='red', width=2)
    
    # Dibujar las etiquetas de peso en las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, posiciones_manuales, edge_labels=edge_labels)
    
    # Carga la imagen de fondo
    background_image = plt.imread('image/risaralda.jpeg')
    
    # Muestra la imagen de fondo con interpolación bilineal
    ax.imshow(background_image, extent=[-1, 4, -1, 4], aspect='auto', interpolation='bilinear')
    # Establecemos el color de fondo del eje
    ax.set_facecolor('white')
    
    # Desactivar los ejes
    ax.axis('off')
    
    plt.savefig('image/risaralda_mejorado.png', dpi=300, bbox_inches='tight')
    
    plt.close()


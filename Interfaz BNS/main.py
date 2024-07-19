# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:50:30 2024

@author: Samuel
"""

import sys
import psutil
import time
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QDialog
from PyQt5.QtGui import QImage,QPalette,QBrush,QPixmap,QMouseEvent,QPainter,QColor
from PyQt5.QtCore import QSize, QPropertyAnimation, Qt,QRectF, pyqtSignal, QObject
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ui_interface import *
from ui_second import Ui_SecondWindow
from Grafo_BFS import *
from bus_profundidad import *
from Bus_profundidad_iterativa_Risaralda import *
from bus_coste import *
from Tree_OK import Node3




class VentanaPrincipal(QtWidgets.QMainWindow, QGraphicsView):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        algoritmos = ['Amplitud', 'Profundidad (DFS)', 'Profundidad Iterativa (IDS)', 'Busqueda Coste Uniforme (UCS)']
        for i, algoritm in enumerate(algoritmos):
            self.ui.algoritmo.addItem(algoritm, i)
            
        ciudades = ['Pueblo rico', 'Apia', 'Belen de umbria', 'Santuario', 
        'Guatica', 'Mistrato', 'Quinchia', 'La celia', 'Balboa', 'La virginia', 
        'Pereira', 'Marsella', 'Dosquebradas', 'Santa Rosa']
        for i, ciudadO in enumerate(ciudades):
            self.ui.origen.addItem(ciudadO, i)
          
        for i, ciudadD in enumerate(ciudades):
            self.ui.destino.addItem(ciudadD, i)
        
        
        self.ui.graficar.clicked.connect(self.ejecutar_algoritmo)
        self.ui.menu.clicked.connect(self.mover_menu)
        self.ui.salir.clicked.connect(self.close)
        self.ui.limpiar.clicked.connect(self.limpiar_combobox)
        self.ui.limpiar.clicked.connect(self.limpiar_imagen)
        self.ui.limpiar.clicked.connect(self.etiqueta3)
        self.ui.adyacencia.clicked.connect(self.secondWindow)

        # Guardar el estado inicial del combobox
        self.estado_inicial_combobox = self.ui.algoritmo.currentText()
        self.estado_inicial_combobox_2 = self.ui.origen.currentText()
        self.estado_inicial_combobox_3 = self.ui.destino.currentText()
        
        self.inicio_ejecucion = time.time()
        self.inicio_consumo_cpu = psutil.cpu_percent()
        self.inicio_consumo_memoria = psutil.virtual_memory().percent
        self.inicio_consumo_disco = psutil.disk_usage('/').percent
        
        self.etiqueta3()
        self.show()
    
    # Definir la función para limpiar el combobox
    def secondWindow(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_SecondWindow()
        self.ui.setupUi(self.ventana)
        self.ui.volver.clicked.connect(self.closed)
        self.ventana.show()        
    
    def closed(self):
        self.ventana.close()
        self.close()
        self.ui.setupUi(self.__init__())
        

    def limpiar_imagen(self):
        imagen = 'image/risaralda.jpeg'
        pixmap = QPixmap(imagen)
        self.ui.image.setPixmap(pixmap)
        self.current_pixmap = None

           
    def limpiar_combobox(self):
        # Restablecer el estado inicial del combobox
        self.ui.algoritmo.setCurrentText(self.estado_inicial_combobox)
        self.ui.origen.setCurrentText(self.estado_inicial_combobox_2)
        self.ui.destino.setCurrentText(self.estado_inicial_combobox_3)
    
    def mover_menu(self):
        if True:
            width = self.ui.side_menu.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.side_menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
        
    def calcularTime(self):
        
        fin_ejecucion = time.time()
        fin_consumo_cpu = psutil.cpu_percent()
        fin_consumo_memoria = psutil.virtual_memory().percent
        fin_consumo_disco = psutil.disk_usage('/').percent
        
        self.tiempo_transcurrido = fin_ejecucion - self.inicio_ejecucion
        self.tiempo_total_cpu = fin_consumo_cpu - self.inicio_consumo_cpu
        self.tiempo_total_memoria = fin_consumo_memoria - self.inicio_consumo_memoria
        self.tiempo_total_disco = fin_consumo_disco - self.inicio_consumo_disco
    
    def calcularTimeAlgorithm(self):
        
        tiempo_transcurrido = self.fin_ejecucion2 - self.inicio_ejecucion2
        tiempo_total_cpu = self.fin_consumo_cpu2 - self.inicio_consumo_cpu2
        tiempo_total_memoria = self.fin_consumo_memoria2 - self.inicio_consumo_memoria2
        tiempo_total_disco = self.fin_consumo_disco2 - self.inicio_consumo_disco2
        
        etiqueta3 = self.ui.etiqueta3
        mensaje = f"Tiempo total de ejecución: {tiempo_transcurrido:.2f} segundos\n"
        mensaje += f"Consumo total de CPU: {tiempo_total_cpu:.2f}%\n"
        mensaje += f"Consumo total de memoria: {tiempo_total_memoria:.2f}%\n"
        mensaje += f"Consumo total de disco: {tiempo_total_disco:.2f}%" 
        
        etiqueta3.setText(mensaje)
    
    def etiqueta3(self):
        
        self.calcularTime()
        etiqueta3 = self.ui.etiqueta3
        mensaje = f"Tiempo total de ejecución: {self.tiempo_transcurrido:.2f} segundos\n"
        mensaje += f"Consumo total de CPU: {self.tiempo_total_cpu:.2f}%\n"
        mensaje += f"Consumo total de memoria: {self.tiempo_total_memoria:.2f}%\n"
        mensaje += f"Consumo total de disco: {self.tiempo_total_disco:.2f}%" 
        
        etiqueta3.setText(mensaje)
    
    def ejecutar_algoritmo(self):
        
        self.inicio_ejecucion2 = time.time()
        self.inicio_consumo_cpu2 = psutil.cpu_percent()
        self.inicio_consumo_memoria2 = psutil.virtual_memory().percent
        self.inicio_consumo_disco2 = psutil.disk_usage('/').percent
        
        municipality_to_number = {
            'Pueblo rico': 1,
            'Apia': 2,
            'Belen de umbria': 3,
            'Santuario': 4,
            'Guatica': 5,
            'Mistrato': 6,
            'Quinchia': 7,
            'La celia': 8,
            'Balboa': 9,
            'La virginia': 10,
            'Pereira':11,
            'Marsella':12,
            'Dosquebradas':13,
            'Santa Rosa':14
        }

        connections = {
            'Pueblo rico': {'Apia': 26},
            'Apia': {'Pueblo rico':26,'Belen de umbria': 28, 'Santuario': 15},
            'Belen de umbria': {'Apia':28,'Mistrato': 26, 'Guatica': 17},
            'Santuario': {'Apia': 15, 'La celia': 18, 'Balboa': 41,'La virginia':32},
            'Guatica': {'Belen de umbria': 17, 'Mistrato': 26,'Quinchia':18},
            'Mistrato': {'Belen de umbria': 26,'Guatica':26},
            'Quinchia': {'Guatica': 18},
            'La celia': {'Santuario': 18, 'Balboa': 13, 'La virginia': 32},
            'Balboa': {'La celia': 13, 'Santuario': 41, 'La virginia': 19},
            'La virginia': {'Santuario': 32, 'La celia': 32, 'Balboa': 19,'Pereira':31},
            'Pereira': {'La virginia': 31, 'Marsella': 32, 'Dosquebradas': 5},
            'Marsella': {'Pereira': 32},
            'Dosquebradas': {'Pereira': 5,'Santa Rosa':10},
            'Santa Rosa': {'Dosquebradas': 10},
        }
        connections_with_numbers = {}
        for municipality, connections in connections.items():
            connections_with_numbers[municipality_to_number[municipality]] = {
                municipality_to_number[connected_municipality]: distance
                for connected_municipality, distance in connections.items()
            }
        
        # Encontramos la ruta más corta entre el nodo de inicio y el nodo de fin que pusimos
        
        init_state_number = municipality_to_number[self.ui.origen.currentText()]
        solution_number = municipality_to_number[self.ui.destino.currentText()]
        
        indice = self.ui.algoritmo.currentIndex()
        
        # Determinar qué algoritmo debe ejecutarse según el índice seleccionado
        if indice == 0:
            
            solution_node = Grafo.search_BFS_solution(connections_with_numbers, init_state_number, solution_number)
            Grafo.ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number)
        
        elif indice == 1:
            
            solution_node = Bus.search_solution_DFS(init_state_number, solution_number, connections_with_numbers)
            Bus.ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number)

        elif indice == 2:
            
            x=municipality_to_number[self.ui.origen.currentText()]
            y=municipality_to_number[self.ui.destino.currentText()]
            municipality_to_number[municipality]

            init_state = Node3(x)
            solution = y
            
            solution_node = BusIt.search_DSF_prof_iter(init_state, solution, connections_with_numbers)
            BusIt.ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number)
                
        elif indice == 3:

            solution_node = BusCost.ucs(connections_with_numbers, init_state_number, solution_number)
            BusCost.ejecucion(self, solution_node, init_state_number, solution_number, municipality_to_number)
            
        else:
            etiqueta2 = self.ui.etiqueta2
            texto_resultado = "Opción incorrecta"
            etiqueta2.setText(texto_resultado)
            
        image = 'image/risaralda_mejorado.png'
        pixmap = QPixmap(image)
        self.ui.image.setPixmap(pixmap)
        self.ui.image.setStyleSheet("position: absolute; top: 50px; left: 50px;")
        self.current_pixmap = pixmap
        
        self.fin_ejecucion2 = time.time()
        self.fin_consumo_cpu2 = psutil.cpu_percent()
        self.fin_consumo_memoria2 = psutil.virtual_memory().percent
        self.fin_consumo_disco2 = psutil.disk_usage('/').percent
        
        self.calcularTimeAlgorithm()


if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())
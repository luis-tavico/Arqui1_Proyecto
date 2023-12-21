import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PySide6.QtGui import QFont, QPixmap, QIcon, Qt, QCursor
from PySide6.QtCore import QSize
import serial
import time

# Encender = 'E'
# Apagar = 'A'
# Foto = 'F'

class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.estado_estabilizador = False
        self.inicializar_componentes()
        self.inicializar_comunicacion()

    def inicializar_componentes(self):
        # etiqueta1
        self.etiqueta1 = QLabel("Tomar Foto", self)
        self.etiqueta1.setFont(QFont("Arial", 16))
        self.etiqueta1.setFixedSize(500, 50)
        self.etiqueta1.setAlignment(Qt.AlignCenter)
        self.etiqueta1.move(0, 90)

        # boton tomar foto
        self.btn_foto = QPushButton(self)
        self.btn_foto.setStyleSheet("background-color: transparent;")
        self.btn_foto.setIcon(QIcon('camara.png'))
        self.btn_foto.setIconSize(QSize(50, 50))
        self.btn_foto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_foto.move(218, 149)
        self.btn_foto.clicked.connect(self.tomar_foto)

        # etiqueta2
        self.etiqueta2 = QLabel("Estado de Estabilizacion:", self)
        self.etiqueta2.setFont(QFont("Arial", 16))
        self.etiqueta2.setFixedSize(500, 50)
        self.etiqueta2.setAlignment(Qt.AlignCenter)
        self.etiqueta2.move(0, 240)

        # boton encender/apagar estabilizacion
        self.btn_estabilizador = QPushButton(self)
        self.btn_estabilizador.setStyleSheet("background-color: transparent;")
        self.btn_estabilizador.setIcon(QIcon('apagado.png'))
        self.btn_estabilizador.setIconSize(QSize(50, 50))
        self.btn_estabilizador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estabilizador.move(218, 300)
        self.btn_estabilizador.clicked.connect(self.enc_apag_estabilizacion)

        # etiqueta3
        self.etiqueta3 = QLabel("Apagado", self)
        self.etiqueta3.setFont(QFont("Arial", 10))
        self.etiqueta3.setFixedSize(500, 25)
        self.etiqueta3.setAlignment(Qt.AlignCenter)
        self.etiqueta3.setStyleSheet("background-color: transparent;")
        self.etiqueta3.move(0, 360)

        # tamaño ventana
        self.setFixedSize(500, 500)
        self.setWindowTitle('Arqui1_Grupo8')
    
    def inicializar_comunicacion(self):
        self.puerto_serial = serial.Serial('COM1', 9600) # puerto serial
        time.sleep(2) # esperar a que se establezca la conexión

    def tomar_foto(self):
        # Enviar señal de tomar foto a Arduino
        self.puerto_serial.write(b'F')
        QMessageBox.information(self, 'Mensaje', '¡Foto tomada exitosamente!')

    def enc_apag_estabilizacion(self):
        if self.estado_estabilizador:
            self.btn_estabilizador.setIcon(QIcon('apagado.png'))
            self.etiqueta3.setText("Apagado")
            # Enviar señal de apagado a Arduino
            self.puerto_serial.write(b'A')
        else:
            self.btn_estabilizador.setIcon(QIcon('encendido.png'))
            self.etiqueta3.setText("Encendido")
            # Enviar señal de encendido a Arduino
            self.puerto_serial.write(b'E')

        self.estado_estabilizador = not self.estado_estabilizador

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
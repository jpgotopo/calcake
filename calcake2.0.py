import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTextEdit, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont


# Función para calcular los ingredientes
def calcular_ingredientes(tamaño):
    base = (1/3) * tamaño - 1
    factores = {
        "Huevos": 1,
        "Harina": 25,
        "Azúcar": 5,
        "Cacao": 30
    }
    return {ing: round(factores[ing] * base) for ing in factores}


class CalcakeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calcake - Calculadora de Ingredientes")
        self.setGeometry(100, 100, 450, 400)
        self.setStyleSheet("background-color: #f9f9f9; font-family: Arial;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Calculadora de Ingredientes por Tamaño")
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50;")
        layout.addWidget(title_label)

        # Campo de entrada
        self.label_tamaño = QLabel("Ingresa el tamaño:")
        self.label_tamaño.setFont(QFont("Arial", 12))
        layout.addWidget(self.label_tamaño)

        self.entry_tamaño = QLineEdit()
        self.entry_tamaño.setFont(QFont("Arial", 12))
        self.entry_tamaño.setPlaceholderText("Ejemplo: 20")
        layout.addWidget(self.entry_tamaño)

        # Botón
        self.btn_calcular = QPushButton("Calcular Ingredientes")
        self.btn_calcular.setFont(QFont("Arial", 12))
        self.btn_calcular.setStyleSheet("background-color: #3498db; color: white; padding: 8px;")
        self.btn_calcular.clicked.connect(self.on_calcular)
        layout.addWidget(self.btn_calcular)

        # Área de resultados
        self.text_resultado = QTextEdit()
        self.text_resultado.setReadOnly(True)
        self.text_resultado.setFont(QFont("Courier", 12))
        self.text_resultado.setStyleSheet("background-color: #ecf0f1; border: 1px solid #ccc;")
        layout.addWidget(self.text_resultado)

        self.setLayout(layout)

    def on_calcular(self):
        try:
            tamaño_texto = self.entry_tamaño.text().strip()
            if not tamaño_texto:
                raise ValueError("Campo vacío")

            tamaño = int(tamaño_texto)
            if tamaño < 5:
                QMessageBox.warning(self, "Advertencia", "El tamaño debe ser al menos 15.")
                return

            resultados = calcular_ingredientes(tamaño)
            texto = f"Tamaño {tamaño}:\n\n"
            for ingrediente, cantidad in resultados.items():
                texto += f"{ingrediente+':':<7} {cantidad}\n"

            self.text_resultado.setText(texto)

        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor ingresa un número válido.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalcakeApp()
    window.show()
    sys.exit(app.exec_())
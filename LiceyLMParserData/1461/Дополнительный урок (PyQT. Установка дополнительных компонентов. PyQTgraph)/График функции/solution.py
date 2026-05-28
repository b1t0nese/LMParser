import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QWidget, QPushButton, QLabel, QLineEdit, QSpinBox)
import pyqtgraph as pg
import math


def eval_math(expr, **vars):
    allowed_names = {
        'pi': math.pi, 'e': math.e,
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'exp': math.exp, 'log': math.log, 'log10': math.log10,
        'sqrt': math.sqrt, 'pow': math.pow,
        'abs': abs, 'ceil': math.ceil, 'floor': math.floor,
        'degrees': math.degrees, 'radians': math.radians,
    }
    code = compile(expr, '<string>', 'eval')
    for name in code.co_names:
        if name not in allowed_names and name not in vars:
            raise ValueError(f"Использование '{name}' запрещено")
    return eval(code, {"__builtins__": {}}, {**allowed_names, **vars})


class GraphFunction(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("График функции")

    def initUI(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.graphicsView = pg.PlotWidget()
        self.graph_style()
        layout.addWidget(self.graphicsView)

        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        input_layout.addWidget(QLabel("Функция:"))
        self.functionText = QLineEdit("x**2")
        input_layout.addWidget(self.functionText)

        input_layout.addWidget(QLabel("Диапазон:"))
        self.rangeSpin = QSpinBox()
        self.rangeSpin.setValue(100)
        self.rangeSpin.setMaximum(100000)
        self.rangeSpin.setSingleStep(10)
        input_layout.addWidget(self.rangeSpin)

        self.centerButton = QPushButton("Центрировать", self)
        self.centerButton.clicked.connect(self.graph_center)
        input_layout.addWidget(self.centerButton)

        self.pushButton = QPushButton("Построить")
        self.pushButton.clicked.connect(self.run)
        layout.addWidget(self.pushButton)

    def run(self):
        self.graph_clear()
        function, t_range = self.functionText.text(), int(self.rangeSpin.text())
        x_all = list(range(-t_range, t_range + 1))
        x_valid, y_valid = [], []
        for x in x_all:
            try:
                y = eval_math(function, x=x)
                x_valid.append(x)
                y_valid.append(y)
            except ZeroDivisionError:
                if x_valid and y_valid:
                    self.graphicsView.plot(x_valid, y_valid)
                    x_valid.clear()
                    y_valid.clear()
            except Exception as e:
                print(f"{e.__class__.__name__}: {e}")
                return
        if x_valid and y_valid:
            self.graphicsView.plot(x_valid, y_valid)
        self.graph_center()

    def graph_clear(self):
        self.graphicsView.clear()
        self.graph_style()

    def graph_style(self):
        self.graphicsView.addItem(pg.InfiniteLine(pos=0, angle=0, pen=pg.mkPen(
            'gray', width=1, style=pg.QtCore.Qt.PenStyle.DashLine)))
        self.graphicsView.addItem(pg.InfiniteLine(pos=0, angle=90, pen=pg.mkPen(
            'gray', width=1, style=pg.QtCore.Qt.PenStyle.DashLine)))

    def graph_center(self):
        self.graphicsView.autoRange()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphFunction()
    window.show()
    sys.exit(app.exec())
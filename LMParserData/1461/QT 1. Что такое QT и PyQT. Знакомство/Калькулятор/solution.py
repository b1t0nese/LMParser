from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QGridLayout, QLabel, QPushButton)
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.waiting_for_operand = True
        self.error_state = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(325, 450)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(1)

        self.secondary_label = QLabel("")
        self.secondary_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.secondary_label.setStyleSheet("font-size: 16px; color: gray;")
        self.secondary_label.setFixedHeight(30)

        self.main_label = QLabel("0")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_label.setStyleSheet("font-size: 28px; font-weight: bold; border: 1px solid #ccc; padding: 5px;")
        self.main_label.setFixedHeight(50)
        
        main_layout.addWidget(self.secondary_label)
        main_layout.addWidget(self.main_label)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(1)

        self.number_buttons = []
        for i in range(10):
            btn = QPushButton(str(i))
            btn.setFixedSize(70, 70)
            btn.clicked.connect(self.on_number_clicked)
            self.number_buttons.append(btn)

        self.clear_button = QPushButton("C")
        self.clear_entry_button = QPushButton("CE")
        self.divide_button = QPushButton("/")
        self.multiply_button = QPushButton("*")
        self.substract_button = QPushButton("-")
        self.add_button = QPushButton("+")
        self.equals_button = QPushButton("=")
        self.float_point_button = QPushButton(".")
        self.plus_minus_button = QPushButton("±")

        for btn in [self.clear_button, self.clear_entry_button, self.divide_button,
                    self.multiply_button, self.substract_button, self.add_button,
                    self.equals_button, self.float_point_button, self.plus_minus_button]:
            btn.setFixedSize(70, 70)

        self.clear_button.clicked.connect(self.clear_all)
        self.clear_entry_button.clicked.connect(self.clear_entry)
        self.float_point_button.clicked.connect(self.add_decimal_point)
        self.plus_minus_button.clicked.connect(self.toggle_sign)
        self.equals_button.clicked.connect(self.calculate_result)

        for btn, op in {self.divide_button: "/", self.multiply_button: "*",
                        self.substract_button: "-", self.add_button: "+"}.items():
            btn.clicked.connect(lambda checked, operator=op: self.set_operation(operator))

        grid_layout.addWidget(self.clear_button, 0, 0)
        grid_layout.addWidget(self.clear_entry_button, 0, 1)
        grid_layout.addWidget(self.plus_minus_button, 0, 2)
        grid_layout.addWidget(self.divide_button, 0, 3)

        grid_layout.addWidget(self.number_buttons[7], 1, 0)
        grid_layout.addWidget(self.number_buttons[8], 1, 1)
        grid_layout.addWidget(self.number_buttons[9], 1, 2)
        grid_layout.addWidget(self.multiply_button, 1, 3)

        grid_layout.addWidget(self.number_buttons[4], 2, 0)
        grid_layout.addWidget(self.number_buttons[5], 2, 1)
        grid_layout.addWidget(self.number_buttons[6], 2, 2)
        grid_layout.addWidget(self.substract_button, 2, 3)

        grid_layout.addWidget(self.number_buttons[1], 3, 0)
        grid_layout.addWidget(self.number_buttons[2], 3, 1)
        grid_layout.addWidget(self.number_buttons[3], 3, 2)
        grid_layout.addWidget(self.add_button, 3, 3)

        grid_layout.addWidget(self.number_buttons[0], 4, 1, 1, 2)
        grid_layout.addWidget(self.float_point_button, 4, 2)
        grid_layout.addWidget(self.equals_button, 4, 3)
        
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def format_number(self, num_str, max_length=11):
        if self.error_state:
            return "ОШИБКА"
        try:
            num = float(num_str)
        except ValueError:
            return num_str
        if num.is_integer():
            num = int(num)
        if len(num_str.replace('.', '').replace('-', '')) > max_length:
            return f"{num:.2e}".upper().replace('E', 'e')
        return num_str

    def update_display(self):
        main_text = self.format_number(self.current_input)
        if len(main_text) > 11:
            main_text = self.format_number(self.current_input, 8)
        self.main_label.setText(main_text)
        if self.previous_input and self.operator:
            prev_text = self.format_number(self.previous_input, 30)
            self.secondary_label.setText(f"{prev_text} {self.operator}")
        else:
            self.secondary_label.setText("")

    def on_number_clicked(self):
        if self.error_state:
            self.clear_all()
            self.error_state = False
        if self.waiting_for_operand:
            self.current_input = self.sender().text()
            self.waiting_for_operand = False
        else:
            if self.current_input == "0":
                self.current_input = self.sender().text()
            else:
                self.current_input += self.sender().text()
        self.update_display()

    def add_decimal_point(self):
        if self.error_state:
            return
        if self.waiting_for_operand:
            self.current_input = "0."
            self.waiting_for_operand = False
        elif "." not in self.current_input:
            self.current_input += "."
        self.update_display()

    def toggle_sign(self):
        if self.error_state:
            return
        try:
            if float(self.current_input) == 0:
                return
        except ValueError:
            return
        if self.current_input.startswith("-"):
            self.current_input = self.current_input[1:]
        else:
            self.current_input = "-" + self.current_input
        self.update_display()

    def clear_all(self):
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.waiting_for_operand = True
        self.error_state = False
        self.update_display()

    def clear_entry(self):
        if self.error_state:
            self.clear_all()
            return
        if self.waiting_for_operand:
            self.clear_all()
        else:
            self.current_input = "0"
            self.update_display()

    def set_operation(self, operation):
        if self.error_state:
            return
        if self.operator and not self.waiting_for_operand:
            self.calculate_result()
        self.operator = operation
        self.previous_input = self.current_input
        self.waiting_for_operand = True
        self.update_display()

    def calculate_result(self):
        if self.error_state or not self.operator or not self.previous_input:
            return
        try:
            num1, num2 = float(self.previous_input), float(self.current_input)
            if self.operator == "+":
                result = num1 + num2
            elif self.operator == "-":
                result = num1 - num2
            elif self.operator == "*":
                result = num1 * num2
            elif self.operator == "/":
                result = num1 / num2
            if result.is_integer():
                result = int(result)
            self.current_input = str(result)
        except Exception:
            self.current_input = "0"
            self.error_state = True
        self.previous_input = ""
        self.operator = ""
        self.waiting_for_operand = True
        self.update_display()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
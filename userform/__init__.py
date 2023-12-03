import random
from PyQt6.QtWidgets import QLineEdit, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QComboBox, QSizePolicy, QFrame
from PyQt6.QtGui import QPixmap, QPainter, QFont, QColor
from PyQt6.QtCore import Qt
from time import time
from modules.get_aoc import get_input
from modules import *


class UserForm(QWidget):
    def __init__(self):
        super().__init__()

        # Remove title bar
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.FramelessWindowHint)
        # Update background aoc23 picture
        self.background = QPixmap("resources/pictures/aoc23.png")

        # Set a fixed size of the window
        self.setFixedSize(800, 450)

        # -------------
        # Close Button
        close_button = QPushButton(self)
        close_button.setStyleSheet(
            "color: lightgreen; background-color: transparent;")
        # Close the window when clicked
        close_button.clicked.connect(self.close)
        close_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        close_button.setFixedHeight(100)

        # -------------
        # Labels for Solutions
        label_sol1 = QLabel('Part 1 solution', self)
        label_sol1.setStyleSheet("color: silver;")
        label_sol1.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        self.sol1 = QLineEdit(self)
        self.sol1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sol1.setStyleSheet(
            "background-color: transparent; color: silver; border: none;")
        self.sol1.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))

        label_sol2 = QLabel('Part 2 solution', self)
        label_sol2.setStyleSheet("color: goldenrod;")
        label_sol2.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        self.sol2 = QLineEdit(self)
        self.sol2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sol2.setStyleSheet(
            "background-color: transparent; color: goldenrod; font-weight: bold; border: none;")
        self.sol2.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        # -------------

        # -------------
        # Labels for Execution time
        label_exetime = QLabel('Execution time', self)
        label_exetime.setStyleSheet("color: lightgreen")
        label_exetime.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        self.exetime = QLabel(self)
        self.exetime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exetime.setStyleSheet("color: lightgreen")
        self.exetime.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        # -------------

        # -------------
        # Main Vertical Layout
        vbox = QVBoxLayout()
        # -------------

        # -------------
        # Top Horizontal Layouts
        top_hbox = QHBoxLayout()
        grid_widget = QWidget()  # Widget to hold the grid layout
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(3)  # Set the horizontal spacing
        grid_layout.setVerticalSpacing(2)  # Set the vertical spacing

        # Populate the grid with buttons containing numbers from 1 to 25
        for i in range(5):
            for j in range(5):
                number = i * 5 + j + 1  # Calculate the number
                # Create a button with the number as text
                button = QPushButton(str(number))
                button.setFont(QFont('Source Code Pro', 9, QFont.Weight.Bold))
                color = QColor(random.randint(127, 255), random.randint(
                    0, 255), random.randint(0, 127))
                button.setStyleSheet(
                    f"background-color: transparent; color: {color.name()};text-align: right;")
                button.setFixedSize(15, 15)  # Set the fixed size of the button
                # Connect button click event to function
                button.clicked.connect(self.on_button_clicked)
                # Add button to the grid
                grid_layout.addWidget(
                    button, i, j)
        grid_widget.setLayout(grid_layout)
        top_hbox.addWidget(
            grid_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        top_hbox.addWidget(close_button)
        vbox.addLayout(top_hbox)
        # -------------

        # -------------
        # Add stretch between top and middle
        vbox.addStretch(1)
        # -------------

        # -------------
        # Bottom Horizontal Layouts
        bottom_hbox = QHBoxLayout()
        # Add 3 vertical layout inside bottom layout

        bvbox1 = QVBoxLayout()
        bvbox1.addWidget(label_sol1, alignment=Qt.AlignmentFlag.AlignCenter)
        bvbox1.addWidget(self.sol1, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_hbox.addLayout(bvbox1)

        bvbox2 = QVBoxLayout()
        bvbox2.addWidget(label_sol2, alignment=Qt.AlignmentFlag.AlignCenter)
        bvbox2.addWidget(self.sol2, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_hbox.addLayout(bvbox2)

        bvbox3 = QVBoxLayout()
        bvbox3.addWidget(label_exetime, alignment=Qt.AlignmentFlag.AlignCenter)
        bvbox3.addWidget(self.exetime, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_hbox.addLayout(bvbox3)
        vbox.addLayout(bottom_hbox)
        # -------------

        self.setLayout(vbox)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.background.scaled(self.size()))

    # Function to display button label in a message box when clicked

    def on_button_clicked(self):
        button = self.sender()  # Get the button that triggered the event
        day = int(button.text())
        start = time()
        sample = False
        # Fetch input data
        inputs = get_input(day=day, separator=SEPARATORS[day], sample=sample)
        sol = eval(f"Day_{day}").main(inputs)
        self.sol1.setText(sol[0])
        self.sol2.setText(sol[1])
        self.exetime.setText(f"{int((time() - start)*1000)} ms")


SEPARATORS = {1: '\n', 2: '\n', }

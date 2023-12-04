import random
from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QSizePolicy
from PyQt6.QtGui import QPixmap, QPainter, QFont, QColor
from PyQt6.QtCore import Qt
from time import time
from modules import Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7, Day_8, Day_9, Day_10, Day_11, Day_12, Day_13, Day_14, Day_15, Day_16, Day_17, Day_18, Day_19, Day_20, Day_21, Day_22, Day_23, Day_24, Day_25
from modules.sub_modules.get_aoc import get_input

AOC_COLOR = {'golden': QColor(255, 255, 0),
             'red': QColor(193, 39, 45),
             'amber': QColor(251, 176, 59),
             'green': QColor(60, 181, 86),
             'brightgreen': QColor(15, 250, 58),
             'blue': QColor(36, 112, 224),
             'white': QColor(255, 255, 255), }


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
        # Create a grid to pick day in calendar
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
                color = AOC_COLOR[random.choice(list(AOC_COLOR.keys()))].name()
                button.setStyleSheet(
                    f"background-color: transparent; color: {color};text-align: right;")
                button.setFixedSize(15, 15)  # Set the fixed size of the button
                # Connect button click event to function
                button.clicked.connect(self.on_button_clicked)
                # Add button to the grid
                grid_layout.addWidget(
                    button, i, j)
        grid_widget.setLayout(grid_layout)
        # -------------

        # -------------
        # Label for title of the day's puzzle
        self.title = QLabel('Part 1 solution', self)
        color = AOC_COLOR['brightgreen'].name()
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet(f"color: {color};")
        self.title.setFont(QFont('Source Code Pro', 24, QFont.Weight.Bold))
        self.title.setText('Pick a day in calendar')
        self.title.setFixedSize(self.title.sizeHint().width(),
                                grid_widget.sizeHint().height())

        # -------------

        # -------------
        # Close Button
        close_button = QPushButton(self)
        close_button.setStyleSheet("background-color: transparent;")
        close_button.setFixedSize(
            grid_widget.sizeHint().width()//2, grid_widget.sizeHint().height())
        close_button.clicked.connect(self.close)

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
        color = AOC_COLOR['golden'].name()
        label_sol2.setStyleSheet(f"color: {color};")
        label_sol2.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        self.sol2 = QLineEdit(self)
        self.sol2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sol2.setStyleSheet(
            f"background-color: transparent; color: {color}; border: none;")
        self.sol2.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        # -------------

        # -------------
        # Labels for Execution time
        label_exetime = QLabel('Execution time', self)
        color = AOC_COLOR['green'].name()
        label_exetime.setStyleSheet(f"color: {color};")
        label_exetime.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        self.exetime = QLabel(self)
        self.exetime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exetime.setStyleSheet(f"color: {color};")
        self.exetime.setFont(QFont('Source Code Pro', 10, QFont.Weight.Bold))
        # -------------

        # -------------
        # Main Vertical Layout
        vbox = QVBoxLayout()
        # -------------

        # -------------
        # Top Horizontal Layouts
        top_hbox = QHBoxLayout()
        # Add stretch between title and close button
        top_hbox.addStretch(1)
        # Add grid to layout
        top_hbox.addWidget(
            grid_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        # Add stretch between calendar and title
        top_hbox.addStretch(1)
        # Add title to layout
        top_hbox.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        # Add stretch between title and close button
        top_hbox.addStretch(1)
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

    def update_labels(self, title, sol1='', sol2='', ela_time=''):
        self.title.setText(title)
        self.sol1.setText(str(sol1))
        self.sol2.setText(str(sol2))
        self.exetime.setText(ela_time)

    # Function to display button label in a message box when clicked

    def on_button_clicked(self):
        day = self.sender().text()  # Get the button's label that triggered the event
        try:
            start = time()
            title = f'Day {day}\n{DAY_DATA[day][1]}'
            # Fetch input data
            inputs = get_input(day=day, separator=DAY_DATA[day][2])
            sol = DAY_DATA[day][0].main(inputs)
            elapsed_time = f"{int((time() - start)*1000)} ms"
            self.update_labels(title, *sol, elapsed_time)
        except KeyError:
            self.update_labels(f'Day {day}\nNot yet solved')


DAY_DATA = {'1': (Day_1, 'Trebuchet?!', '\n'),
            '2': (Day_2, 'Cube Conundrum', '\n'),
            '3': (Day_3, 'Gear Ratios', '\n'),
            }

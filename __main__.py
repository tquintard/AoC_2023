import sys
from PyQt6.QtWidgets import QApplication
from userform import UserForm


def main():
    app = QApplication([])
    form = UserForm()
    app.exec()


if __name__ == '__main__':
    sys.exit(main())

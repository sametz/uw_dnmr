from PySide2 import QtCore
from PySide2.QtCore import Slot as pyqtSlot
from PySide2.QtWidgets import QRadioButton


from qt_nmr.view.widgets.buttons import ABC_ButtonGroup, MultipletButtonGroup


@pyqtSlot(QRadioButton)
def printslot(button):
    # print("SLOT TRIGGER")
    print(button.objectName())


def test_nspins(qtbot, capsys):
    bg = ABC_ButtonGroup()
    bg.buttongroup.buttonClicked.connect(printslot)
    bg.show()
    qtbot.addWidget(bg)
    for name, button in bg.buttons.items():
        qtbot.mouseClick(button, QtCore.Qt.LeftButton)
        captured = capsys.readouterr()
        assert captured.out == f'{button.objectName()}\n'


def test_multiplet(qtbot, capsys):
    bg = MultipletButtonGroup()
    bg.buttongroup.buttonClicked.connect(printslot)
    bg.show()
    qtbot.addWidget(bg)
    for button in [bg.AB_button, bg.AB2_button, bg.ABX_button,
                   bg.ABX3_button, bg.AAXX_button,
                   bg.firstorder_button, bg.AABB_button]:
        qtbot.mouseClick(button, QtCore.Qt.LeftButton)
        captured = capsys.readouterr()
        assert captured.out == f'{button.objectName()}\n'

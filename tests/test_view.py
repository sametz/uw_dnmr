from PySide2.QtWidgets import QRadioButton

from qt_nmr.view.mainwindow import MainWindow


def test_calctype_not_impemented(qtbot, caplog):
    view = MainWindow(controller=None)
    qtbot.addWidget(view)
    testbutton = QRadioButton()
    testbutton.setObjectName('custom')
    buttongroup = view._ui.calctype.buttongroup
    buttongroup.addButton(testbutton)
    assert testbutton in buttongroup.buttons()
    testbutton.animateClick(msec=0)
    qtbot.wait(100)
    assert caplog.records[-1].levelname == 'ERROR'
    assert 'button name mismatch' in caplog.text

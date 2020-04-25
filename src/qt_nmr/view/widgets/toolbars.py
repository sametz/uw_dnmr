import logging

from PySide2.QtCore import Qt
from PySide2.QtCore import Slot as pyqtSlot
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import (QWidget, QHBoxLayout, QStackedWidget, QSpinBox,
                               QPushButton, QDialog, QGridLayout, QLabel,
                               QVBoxLayout, QSizePolicy)
from qt_nmr.view.widgets.entry import (EntryWidget, V_EntryWidget,
                                       J_EntryWidget, Color)

logger = logging.getLogger(__name__)

MINIMUM = QSizePolicy.Minimum
MAXIMUM = QSizePolicy.Maximum


class MultipletBar(QWidget):
    def __init__(self, mainwindow, model, params, *args, **kwargs):
        super(MultipletBar, self).__init__(*args, **kwargs)
        self.mainwindow = mainwindow
        self.model = model
        self.data = params
        logger.debug(f'toolbar model {self.model} has params {self.data}')

        layout = QHBoxLayout()
        self.setLayout(layout)
        self._set_name()
        self._add_widgets()

    def _set_name(self):
        self.setObjectName(f'multiplet_{self.model}_toolbar')

    def _add_widgets(self):
        self.widgets = [EntryWidget(key, val) for key, val in self.data.items()]
        for widget in self.widgets:
            self.layout().addWidget(widget, 0)
            widget.value_changed_signal.connect(self.on_value_changed)
        self.layout().addWidget(QWidget(), 1)

    @pyqtSlot(tuple)
    def on_value_changed(self, data):
        name, value = data
        logger.debug(f'change request: name {name}, value {value}')
        logger.debug(f'before change: toolbar data {self.data}')
        logger.debug(f'before change: mainwindow state {self.mainwindow.view_state}')
        self.data[name] = value
        # self._set_data()
        # self._set_state()
        logger.debug(f'after change: toolbar data {self.data}')
        logger.debug(f'after change: mainwindow state {self.mainwindow.view_state}')
        self.request_update()

    def request_update(self):
        self.mainwindow.request_update('multiplet', self.model)

    # @pyqtSlot(dict)
    # def update(self):
    #     pass


class FirstOrderBar(MultipletBar):
    def __init__(self, *args, **kwargs):
        super(FirstOrderBar, self).__init__(*args, **kwargs)

    def _add_widgets(self):
        widgets = []
        for key, val in self.data.items():
            if '#' in key:
                widgets.append(EntryWidget(key, val, entry=QSpinBox))
            else:
                widgets.append(EntryWidget(key, val))
        for widget in widgets:
            self.layout().addWidget(widget)
            widget.value_changed_signal.connect(self.on_value_changed)


class SecondOrderBar(QWidget):
    def __init__(self, mainwindow, model, params, *args, **kwargs):
        super(SecondOrderBar, self).__init__(*args, **kwargs)
        self.mainwindow = mainwindow
        self.model = model
        self.data = params  # necessary?
        logger.debug(f'toolbar model {self.model} has params {self.data}')
        self.v, self.j = self.data
        self.n = len(self.v)
        assert self.n == int(self.model)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self._set_name()
        self._add_nspin_widgets()
        self._add_popup()

    def _set_name(self):
        self.setObjectName('nuclei_bar' + str(self.model))

    # def _add_widgets(self):
    #     pass  # must initialize widgets after super init

    def _add_nspin_widgets(self):
        self._add_frequency_widgets()
        self._add_peakwidth_widget()
        self._add_J_button()
        self.layout().addWidget(QWidget(), 1)  # spacer

    def _add_frequency_widgets(self):
        self.v_widgets = []
        for i in range(self.n):
            name = 'V' + str(i + 1)
            value = self.v[i]
            widget = V_EntryWidget(name=name,
                                   value=value,
                                   index=i,
                                   v_array=self.v)  # TODO remove redundancy
            # widgets.append(widget))
            widget.value_changed_signal.connect(self.on_v_toolbar_change)
            self.layout().addWidget(widget, 0)
            self.v_widgets.append(widget)

    def _add_peakwidth_widget(self):
        pass

    def _add_J_button(self):
        self.j_button = QPushButton('Enter Js')
        self.layout().addWidget(self.j_button, 0)
        self.j_button.setSizePolicy(MAXIMUM, MAXIMUM)
        self.j_button.clicked.connect(self.on_jbutton_clicked)

    def _add_popup(self):
        self.popup = J_Popup(self)

    @pyqtSlot()
    def on_jbutton_clicked(self):
        logger.debug('j button clicked')
        self.popup.show()

    @pyqtSlot(tuple)
    def on_v_toolbar_change(self, data):
        index, value = data
        logger.debug(f'on_v_toolbar_change received {index, value}')
        self.v[index] = value  # TODO: remove redundancy with on_v_popup_change
        logger.debug(f'self.v is now {self.v}')
        self.popup.reset()  # TODO: make sure popup v update doesn't trigger multiple calls
        self.request_update()

    @pyqtSlot(tuple)
    def on_v_popup_change(self, data):
        index, value = data
        logger.debug(f'index {index} {type(index)}')
        logger.debug(f'value {value} {type(value)}')
        # self.v[index] = value
        toolbar_widget = self.v_widgets[index]
        toolbar_widget.entry.setValue(value)

    @pyqtSlot(tuple)
    def on_j_change(self, data):
        coords, value = data
        i, j = coords
        logger.debug('j {coord} changed to {value}')
        self.j[i, j] = value
        self.j[j, i] = value
        self.request_update()

    def request_update(self):
        self.mainwindow.request_update('nspin', self.n)

    # def reset(self):
    #     for i, widget in enumerate(self.v_widgets):
    #         self.v[i] = widget.value()
    #     self.request_update()


class J_Popup(QDialog):

    def __init__(self, caller, parent=None):
        super(J_Popup, self).__init__(parent)
        self.caller = caller
        self.setObjectName('j_popup' + str(caller.n))
        self.setWindowTitle('Spin ' + str(caller.n))
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('darkGray'))
        self.setPalette(palette)
        layout = QGridLayout()
        self.setLayout(layout)
        self.layout().setSpacing(3)
        logger.debug(f'J_Popup construction with {caller.n, caller.v}')
        # Set dialog layout
        layout.addWidget(self.grey())
        self.v_widgets = []
        self.j_widgets = {}
        fixed = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        for col in range(1, caller.n):
            label = QLabel(f'V{col}')
            label.setAlignment(Qt.AlignHCenter)
            label.setSizePolicy(MINIMUM, MAXIMUM)
            labelbox = self.add_background(label)
            labelbox.setSizePolicy(MINIMUM, MAXIMUM)
            layout.addWidget(labelbox, 0, col)
        for row in range(1, caller.n + 1):
            entry = V_EntryWidget(name=f'V{row}',
                                  value=caller.v[row - 1],
                                  index=row - 1,
                                  v_array=caller.v  # TODO remove redundancy
                                  )
            entry.setSizePolicy(fixed)
            self.v_widgets.append(entry)
            entry.value_changed_signal.connect(caller.on_v_popup_change)
            entrybox = self.add_background(entry)
            entrybox.setSizePolicy(fixed)
            layout.addWidget(entrybox, row, 0)
        for col in range(1, caller.n):
            self.j_widgets[col - 1] = {}
            for row in range(1, caller.n + 1):
                if col < row:
                    j_entry = J_EntryWidget(name=f'J{col}{row}',
                                            value=caller.j[col - 1, row - 1],
                                            coords=(col - 1, row - 1),
                                            j_matrix=caller.j
                                            )
                    self.j_widgets[col - 1][row - 1] = j_entry
                    j_entry.value_changed_signal.connect(caller.on_j_change)
                    j_entry.setSizePolicy(fixed)
                    j_entrybox = self.add_background(j_entry)
                    j_entrybox.setSizePolicy(fixed)
                    layout.addWidget(j_entrybox, row, col)
                else:
                    layout.addWidget(self.grey(), row, col)

    def reset(self):
        logger.debug(f'j dump for spin {self.caller.n}:')
        logger.debug(f'{self.j_widgets}')
        for i, widget in enumerate(self.v_widgets):
            widget.entry.setValue(self.caller.v[i])
        for i in range(0, self.caller.n):
            for j in range(1, self.caller.n):
                if i < j:
                    logger.debug(f'i {i} j {j}')
                    logger.debug(f'matrix {self.j_widgets}')
                    logger.debug(f'found j_widgets[i][j]')
                    self.j_widgets[i][j].entry.setValue(self.caller.j[i, j])

    @staticmethod
    def grey():
        return Color('lightGray')

    @staticmethod
    def add_background(widget, color='lightGray'):
        backing = Color(color)
        layout = QVBoxLayout()
        layout.addWidget(widget)
        backing.setLayout(layout)
        return backing


class DNMR_Bar(MultipletBar):
    def __init__(self, *args, **kwargs):
        """Currently DNMR_Bar is similar enough to MultipletBar that it can
        be a subclass.
        """
        super(DNMR_Bar, self).__init__(*args, **kwargs)

    def _set_name(self):
        self.setObjectName(f'{self.model}')

    def request_update(self):
        self.mainwindow.request_update('dnmr', self.model)


def toolbar_stack(mainwindow, settings):
    stack_toolbars = QStackedWidget()
    stack_toolbars.setObjectName('toolbar_stack')

    for model, params in settings['multiplet'].items():
        if model == '1stOrd':
            toolbar = FirstOrderBar(mainwindow, model, params)
        else:
            toolbar = MultipletBar(mainwindow, model, params)
        # toolbar.setObjectName(f'multiplet_{model_name}_toolbar')
        stack_toolbars.addWidget(toolbar)
        mainwindow.toolbars[f'multiplet_{model}'] = toolbar

    for spins, params in settings['nspin'].items():
        # model = str(spins)  # need str so BaseToolbar name inits
        toolbar = SecondOrderBar(mainwindow, spins, params)
        stack_toolbars.addWidget(toolbar)
        mainwindow.toolbars[toolbar.objectName()] = toolbar

    for model, params in settings['dnmr'].items():
        toolbar = DNMR_Bar(mainwindow, model, params)
        stack_toolbars.addWidget(toolbar)
        mainwindow.toolbars[toolbar.objectName()] = toolbar
    stack_toolbars.setCurrentWidget(mainwindow.toolbars['multiplet_AB'])
    return stack_toolbars

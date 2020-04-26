from pyqtgraph import PlotWidget, setConfigOption
from PySide2.QtWidgets import (QHBoxLayout, QStackedWidget,
                               QVBoxLayout, QWidget)

from qt_nmr.view.widgets.toolbars import toolbar_stack
from qt_nmr.view.widgets.buttons import (
    CalcTypeButtonGroup, ABC_ButtonGroup, MultipletButtonGroup,
    DNMR_ButtonGroup)


class UiMainWindow:
    def setupUi(self, main_window):
        main_window.setObjectName('main_window')
        main_window.setWindowTitle('qt_mvc Demo')
        main_window.resize(800, 600)

        # pyqtgraph configuration
        setConfigOption('background', 'w')
        setConfigOption('foreground', 'k')

        # Divide window into left (toolbar) and right(main) vertical layouts
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName('centralwidget')
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setObjectName('centrallayout')
        self.left_bar_layout = QVBoxLayout()
        self.left_bar_layout.setObjectName('left_bar_layout')
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName('main_layout')
        self.central_layout.addLayout(self.left_bar_layout, 0)
        self.central_layout.addLayout(self.main_layout, 1)

        # Populate left toolbar
        self.calctype = CalcTypeButtonGroup('Calc Type')
        self.calctype.setObjectName('calctype_menu')
        self.stack_model_selections = QStackedWidget()
        self.stack_model_selections.setObjectName('model_selection_stack')
        self.multiplet_menu = MultipletButtonGroup('Multiplet')
        self.multiplet_menu.setObjectName('multiplet_menu')
        self.abc_menu = ABC_ButtonGroup('Number of Spins')
        self.abc_menu.setObjectName('abc_menu')
        self.dnmr_menu = DNMR_ButtonGroup('DNMR')
        self.dnmr_menu.setObjectName('dnmr_menu')
        for menu in [self.multiplet_menu, self.abc_menu, self.dnmr_menu]:
            self.stack_model_selections.addWidget(menu)
        self.stack_model_selections.setCurrentWidget(self.multiplet_menu)
        self.left_bar_layout.addWidget(self.calctype, 0)
        self.left_bar_layout.addWidget(self.stack_model_selections, 0)
        self.left_bar_layout.addWidget(QWidget(), 1)

        # Add toolbars and plot area to main layout
        self.toolbars = toolbar_stack(main_window, main_window.view_state)
        self.plot = PlotWidget()
        self.plot.getViewBox().invertX(True)  # Reverse x axis "NMR style"
        self.main_layout.addWidget(self.toolbars, 0)
        self.main_layout.addWidget(self.plot, 1)

        main_window.setCentralWidget(self.central_widget)

from PySide2.QtWidgets import (QGroupBox, QRadioButton, QVBoxLayout,
                               QButtonGroup, QSizePolicy)


# MAXIMUM = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
FIXED = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


class CalcTypeButtonGroup(QGroupBox):
    """
    A widget of radio buttons that will determine which QStackedWidget is
    displayed.
    """

    # It seems that in order for the buttonClicked signal to work,
    # self.ButtonGroup and not ButtonGroup is necessary. Does not work
    # with out 'self.' prefix!!!
    def __init__(self, *args, **kwargs):
        super(CalcTypeButtonGroup, self).__init__(*args, **kwargs)
        self.multiplet_button = QRadioButton('Multiplet')
        self.multiplet_button.setObjectName('multiplet_button')
        self.abc_button = QRadioButton('ABC...')
        self.abc_button.setObjectName('abc_button')
        self.dnmr_button = QRadioButton('DNMR')
        self.dnmr_button.setObjectName('dnmr_button')

        layout = QVBoxLayout()
        self.buttongroup = QButtonGroup()
        for button in [self.multiplet_button, self.abc_button, self.dnmr_button]:
            layout.addWidget(button)
            self.buttongroup.addButton(button)
        self.setLayout(layout)

        self.multiplet_button.setChecked(True)


class MultipletButtonGroup(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(MultipletButtonGroup, self).__init__(*args, **kwargs)
        self.AB_button = QRadioButton('AB')
        self.AB_button.setObjectName('AB_button')
        self.AB2_button = QRadioButton('AB2')
        self.AB2_button.setObjectName('AB2_button')
        self.ABX_button = QRadioButton('ABX')
        self.ABX_button.setObjectName('ABX_button')
        self.ABX3_button = QRadioButton('ABX3')
        self.ABX3_button.setObjectName('ABX3_button')
        self.AAXX_button = QRadioButton("AA'XX'")
        self.AAXX_button.setObjectName('AAXX_button')
        self.firstorder_button = QRadioButton('1stOrd')
        self.firstorder_button.setObjectName('1stOrd_button')
        self.AABB_button = QRadioButton("AA'BB'")
        self.AABB_button.setObjectName('AABB_button')

        layout = QVBoxLayout()
        self.buttongroup = QButtonGroup()
        for button in [self.AB_button, self.AB2_button, self.ABX_button,
                       self.ABX3_button, self.AAXX_button,
                       self.firstorder_button, self.AABB_button]:
            layout.addWidget(button)
            self.buttongroup.addButton(button)
        self.setLayout(layout)
        self.setSizePolicy(FIXED)
        self.AB_button.setChecked(True)


class ABC_ButtonGroup(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(ABC_ButtonGroup, self).__init__(*args, **kwargs)
        self.buttons = {}
        layout = QVBoxLayout()
        self.buttongroup = QButtonGroup()
        for i in range(2, 9):  # 2 to 8 nuclei
            button = QRadioButton(str(i))
            self.buttons[str(i)] = button
            button.setObjectName('nuclei_button' + str(i))
            layout.addWidget(button)
            self.buttongroup.addButton(button)
        self.setLayout(layout)

        self.buttons['2'].setChecked(True)


class DNMR_ButtonGroup(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(DNMR_ButtonGroup, self).__init__(*args, **kwargs)
        self.dnmr_twospin_button = QRadioButton('2-spin')
        self.dnmr_twospin_button.setObjectName('dnmr_twospin_button')
        self.dnmr_ab_button = QRadioButton('AB coupled')
        self.dnmr_ab_button.setObjectName('dnmr_ab_button')

        layout = QVBoxLayout()
        self.buttongroup = QButtonGroup()
        for button in [self.dnmr_twospin_button, self.dnmr_ab_button]:
            layout.addWidget(button)
            self.buttongroup.addButton(button)
        self.setLayout(layout)
        self.dnmr_twospin_button.setChecked(True)

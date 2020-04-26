import logging

from PySide2.QtCore import QObject

from qt_nmr.controller.adapter import view_to_model
from qt_nmr.view.mainwindow import MainWindow

logger = logging.getLogger(__name__)


class Controller(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model
        self.view = MainWindow(self)
        self.view.on_toolbar_change()  # trigger an initial plot

    def update_model(self, calctype, model_name, params):
        logger.debug(f' controller received {calctype} {model_name} {params}')
        if calctype == 'nspin':
            args = params  # no conversion required
        else:
            args = view_to_model(model_name, params)
        logger.debug(f' controller will send to model {args}')
        x, y = self._model.update(calctype, model_name, *args)
        logger.debug(f'sending to plot {x[:10], y[:10]}')
        self.view.plot(x, y)

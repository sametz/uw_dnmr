"""The executable file for the uw_dnmr app"""
import sys

from PySide2.QtWidgets import QApplication

from uw_dnmr.controller.controller import Controller
from uw_dnmr.model.model import Model


# noinspection PyArgumentList
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = Controller(self.model)
        self.main_view = self.main_controller.view
        self.main_view.show()


def main():
    import logging
    logging.basicConfig(level=logging.INFO,
                        format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    numba_logger = logging.getLogger('numba')
    numba_logger.setLevel(logging.CRITICAL)
    app = App(sys.argv)
    sys.exit(app.exec_())

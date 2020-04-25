import logging

from qt_nmr.view.settings import view_defaults
from qt_nmr.view.widgets.toolbars import DNMR_Bar


class FakeMainWindow:
    def __init__(self):
        self.view_state = view_defaults

    def request_update(self, *args, **kwargs):
        pass


def test_dnmr_bar_instantiates(caplog, qtbot):
    with caplog.at_level(logging.DEBUG):
        pass
    mainwindow = FakeMainWindow()
    qtbot.addWidget(mainwindow)
    model = 'dnmr_two_singlets'
    params = view_defaults['dnmr']['dnmr_two_singlets']
    bar = DNMR_Bar(mainwindow, model, params)
    qtbot.addWidget(bar)
    bar.request_update()
    assert 1 == 1

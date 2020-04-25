import logging
# import time

import numpy as np
from PySide2 import QtCore
# import pytest

from qt_nmr.controller.controller import Controller
from qt_nmr.model.model import Model
# from qt_nmr.view.widgets.entry import V_EntryWidget
from tests.accepted_data.utils import load_lineshape

# There's a lot of repetition in the test code, but trying to reduce repetition
# by e.g. using pytest fixtures runs into problems with trying to create
# more than one Singleton.

# class App(QApplication):
#     def __init__(self, sys_argv):
#         super(App, self).__init__(sys_argv)
#         self.model = Model()
#         self.main_controller = Controller(self.model)
#         self.main_view = self.main_controller.view
#         self.main_view.show()
#
#
# @pytest.fixture(scope='class')
# def app():
#     model = Model()
#     controller = Controller(model)
#     view = controller.view
#     yield model, controller, view
#
#
# @pytest.mark.usefixtures("app")
# class TestFixture:
#     def test_fixture(self):
#         print(model, controller, view)
#         assert 1 == 1


def beep():
    import os
    os.system('afplay /System/Library/Sounds/Bottle.aiff')


def ding():
    import os
    os.system('afplay /System/Library/Sounds/Glass.aiff')


# noinspection PyProtectedMember
def view_buttons(view):
    buttons = {
        'calctype': {
            'multiplet': view._ui.calctype.multiplet_button,
            'abc': view._ui.calctype.abc_button,
            'dnmr': view._ui.calctype.dnmr_button
        },
        'multiplet': {
            'AB': view._ui.multiplet_menu.AB_button,
            'AB2': view._ui.multiplet_menu.AB2_button,
            'ABX': view._ui.multiplet_menu.ABX_button,
            'ABX3': view._ui.multiplet_menu.ABX3_button,
            'AAXX': view._ui.multiplet_menu.AAXX_button,
            '1stOrd': view._ui.multiplet_menu.firstorder_button,
            'AABB': view._ui.multiplet_menu.AABB_button
        },
        'nspin': view._ui.abc_menu.buttons,
        'dnmr': {
            'dnmr_two_singlets': view._ui.dnmr_menu.dnmr_twospin_button,
            'dnmr_ab': view._ui.dnmr_menu.dnmr_ab_button
        }
    }
    return buttons


# noinspection PyProtectedMember
def view_lineshape(view):
    return view._ui.plot.listDataItems()[0].getData()


class TestApp:
    @staticmethod
    def mvc():
        model = Model()
        controller = Controller(model)
        view = controller.view
        view.show()
        return model, view, controller

    def test_instantiation(self, qtbot):
        # model = Model()
        # controller = Controller(model)
        # view = controller.view
        model, view, controller = self.mvc()
        # view.show()
        qtbot.addWidget(view)
        dataitem = view._ui.plot.listDataItems()[0]
        view_data = dataitem.getData()
        expected_data = load_lineshape('multiplet_AB.json')
        np.testing.assert_array_almost_equal(view_data, expected_data)

    def test_nspins(self, qtbot):
        model, view, controller = self.mvc()
        # view.show()
        qtbot.addWidget(view)
        abc_button = view._ui.calctype.abc_button
        assert abc_button
        qtbot.mouseClick(abc_button, QtCore.Qt.LeftButton)
        dataitem = view._ui.plot.listDataItems()[0]
        view_data = dataitem.getData()
        expected_data = load_lineshape('nspin_2.json')
        np.testing.assert_array_almost_equal(view_data, expected_data)

    def test_stack_widget(self, qtbot):
        model, view, controller = self.mvc()
        qtbot.addWidget(view)
        buttons = view_buttons(view)
        model_selections = {
            'multiplet': view._ui.multiplet_menu,
            'abc': view._ui.abc_menu,
            'dnmr': view._ui.dnmr_menu
        }
        for calctype in ['abc', 'dnmr', 'multiplet']:
            qtbot.mouseClick(buttons['calctype'][calctype],
                             QtCore.Qt.LeftButton)
            stackedwidget = view._ui.stack_model_selections
            assert stackedwidget.currentWidget() is model_selections[calctype]

    def test_all_multiplets(self, qtbot):
        model, view, controller = self.mvc()
        qtbot.addWidget(view)
        buttons = view_buttons(view)
        buttongroup = view._ui.multiplet_menu.buttongroup

        for model, button in buttons['multiplet'].items():
            # qtbot.wait(2000)
            # time.sleep(2)
            qtbot.mouseClick(button, QtCore.Qt.LeftButton)
            assert button in buttongroup.buttons()
            qtbot.mouseClick(button, QtCore.Qt.LeftButton)
            # while buttongroup.checkedButton() is not button:
            #     beep()
            #     qtbot.wait(1000)
            #     time.sleep(1)
            # ding()
            filename = f'multiplet_{model}.json'
            dataitem = view._ui.plot.listDataItems()[0]
            view_data = dataitem.getData()
            expected_data = load_lineshape(filename)
            np.testing.assert_array_almost_equal(view_data, expected_data)

    def test_all_dnmr(self, qtbot):
        model, view, controller = self.mvc()
        qtbot.addWidget(view)
        buttons = view_buttons(view)
        qtbot.mouseClick(buttons['calctype']['dnmr'], QtCore.Qt.LeftButton)
        for model, button in buttons['dnmr'].items():
            # qtbot.wait(1000)
            # time.sleep(1)
            qtbot.mouseClick(button, QtCore.Qt.LeftButton)
            # print('\a')
            filename = f'dnmr_{model}.json'
            # dataitem = view._ui.plot.listDataItems()[0]
            # view_data = dataitem.getData()
            view_data = view_lineshape(view)
            expected_data = load_lineshape(filename)
            np.testing.assert_array_almost_equal(view_data, expected_data)

    def test_dnmr_entries(self, qtbot):
        model, view, controller = self.mvc()
        qtbot.addWidget(view)
        buttons = view_buttons(view)
        qtbot.mouseClick(buttons['calctype']['dnmr'], QtCore.Qt.LeftButton)
        va_entry = view._ui.toolbars.currentWidget().widgets[0]
        assert va_entry.entry.value() == 165.0
        vb_entry = view._ui.toolbars.currentWidget().widgets[1]
        assert vb_entry.entry.value() == 135.0
        va_entry.entry.setValue(135.0)
        # qtbot.wait(100)
        assert not np.allclose(
            view_lineshape(view),
            load_lineshape(f'dnmr_dnmr_two_singlets.json'))
        vb_entry.entry.setValue(165.0)
        assert np.allclose(
            view_lineshape(view),
            load_lineshape(f'dnmr_dnmr_two_singlets.json'))

    def test_all_nspin(self, qtbot, caplog):
        # currently not working. For some reason, qtbot clicking the nspin
        # buttons isn't working.
        caplog.set_level(logging.INFO)
        model, view, controller = self.mvc()
        qtbot.addWidget(view)
        buttons = view_buttons(view)
        buttongroup = view._ui.abc_menu.buttongroup
        qtbot.mouseClick(buttons['calctype']['abc'], QtCore.Qt.LeftButton)
        np.testing.assert_array_almost_equal(view_lineshape(view),
                                             load_lineshape('nspin_2.json'))
        for number, button in buttons['nspin'].items():
            print(number, button)
            if number == '2':
                continue
            assert button in buttongroup.buttons()
            assert view._ui.abc_menu.buttons[str(number)] is button
            assert button.objectName() == f'nuclei_button{str(number)}'
            button.animateClick(msec=0)  # workaround for qtbot.click failure

            # following didn't work: segfaults
            # with qtbot.waitSignal(view._ui.plot.listDataItems()[0].sigPlotChanged, timeout=5000):
            #     button.animateClick(msec=0)

            # in lieu of working update plot signal, add a suitable delay:
            qtbot.wait(100)
            filename = f'nspin_{number}.json'
            np.testing.assert_array_almost_equal(view_lineshape(view),
                                                 load_lineshape(filename))
            # qtbot.mouseClick(button, QtCore.Qt.LeftButton)
            # while buttongroup.checkedButton() is not button:
            #     beep()
            #     qtbot.wait(1000)
            #     time.sleep(1)
            # ding()
        # n3button = buttons['nspin']['3']
        # n3button = view._ui.abc_menu.buttons['3']
        # assert n3button.objectName() == 'nuclei_button3'
        # qtbot.mouseClick(n3button, QtCore.Qt.LeftButton)
        # beep()
        # qtbot.wait(1000)
        # time.sleep(1)
        # current_nbutton = view._ui.stack_model_selections.currentWidget().buttongroup.checkedButton()
        # print('current nbutton: ', current_nbutton.objectName())
        #
        # print('current toolbar: ', view._ui.toolbars.currentWidget().objectName())
        # np.testing.assert_array_almost_equal(view_lineshape(view),
        #                                      load_lineshape('nspin_3.json'))

    def test_nspin_entries(self, qtbot):
        # Started to write test, but nspin button clicks not working
        # spun off as test_all_nspin to find problem.
        # Leaving an outline for the test to be written once this is fixed

        # GIVEN a fresh instance of the app
        model, view, controller = self.mvc()
        qtbot.addWidget(view)

        # WHEN the 'abc...' models are selected
        buttons = view_buttons(view)
        qtbot.mouseClick(buttons['calctype']['abc'], QtCore.Qt.LeftButton)

        # AND 3 nuclei is selected
        n3button = buttons['nspin']['3']
        n3button.animateClick(msec=0)  # workaround for qtbot.click failure
        qtbot.wait(100)
        # THEN the plot data matches that expected for the 3-spin simulation
        assert np.allclose(
            view_lineshape(view),
            load_lineshape(f'nspin_3.json'))

        # WHEN the V1 toolbar entry is changed to 140 Hz
        current_toolbar = view._ui.toolbars.currentWidget()
        # assert current_toolbar.objectName() == 'nuclei_bar3'
        # assert len(current_toolbar.v_widgets) == 3
        # assert isinstance(current_toolbar.v_widgets[0], V_EntryWidget)
        v1_widget = view._ui.toolbars.currentWidget().v_widgets[0]
        assert v1_widget.objectName() == 'V1'
        v1_widget.entry.setValue(140.0)
        qtbot.wait(100)
        # THEN the plot data no longer matches expected
        try:
            assert not np.allclose(
                view_lineshape(view),
                load_lineshape(f'nspin_3.json'))
        except ValueError as e:
            print(e)  # if arrays can't be compared, they're different

        # BUT WHEN the J-value dialog is selected
        j_button = current_toolbar.j_button
        qtbot.mouseClick(j_button, QtCore.Qt.LeftButton)
        qtbot.wait(100)
        dialog = current_toolbar.popup

        # AND the dialog is used to change:
        # - V2 to 190 Hz,
        v2_widget = dialog.v_widgets[1]
        assert v2_widget.objectName() == 'V2'
        v2_widget.entry.setValue(190.0)

        # - V3 to 115 Hz,
        v2_widget = dialog.v_widgets[2]
        assert v2_widget.objectName() == 'V3'
        v2_widget.entry.setValue(115.0)

        # - J12 to 3 Hz,
        J12_widget = dialog.j_widgets[0][1]  # dict by matrix index, not name
        assert J12_widget.objectName() == 'J12'
        J12_widget.entry.setValue(3.0)

        # - J13 to 6 Hz,
        J13_widget = dialog.j_widgets[0][2]
        assert J13_widget.objectName() == 'J13'
        J13_widget.entry.setValue(6.0)

        # - J23 to 12 Hz
        J23_widget = dialog.j_widgets[1][2]
        assert J23_widget.objectName() == 'J23'
        J23_widget.entry.setValue(12.0)
        # THEN the plot data once again matches expected
        assert np.allclose(
            view_lineshape(view),
            load_lineshape(f'nspin_3.json'))

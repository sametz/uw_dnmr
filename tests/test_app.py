import numpy as np
import pytest

from qt_nmr.app import App
from tests.accepted_data.utils import load_lineshape


# @pytest.mark.skip()
def test_app():
    app = App([])
    abc_button = app.main_view._ui.calctype.abc_button
    abc_button.animateClick(msec=0)
    dataitem = app.main_view._ui.plot.listDataItems()[0]
    view_data = dataitem.getData()
    expected_data = load_lineshape('nspin_2.json')
    np.testing.assert_array_almost_equal(view_data, expected_data)

import numpy as np
import pytest

from tests.accepted_data.utils import load_lineshape
from qt_nmr.controller.adapter import view_to_model
from qt_nmr.model.model import Model
from qt_nmr.view.settings import view_defaults


def model_args(calctype, model, params):
    if calctype == 'nspin':
        return params
    else:
        return view_to_model(model, params)


@pytest.fixture()
def test_model():
    model = Model()
    return model


class TestModel:
    def test_multiplet(self, test_model):
        args = model_args('multiplet', 'AB', view_defaults['multiplet']['AB'])
        # print(args)
        x, y = test_model.update('multiplet', 'AB', *args)
        test_data = [list(x), list(y)]
        expected_data = load_lineshape('multiplet_AB.json')
        print(test_data)
        print(expected_data)
        np.testing.assert_array_almost_equal(test_data, expected_data)

    def test_all(self, test_model):
        for calctype, model_dict in view_defaults.items():
            for model, params in model_dict.items():
                args = model_args(calctype, model, params)
                x, y = test_model.update(calctype, model, *args)
                test_data = [list(x), list(y)]
                expected_datafile = f'{calctype}_{str(model)}.json'
                expected_data = load_lineshape(expected_datafile)
                np.testing.assert_array_almost_equal(test_data, expected_data)

    def test_bad_modelname(self, test_model):
        args = model_args('multiplet', 'AB', view_defaults['multiplet']['AB'])
        response = test_model.update('maltypet', 'AB', *args)
        assert response == 'maltypet'

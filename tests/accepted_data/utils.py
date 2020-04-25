"""Generate reference lineshapes for tests.

The script trusts that the Model/Controller functions it uses at the time it's
run are correct, and that view.settings doesn't change.
TODO: write unit tests to verify.
"""
import json
import os
from pathlib import Path

from qt_nmr.controller.adapter import view_to_model
from qt_nmr.model.model import Model
from qt_nmr.view.settings import view_defaults

_model = Model()


def load_lineshape(filename):
    data_dir = os.path.dirname(__file__)
    file_path = Path(data_dir, filename)
    with file_path.open('r') as f:
        data = json.load(f)
        return data


def save_lineshapes():
    for calctype, model_dict in view_defaults.items():
        for model, params in model_dict.items():
            process_model(calctype, model, params)


def process_model(calctype, model, params):
    data = calc_lineshape(calctype, model, params)
    filename = f'{calctype}_{str(model)}.json'
    save_json(data, filename)


def calc_lineshape(calctype, model, params):
    if calctype == 'nspin':
        model_args = params
    else:
        model_args = view_to_model(model, params)
    x, y = _model.update(calctype, model, *model_args)
    data = (list(x), list(y))
    return data


def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    save_lineshapes()

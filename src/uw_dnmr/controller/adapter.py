"""Converts parameters sent by the view to parameters that can be used by the
Model.
"""
import logging

logger = logging.getLogger(__name__)


def parse_posargs(params):
    """
    Converts params to a list of numeric arguments for the model_name, IF the
    following conditions are met:
    * dicts are the new ordered-by-default
    * arguments are listed in settings.py dicts in same order as position of
      arguments in the model_name's corresponding function

    :param params: {str: float...}
        for {name of variable: value...}
    :return: [float...]
        a list of numerical positional arguments
    """
    return [val for val in params.values()]


def parse_abx(params):
    """Matches ABX behavior to WINDNMR behavior.

    In WINDNMR, vx was hard coded to equal vb + 100.
    """
    logger.debug(f'params before abx conversion: {params}')
    # new dict's order is important therefore converted item-wise
    new_params = {
        'Jab': params['Jab'],
        # For ud_dnmr output to match WINDNMR output, Js must be transposed
        'Jax': params['Jbx'],
        'Jbx': params['Jax'],
        'Vab': params['Vab'],
        'Vcentr': params['Vcentr']
        # # new parameter added: WINDNMR assumes vx is vb + 100
        # 'vx': Vcentr + (Vab / 2) + 100
    }
    # params['Jax'], params['Jbx'] = params['Jbx'], params['Jax']
    Vcentr = new_params['Vcentr']
    Vab = new_params['Vab']
    # Reich's ABX: vx initialized as vb + 100
    new_params['vx'] = Vcentr + (Vab / 2) + 100
    logger.debug(f'params after conversion: {new_params}')
    return parse_posargs(new_params)


def parse_first_order(params):
    logger.debug(f'parse_first_order received {params}')
    _Jax = params['JAX']
    _a = params['#A']
    _Jbx = params['JBX']
    _b = params['#B']
    _Jcx = params['JCX']
    _c = params['#C']
    _Jdx = params['JDX']
    _d = params['#D']
    _Vcentr = params['Vcentr']
    singlet = (_Vcentr, 1)  # using default intensity of 1
    allcouplings = [(_Jax, _a), (_Jbx, _b), (_Jcx, _c), (_Jdx, _d)]
    couplings = [coupling for coupling in allcouplings if coupling[1] != 0]
    return singlet, couplings


def parse_dnmr_two_singlets(params):
    param_copy = params.copy()
    param_copy['%a'] = params['%a'] / 100
    return [val for val in param_copy.values()]


def view_to_model(model, params):
    adapters = {
        'AB': parse_posargs,
        'AB2': parse_posargs,
        'ABX': parse_abx,
        'ABX3': parse_posargs,
        'AAXX': parse_posargs,
        'AABB': parse_posargs,
        '1stOrd': parse_first_order,
        'dnmr_two_singlets': parse_dnmr_two_singlets,
        'dnmr_ab': parse_posargs
    }
    logger.debug(f'adapter received {model} {params}')
    return adapters[model](params)

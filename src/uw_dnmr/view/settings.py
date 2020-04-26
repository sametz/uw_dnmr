import numpy as np

ABdict = {'Jab': 12.0,
          'Vab': 15.0,
          'Vcentr': 150.0}

AB2dict = {'Jab': 12.0,
           'Vab': 15.0,
           'Vcentr': 150.0}

ABXdict = {'Jab': 12.0,
           'Jax': 2.0,
           'Jbx': 8.0,
           'Vab': 15.0,
           'Vcentr': 7.5}

ABX3dict = {'Jab': -12.0,
            'Jax': 7.0,
            'Jbx': 7.0,
            'Vab': 14.0,
            'Vcentr': 150}

AAXXdict = {"Jaa": 15.0,
            "Jxx": -10.0,
            "Jax": 40.0,
            "Jax_prime": 6.0,
            'Vcentr': 150}

AABBdict = {"Vab": 40,
            "Jaa": 15.0,
            "Jbb": -10.0,
            "Jab": 40.0,
            "Jab_prime": 6.0,
            'Vcentr': 150}

firstorder_dict = {
    'JAX': 7.00,
    '#A': 2,
    'JBX': 3.00,
    '#B': 1,
    'JCX': 2.00,
    '#C': 0,
    'JDX': 7.00,
    '#D': 0,
    'Vcentr': 150.00
}

dnmr_two_spins_dict = {
    'Va': 165.00,
    'Vb': 135.00,
    'ka': 1.50,
    'Wa': 0.5,
    'Wb': 0.5,
    '%a': 50
}

dnmr_ab_dict = {'Va': 165.00,
                'Vb': 135.00,
                'J': 12.00,
                'kAB': 12.00,
                'W': 0.5}


def spin2():
    v = np.array([150-7.5, 150+7.5])
    J = np.zeros((2, 2))
    J[0, 1] = 12
    J = J + J.T
    return v, J


def spin3():
    v = np.array([115, 140, 190])
    J = np.zeros((3, 3))
    J[0, 1] = 6
    J[0, 2] = 12
    J[1, 2] = 3
    J = J + J.T
    return v, J


def spin4():
    v = np.array([105, 140, 180, 205])
    J = np.zeros((4, 4))
    J[0, 1] = -12
    J[0, 2] = 6
    J[0, 3] = 8
    J[1, 2] = 3
    J[1, 3] = 3
    # J[2, 3] = 0
    J = J + J.T
    return v, J


def spin5():
    v = np.array([105, 140, 180, 205, 225])
    J = np.zeros((5, 5))
    J[0, 1] = -12
    J[0, 2] = 6
    # J[0, 3] = 0
    J[0, 4] = 2
    J[1, 2] = 3
    # J[1, 3] = 0
    J[1, 4] = 14
    J[2, 3] = 1
    # J[2, 4] = 0
    J[3, 4] = 1.5
    J = J + J.T
    return v, J


def spin6():
    v = np.array([105, 140, 180, 205, 225, 235])
    J = np.zeros((6, 6))
    J[0, 1] = -12
    J[0, 2] = 6
    # J[0, 3] = 0
    J[0, 4] = 2
    # J[0, 5] = 0
    J[1, 2] = 3
    # J[1, 3] = 0
    J[1, 4] = 14
    J[1, 5] = 6
    J[2, 3] = 1
    # J[2, 4] = 0
    J[2, 5] = 3
    J[3, 4] = 1.5
    J[3, 5] = 5
    J[4, 5] = 2
    J = J + J.T
    return v, J


def spin7():
    v = np.array([105, 140, 180, 205, 225, 235, 255])
    J = np.zeros((7, 7))
    J[0, 1] = -12
    J[0, 2] = 6
    # J[0, 3] = 0
    J[0, 4] = 2
    # J[0, 5] = 0
    # J[0, 6] = 0
    J[1, 2] = 3
    # J[1, 3] = 0
    J[1, 4] = 14
    J[1, 5] = 6
    # J[1, 6] = 0
    J[2, 3] = 1
    # J[2, 4] = 0
    J[2, 5] = 3
    # J[2, 6] = 0
    J[3, 4] = 1.5
    J[3, 5] = 5
    # J[3, 6] = 0
    J[4, 5] = 2
    # J[4, 6] = 0
    J[5, 6] = 2
    J = J + J.T
    return v, J


def spin8():
    v = np.array([85, 120, 160, 185, 205, 215, 235, 260])
    J = np.zeros((8, 8))
    J[0, 1] = -12
    J[0, 2] = 6
    J[0, 3] = 2
    # J[0, 4] = 0
    # J[0, 5] = 0
    # J[0, 6] = 0
    # J[0, 7] = 0
    # J[1, 2] = 0
    # J[1, 3] = 0
    J[1, 4] = 14
    # J[1, 5] = 0
    # J[1, 6] = 0
    J[1, 7] = 3
    # J[2, 3] = 0
    # J[2, 4] = 0
    J[2, 5] = 3
    # J[2, 6] = 0
    # J[2, 7] = 0
    # J[3, 4] = 0
    J[3, 5] = 5
    # J[3, 6] = 0
    # J[3, 7] = 0
    J[4, 5] = 2
    # J[4, 6] = 0
    # J[4, 7] = 0
    # J[5, 6] = 0
    # J[5, 7] = 0
    J[6, 7] = 12
    J = J + J.T
    return v, J


view_defaults = {
    'multiplet': {
        'AB': ABdict,
        'AB2': AB2dict,
        'ABX': ABXdict,
        'ABX3': ABX3dict,
        'AAXX': AAXXdict,
        '1stOrd': firstorder_dict,
        'AABB': AABBdict
    },
    'nspin': {
        2: spin2(),
        3: spin3(),
        4: spin4(),
        5: spin5(),
        6: spin6(),
        7: spin7(),
        8: spin8()
    },
    'dnmr': {
        'dnmr_two_singlets': dnmr_two_spins_dict,
        'dnmr_ab': dnmr_ab_dict

    }
}

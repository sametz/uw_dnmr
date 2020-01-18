"""
The controller for the UW-DNMR app.

Assumes a tkinter view.

Provides the following class:
* Controller    Class that handles data and requests to/from the model and 
                the view.
"""

import tkinter as tk

import numpy as np

from nmrsim.discrete import AB, AB2, ABX, ABX3, AABB, AAXX
from nmrsim.dnmr import dnmr_two_singlets, dnmr_AB
from nmrsim.firstorder import multiplet
from nmrsim.plt import add_lorentzians
from nmrsim.qm import qm_spinsystem

from uw_dnmr.GUI.view import View
# from uw_dnmr.model.nmrmath import (nspinspec, AB, AB2, ABX, ABX3, AABB, AAXX,
#                                      first_order)
# from uw_dnmr.model.nmrplot import tkplot, dnmrplot_2spin, dnmrplot_AB


def ABX_interface(**kwargs):
    """Matches ABX behavior to WINDNMR behavior.

    In WINDNMR, vx was hard coded to equal vb + 100.
    """
    # For ud_dnmr output to match WINDNMR output, Js must be transposed
    kwargs['Jax'], kwargs['Jbx'] = kwargs['Jbx'], kwargs['Jax']
    Vcentr = kwargs['Vcentr']
    Vab = kwargs['Vab']
    # Reich's ABX: vx initialized as vb + 100
    vx = Vcentr + (Vab / 2) + 100
    kwargs['vx'] = vx
    return kwargs


# Temporarily adding tkplot function here to restore functionality.
def tkplot(spectrum, w=0.5):
    """Generate linspaces of x and y coordinates suitable for plotting on a
    matplotlib tkinter canvas.
    :param spectrum: A list of (frequency, intensity) tuples
    :param w: peak width at half height
    :return: a tuple of x and y coordinate linspaces
    """
    spectrum.sort()
    r_limit = spectrum[-1][0] + 50
    l_limit = spectrum[0][0] - 50
    x = np.linspace(l_limit, r_limit, 2400)
    y = add_lorentzians(x, spectrum, w)
    return x, y


class Controller:
    """Instantiate uw_dnmr's view, and pass data and requests to/from
    the model and the view.
    
    The controller assumes the view offers the following methods:
    
    * initialize()--Initializes the view. Currrently, just "OKs" the View 
    to call Controller.update_view_plot after view's instantiation. 
    
    * clear()--clears the view's plot.
    
    * plot(x, y)--accept a tuple of x, y numpy arrays and plot the data.
    
    The controller provides the following methods:
    
    * update_view_plot: parse the data sent by the view; call the appropriate
    model simulation; and tell the view to plot the model's simulated
    spectral data.

    * call_nspins_model: provide an interface that allows the model to be
    called with the view's second-order data.
    """

    def __init__(self, root):
        """Instantiate the view as a child of root, and then initializes it.
        
        Argument:
            root: a tkinter.Tk() object
        """
        self.models = {'AB': AB,
                       'AB2': AB2,
                       'ABX': ABX,
                       'ABX3': ABX3,
                       'AABB': AABB,
                       'AAXX': AAXX,
                       'first_order': multiplet,
                       'nspin': self.call_nspins_model,
                       'DNMR_Two_Singlets': dnmr_two_singlets,
                       'DNMR_AB': dnmr_AB}

        self.view = View(root, self)
        self.view.pack(expand=tk.YES, fill=tk.BOTH)
        self.view.initialize()

    def update_view_plot(self, model, *args, **data):
        """
        Parse the view's request; call the appropriate model for simulated
        spectral data; and tell the view to plot the data.

        :param model: (str) The type of calculation to be performed.
        :param args: DNMR model is called with positional arguments.
        :param data: first-order and second-order simulations are called with
        keyword arguments.

        :return: None (including when model is not recognized)
        """
        multiplet_models = ['AB', 'AB2', 'ABX', 'ABX3', 'AABB', 'AAXX',
                            'first_order']

        if model in multiplet_models:
            if model == 'ABX':
                data = ABX_interface(**data)
            spectrum = self.models[model](**data)
            plotdata = tkplot(spectrum)
        elif model == 'nspin':
            spectrum, w = self.models[model](**data)
            plotdata = tkplot(spectrum, w)
        elif 'DNMR' in model:
            plotdata = self.models[model](*args)
        else:
            print('model not recognized')
            return

        self.view.clear()
        self.view.plot(*plotdata)

    @staticmethod
    def call_nspins_model(v, j, w, **kwargs):
        """Provide an interface between the controller/view data model (use
        of **kwargs) and the functions for second-order calculations (which
        use *args).

        :param v: a 1-D numpy array of frequencies
        :param j: a 2-D numpy array of coupling constants (J values)
        :param w: line width at half height

        :return: a (spectrum, linewidth) tuple, where spectrum is a list of
        (frequency, intensity) tuples
        """
        # **kwargs to catch unimplemented features
        # The difference between first- and second-order models right now
        # from the controller's perspective is just the added linewidth
        # argument. If more features are added to first- and second-order
        # models, this distinction may be lost, and all requests will have to
        #  be parsed for extra kwargs.
        if not (v.any() and j.any() and w.any()):
            print('invalid kwargs:')
            if not v.any():
                print('v missing')
            if not j.any():
                print('j missing')
            if not w.any():
                print('w missing')
        else:
            return qm_spinsystem(v, j), w


if __name__ == '__main__':
    root = tk.Tk()
    root.title('uw_dnmr')  # working title only!
    app = Controller(root)

    # workaround fix for Tk problems and mac mouse/trackpad:
    while True:
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass

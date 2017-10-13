"""Custom tkinter frames that hold multiple widgets plus capabilities to
store data and send it to a controller.

Provides the following classes:
* ToolBar: A base class for creating toolbars, intended to be subclassed and
extended.

* AB_Bar, AB2_Bar, ABX_Bar, ABX3_Bar, AAXX_Bar, AABB_Bar: hold numerical inputs
required for simulating AB, AB2, ABX, ABX3, AA'XX', and AA'BB' spin systems.

* FirstOrder_Bar: holds numerical inputs required for first-order simulation

* SecondOrderBar: holds numerical inputs, plus a button with a pop-up 2D
array for entering chemical shifts and J coupling constants, for second-order
simulations of up to 8 coupled spins.

* DNMR_TwoSingletBar: holds "custom SpinBox" numerical inputs for the
simulation of a DNMR lineshape for two uncoupled spins.

* DNMR_AB: holds "custom spinbox" numerical inputs for the simulation of a
DNMR lineshape for two coupled spins (AB quartet at the slow exchange limit).

TODO:
* Many of these classes for 'Multiplet' non-QM calculations can be reduced to
a single class, with the exact widget layouts specified by a dict argument.
* DNMR bar code can be simplified
"""

from tkinter import *

import numpy as np

from ReichDNMR.GUI.widgets import (ArrayBox, ArraySpinBox, VarBox, IntBox,
                                       VarButtonBox)
from ReichDNMR.initialize import getWINDNMRdefault


class ToolBar(Frame):
    """Extend tkinter.Frame with a dictionary, a controller reference, a model
    name, and a function to call the controller.

    Intended to be subclassed, and not instantiated itself.

    methods:
        request_plot: sends model type and data to the controller

    Attributes:
        controller: the Controller object of the Model-View-Controller
        architecture. Assumes controller has an update_view_plot method.
        model (str): the type of calculation requested (interpreted by the
        controller).
        vars (dict): holds the kwargs that the controller is called with.
        Intent is that child widgets will store and update their data to this
        dict.
    """

    def __init__(self, parent=None, controller=None, **options):
        """Initialize the ToolBar object with a reference to a controller.

        Keyword arguments:
        :param parent: the parent tkinter object
        :param controller: the Controller object of the MVC application
        :param options: standard optional kwargs for a tkinter Frame
        """
        Frame.__init__(self, parent, **options)
        self.controller = controller
        self.model = 'model'  # must be overwritten by subclasses
        self.vars = {}

    def request_plot(self):
        """Send request to controller to recalculate and refresh the view's
        plot.
        """
        self.controller.update_view_plot(self.model, **self.vars)


class AB_Bar(ToolBar):
    """A subclass of ToolBar designed for use with AB simulations.

    Extends ToolBar with AB quartet inputs, and overwrites .model as 'AB'.
    """
    def __init__(self, parent=None, **options):
        ToolBar.__init__(self, parent, **options)
        self.model = 'AB'
        self.vars = {'Jab': 12.00,
                     'Vab': 15.00,
                     'Vcentr': 150.00}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['Jab', 'Vab', 'Vcentr']:
            widget = VarBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)


class AB2_Bar(ToolBar):
    """A subclass of ToolBar designed for use with AB2 simulations.

    Extends ToolBar with necessary AB2 inputs, and overwrites .model as 'AB2'.
    """
    def __init__(self, parent=None, **options):
        ToolBar.__init__(self, parent, **options)
        self.model = 'AB2'
        self.vars = {'Jab': 12.00,
                     'Vab': 15.00,
                     'Vcentr': 150.00}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['Jab', 'Vab', 'Vcentr']:
            widget = VarBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)


class ABX_Bar(ToolBar):
    """A subclass of ToolBar designed for use with ABX simulations.

    Extends ToolBar with necessary ABX inputs, and overwrites .model as 'ABX'.
    """

    def __init__(self, parent=None, **options):
        ToolBar.__init__(self, parent, **options)
        self.model = 'ABX'
        self.vars = {'Jab': 12.00,
                     'Jax': 2.00,
                     'Jbx': 8.00,
                     'Vab': 15.00,
                     'Vcentr': 118.00}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['Jab', 'Jax', 'Jbx', 'Vab', 'Vcentr']:
            widget = VarBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)


class ABX3_Bar(ToolBar):
    """A subclass of ToolBar designed for use with ABX3 simulations.

   Extends ToolBar with necessary ABX3 inputs, and overwrites .model as
   'ABX3'.
   """

    def __init__(self, parent=None, **options):
        ToolBar.__init__(self, parent, **options)
        self.model = 'ABX3'
        self.vars = {'Jab': -12.00,
                     'Jax': 7.00,
                     'Jbx': 7.00,
                     'Vab': 14.00,
                     'Vcentr': 150}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['Jab', 'Jax', 'Jbx', 'Vab', 'Vcentr']:
            widget = VarBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)


class AAXX_Bar(ToolBar):
    """A subclass of ToolBar designed for use with AA'XX' simulations.

   Extends ToolBar with necessary ABX3 inputs, and overwrites .model as
   'AAXX'.
   """

    def __init__(self, parent=None, **options):
        # WINDNMR uses all caps JAA', JXX', etc. However, the controller
        # function uses Jab, Jax etc. Also, with conversion to using kwargs
        # instead of args, can't have dict keys with apostrophes. So, VarBox
        # names coverted to args in nmrmath.AAXX for now. Future: probably
        # want to refactor so that toolbar widgets can have separate labels
        # and dict keys.
        ToolBar.__init__(self, parent, **options)
        self.model = 'AAXX'
        self.vars = {'Jaa': 15.00,
                     'Jxx': -10.00,
                     'Jax': 40.00,
                     'Jax_prime': 6.00,
                     'Vcentr': 150}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['Jaa', 'Jxx', 'Jax', 'Jax_prime', 'Vcentr']:
            widget = VarBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)


class AABB_Bar(ToolBar):
    # see comments to AAXX_bar for problem. Here, will try to customize
    # request_plot to work around the label conflict
    """A subclass of ToolBar designed for use with AA'XX' simulations.

    Extends ToolBar with necessary ABX3 inputs, and overwrites .model as
    'AAXX'.

    Method overridden:
        request_plot

    Method added:
        make_kwargs: used by request_plot to provide interface between the
        toolbar and the controller.
    """

    def __init__(self, parent=None, **options):
        ToolBar.__init__(self, parent, **options)
        self.model = 'AABB'
        self.vars = {'VAB': 40.00,
                     "JAA'": 15.00,
                     "JBB'": -10.00,
                     'JAB': 40.00,
                     "JAB'": 6.00,
                     'Vcentr': 150}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['VAB', "JAA'", "JBB'", 'JAB', "JAB'", 'Vcentr']:
            widget = VarBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)

    def request_plot(self):
        kwargs = self.make_kwargs()
        self.controller.update_view_plot(self.model, **kwargs)

    def make_kwargs(self):
        _Vab = self.vars['VAB']
        _Jaa = self.vars["JAA'"]
        _Jbb = self.vars["JBB'"]
        _Jab = self.vars["JAB"]
        _Jab_prime = self.vars["JAB'"]
        _Vcentr = self.vars["Vcentr"]

        data = {'Vab': _Vab,
                'Jaa': _Jaa,
                'Jbb': _Jbb,
                'Jab': _Jab,
                'Jab_prime': _Jab_prime,
                'Vcentr': _Vcentr}
        return data


class FirstOrder_Bar(ToolBar):
    """A subclass of ToolBar designed for use with first-order (
    single-signal) simulations.

    Overrides request_plot and includes method make_kwargs, to convert
    self.vars into **kwargs of the correct type for passing to the controller.
    """

    def __init__(self, parent=None, **options):
        ToolBar.__init__(self, parent, **options)
        self.model = 'first_order'
        self.vars = {'JAX': 7.00,
                     '#A': 2,
                     'JBX': 3.00,
                     '#B': 1,
                     'JCX': 2.00,
                     '#C': 0,
                     'JDX': 7,
                     '#D': 0,
                     'Vcentr': 150}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot}
        for key in ['JAX', '#A', 'JBX', '#B', 'JCX', '#C',
                         'JDX', '#D']:
            if '#' not in key:
                widget = VarBox(self, name=key, **kwargs)
            else:
                widget = IntBox(self, name=key, **kwargs)
            widget.pack(side=LEFT)

    def request_plot(self):
        kwargs = self.make_kwargs()
        self.controller.update_view_plot(self.model, **kwargs)

    def make_kwargs(self):
        """Convert the dictionary of widget entries (self.vars) to a dict
        that is compliant with the controller interface.

        The controller needs to pass a (signal, couplings) tuple to the model.
        - signal is a (frequency, intensity) tuple representing the frequency
        and intensity of the signal in the absence of coupling. Intensity is
        1 by default.
        - couplings is a list of (J, n) tuples, where J is the coupling
        constant and n is the number of nuclei coupled to the nucleus of
        interest with that same J value.
        """
        _Jax = self.vars['JAX']
        _a   = self.vars['#A']
        _Jbx = self.vars['JBX']
        _b = self.vars['#B']
        _Jcx = self.vars['JCX']
        _c   = self.vars['#C']
        _Jdx = self.vars['JDX']
        _d = self.vars['#D']
        _Vcentr = self.vars['Vcentr']
        singlet = (_Vcentr, 1)  # using default intensity of 1
        allcouplings = [(_Jax, _a), (_Jbx, _b), (_Jcx, _c), (_Jdx, _d)]
        couplings = [coupling for coupling in allcouplings if coupling[1] != 0]
        data = {'signal': singlet,
                'couplings': couplings}
        return data


class SecondOrderBar(Frame):
    """
    Extends Frame to hold n frequency entry boxes, an entry box for peak
    width (default 0.5 Hz), a 2-D numpy array for frequencies (see below),
    a 2-D numpy array for coupling constants, and a button to pop up a window
    for entering J values as well as frequencies.

    The ArrayBox and ArraySpinBox widgets currently handle 2-D arrays only,
    so the frequencies only occupy the first row of a 1-row 2-dimensional
    array (self.v), and the peak widths the first column of the first row of a
    1-cell 2-D array (self.w). i.e. self.v[0, :] provides a 1-D numpy array
    of the frequencies, and self.v[0, 0] provides the peak width.

    Methods:
        add_frequency_widgets, add_peakwidth_widget, add_J_button: add the
        required widgets to the toolbar. Only intented to be called by
        __init__. TODO: review all code and learn appropriate use of private
        methods to refactor.
        vj_popup: opens a window for the entry of J values as well as
        frequencies.
        request_plot: sends model type and data to the controller

    Attributes:
        controller: the Controller object of the Model-View-Controller
        architecture. Assumes controller has an update_view_plot method.
        model (str): the type of calculation requested (interpreted by the
        controller).
        v (numpy 2D array): the frequency list (located in v[0, :]
        j (numpy 2D array): the symmetric matrix of J coupling constants
        (j[m, n] = j[n, m] = coupling between nuclei m and n)
        w (numpy 2D array): the width of the signal at half height (located
        in w[0, 0]
    """

    def __init__(self, parent=None, controller=None, n=4, **options):
        """Initialize the frame with necessary widgets and attributes.

        Keyword arguments:
        :param parent: the parent tkinter object
        :param controller: the Controller object of the MVC application
        :param n: the number of nuclei in the spin system
        :param options: standard optional kwargs for a tkinter Frame
        """
        Frame.__init__(self, parent, **options)
        self.controller = controller

        # Store a list of entry widgets for all frequencies
        # (used by vj_popup)
        # Since vj_popup doesn't need anymore, can delete?
        # self.v_widgets = np.zeros(n, dtype=object)
        self.v, self.j = getWINDNMRdefault(n)
        self.w_array = np.array([[0.5]])

        self.add_frequency_widgets(n)
        self.add_peakwidth_widget()
        self.add_J_button(n)

    def add_frequency_widgets(self, n):
        for freq in range(n):
            vbox = ArrayBox(self, array=self.v, coord=(0, freq),
                            name='V' + str(freq + 1),
                            controller=self.request_plot)
            # self.v_widgets[freq] = vbox
            vbox.pack(side=LEFT)

    def add_peakwidth_widget(self):
        wbox = ArrayBox(self, array=self.w_array, coord=(0, 0), name="W",
                        controller=self.request_plot)
        wbox.pack(side=LEFT)

    def add_J_button(self, n):
        vj_button = Button(self, text="Enter Js",
                           command=lambda: self.vj_popup(n))
        vj_button.pack(side=LEFT, expand=N, fill=NONE)

    def vj_popup(self, n):
        """
        Creates a new Toplevel window that provides entries for both
        frequencies and J couplings, and updates self.v and self.j when
        entries change.
        :param n: number of spins
        """
        tl = Toplevel()
        Label(tl, text='Second-Order Simulation').pack(side=TOP)
        # datagrid = ArrayFrame(tl, self.request_plot, self.v_widgets)
        datagrid = Frame(tl)

        # For gridlines, background set to the line color (e.g. 'black')
        datagrid.config(background='black')

        Label(datagrid, bg='gray90').grid(row=0, column=0, sticky=NSEW,
                                          padx=1, pady=1)
        for col in range(1, n + 1):
            Label(datagrid, text='V%d' % col, width=8, height=3,
                  bg='gray90').grid(
                row=0, column=col, sticky=NSEW, padx=1, pady=1)

        for row in range(1, n + 1):
            vtext = "V" + str(row)
            v = ArrayBox(datagrid, array=self.v,
                         coord=(0, row - 1),  # V1 stored in v[0, 0], etc.
                         name=vtext, color='gray90',
                         controller=self.request_plot)
            v.grid(row=row, column=0, sticky=NSEW, padx=1, pady=1)
            for col in range(1, n + 1):
                if col < row:
                    j = ArrayBox(datagrid, array=self.j,
                                 # J12 stored in j[0, 1] (and j[1, 0]) etc
                                 coord=(col - 1, row - 1),
                                 name="J%d%d" % (col, row),
                                 controller=self.request_plot)
                    j.grid(row=row, column=col, sticky=NSEW, padx=1, pady=1)
                else:
                    Label(datagrid, bg='grey').grid(
                        row=row, column=col, sticky=NSEW, padx=1, pady=1)

        datagrid.pack()

    def request_plot(self):
        # self.controller.update_view_plot(self.v[0, :], self.j,
        #                                  self.w_array[0, 0])
        kwargs = {'v': self.v[0, :],
                  'j': self.j,
                  'w': self.w_array[0, 0]}

        self.controller.update_view_plot('nspin', **kwargs)


class SecondOrderSpinBar(SecondOrderBar):
    """A subclass of SecondOrderBar that uses ArraySpinBox widgets for the
    toolbar.

    Overrides add_frequency_widgets and add_peakwidth_widget.
    """
    def __init__(self, parent=None,
                 from_=-10000.00, to=10000.00, increment=10, realtime=False,
                 **options):
        """Initialize subclass of SecondOrderBar with extra arguments for the
        SpinBox minimum and maximum values, standard increment, and realtime
        behavior.

        :param from_: (float) the minimum value for the spinboxes
        :param to: (float) the maximum value for the spinboxes
        :param increment: (float) the amount to increment/decrement the SpinBox
        contents per arrow click.
        :param realtime: (bool) True if controller should be repeatedly called
        as a SpinBox arrow is being held down.
        """
        self.spinbox_kwargs = {'from_': from_,
                               'to': to,
                               'increment': increment,
                               'realtime': realtime}
        SecondOrderBar.__init__(self, parent, **options)

    def add_frequency_widgets(self, n):
        for freq in range(n):
            vbox = ArraySpinBox(self, array=self.v, coord=(0, freq),
                                name='V' + str(freq + 1),
                                controller=self.request_plot,
                                **self.spinbox_kwargs)
            # self.v_widgets[freq] = vbox
            vbox.pack(side=LEFT)

    def add_peakwidth_widget(self):
        """
        Currently hard-wired to vary from 0.01 to 100 Hz, with an increment
        of 0.1 Hz.
        """
        wbox = ArraySpinBox(self, array=self.w_array, coord=(0, 0),
                            name="W",
                            controller=self.request_plot,
                            from_=0.01, to=100, increment=0.1,
                            realtime=self.spinbox_kwargs['realtime'])
        wbox.pack(side=LEFT)


class DNMR_TwoSingletBar(ToolBar):
    """
    A toolbar designed for the DNMR simulation for 2 uncoupled exchanging
    nuclei.

    Method:
        request_plot: sends model type and data to the controller

    Attributes:
        Va and Vb (float): the chemcial shifts for nuclei a and b at the slow
        exchange limit.
        ka (float): the a-->b rate constant (note: WINDNMR uses ka + kb here)
        Wa and Wb (float): the width at half height of the signals for nuclei a
        and b at the slow exchange limit.
        pa (float): the % of molecules in state a. Note: must be converted to
        mol fraction prior to calling the controller.
    """

    def __init__(self, parent=None, **options):
        """Bloated code just to get toolbar reimplemented after refactor"""
        ToolBar.__init__(self, parent, **options)

        self.model = 'DNMR_Two_Singlets'
        self.vars = {'Va': 165.00,
                     'Vb': 135.00,
                     'ka': 1.50,
                     'Wa': 0.5,
                     'Wb': 0.5,
                     '%a': 50}
        kwargs = {'dict_': self.vars,
                  'controller': self.request_plot,
                  'realtime': True}
        Va = VarButtonBox(parent=self, name='Va', **kwargs)
        Vb = VarButtonBox(parent=self, name='Vb', **kwargs)
        ka = VarButtonBox(parent=self, name='ka', **kwargs)
        Wa = VarButtonBox(parent=self, name='Wa', **kwargs)
        Wb = VarButtonBox(parent=self, name='Wb', **kwargs)
        pa = VarButtonBox(parent=self, name='%a', **kwargs)
        for widget in [Va, Vb, ka, Wa, Wb, pa]:
            widget.pack(side=LEFT)

    def request_plot(self):
        _Va = self.vars['Va']
        _Vb = self.vars['Vb']
        _ka = self.vars['ka']
        _Wa = self.vars['Wa']
        _Wb = self.vars['Wb']
        _pa = self.vars['%a'] / 100
        self.controller.update_view_plot(self.model,
                                         _Va, _Vb, _ka, _Wa, _Wb, _pa)


class DNMR_AB_Bar(ToolBar):
        """
        A toolbar designed for the DNMR simulation for 2 coupled exchanging
        nuclei.

        Method:
            request_plot: sends model type and data to the controller

        Attributes:
            Va and Vb (float): the chemcial shifts for nuclei a and b at the
            slow exchange limit.
            J (float): the Jab coupling constant
            kAB (float): the exchange rate constant
            W (float): the peak width at half-height at the slow exchange limit
        """

        def __init__(self, parent=None, **options):
            ToolBar.__init__(self, parent, **options)
            self.model = 'DNMR_AB'
            self.vars = {'Va': 165.00,
                         'Vb': 135.00,
                         'J': 12.00,
                         'kAB': 1.50,
                         'W': 0.5}
            kwargs = {'dict_': self.vars,
                      'realtime': True,
                      'controller': self.request_plot}
            Va = VarButtonBox(parent=self, name='Va', **kwargs)
            Vb = VarButtonBox(parent=self, name='Vb', **kwargs)
            J = VarButtonBox(parent=self, name='J', **kwargs)
            kAB = VarButtonBox(parent=self, name='kAB', **kwargs)
            # W is a tkinter string, so use W_
            W_ = VarButtonBox(parent=self, name='W', **kwargs)
            for widget in [Va, Vb, J, kAB, W_]:
                widget.pack(side=LEFT)

        def request_plot(self):
            _Va = self.vars['Va']
            _Vb = self.vars['Vb']
            _J = self.vars['J']
            _kAB = self.vars['kAB']
            _W = self.vars['W']

            self.controller.update_view_plot(self.model, _Va, _Vb, _J, _kAB, _W)


if __name__ == '__main__':

    toolbars = [AB_Bar, AB2_Bar, ABX_Bar, ABX3_Bar, AAXX_Bar, AABB_Bar,
                FirstOrder_Bar, SecondOrderBar, SecondOrderSpinBar,
                DNMR_TwoSingletBar, DNMR_AB_Bar]


    class DummyController:
        @staticmethod
        def update_view_plot(*args, **kwargs):
            print(args)
            print(kwargs)

    dummy_controller = DummyController()

    root = Tk()
    root.title('test toolbars')

    for toolbar in toolbars:
        toolbar(root, controller=dummy_controller).pack(side=TOP)

    # workaround fix for Tk problems and mac mouse/trackpad:
    while True:
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass

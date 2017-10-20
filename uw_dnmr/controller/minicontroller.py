"""
A mini-controller for interfacing with a 1-model minimodel (AB DNMR simulation)

Provides the following class:
* Controller    Class that handles data and requests to/from the model and 
                the view.
"""

from uw_dnmr.model.minimodel import dnmrplot_AB


class MiniController:
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

    def __init__(self):
        """Instantiate the view as a child of root, and then initializes it.
        
        Argument:
            root: a tkinter.Tk() object
        """
        self.models = {'DNMR_AB': dnmrplot_AB}

        self.DNMR_AB_defaults = {'v1': 165.00,
                                 'v2': 135.00,
                                 'J': 12.00,
                                 'k': 12.00,
                                 'W': 0.5}

        self.view = MockView()

    def DNMR_AB_kwargs_to_args(self, **kwargs):
        """Convert view's data to args for model.

        In the actual project, dicts are how variables are passed between the
        View's numerical entry widgets and the Controller. Some models need
        the Controller to provide an interface, converting this data to the
        arguments required by the mode. Reduced this down to one conversion
        for one model.
        """
        args = []
        for arg_name in ['v1', 'v2', 'J', 'k', 'W']:
            args.append(kwargs[arg_name])
        return args

    def update_view_plot(self, model_name, *args, **kwargs):
        """
        Parse the view's request; call the appropriate model for simulated
        spectral data; and tell the view to plot the data.

        :param model: (str) The type of calculation to be performed.
        :param args: DNMR model is called with positional arguments.
        :param data: first-order and second-order simulations are called with
        keyword arguments.

        :return: None (including when model is not recognized)
        """
        if 'DNMR' in model_name:
            plotdata = self.models[model_name](*args)
        else:
            print('model not recognized')
            return
        self.view.plot_data(*plotdata)

class MockView:
    def plot_data(self, x, y):
        print('x data sent to view:')
        print(x)
        print('y data sent to view')
        print(y)


if __name__ == '__main__':

    controller = MiniController()
    initial_variables = controller.DNMR_AB_kwargs_to_args(
        **controller.DNMR_AB_defaults)
    print('initial variables: ', initial_variables)
    controller.update_view_plot('DNMR_AB', *initial_variables)
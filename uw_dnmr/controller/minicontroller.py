"""
A mini-controller for interfacing with a 1-model minimodel (AB DNMR simulation)

Provides the following class:
* Controller    Class that handles data and requests to/from the model and 
                the view.
"""

from uw_dnmr.model.minimodel import dnmrplot_AB


class MiniController:
    """A stripped down controller to demonstrate the MVC relationships.
    
    The controller assumes the view offers the following methods:
    
    * plot_data--accept a tuple of x, y numpy arrays and plot the data.
    
    The controller provides the following methods:
    
    * update_view_plot: parse the data sent by the view; call the appropriate
    model simulation; and tell the view to plot the model's simulated
    spectral data.

    * DNMR_AB_kwargs_to_args: a utility function that converts model data as
    kwargs to model data as args. Used for testing and to allow the web GUI
    flexibility in how to pass variables to the controller.
    """

    def __init__(self):
        """Instantiate the view as a child of root, and then initializes it.

        Attributes:
            models: (dict) Matches a model's name to the model function
            (currently limited to DNMR_AB)
            DNMR_AB_defaults: (dict) Variable names and numbers to initialize
             the GUI with.
            view: the View. Ultimately, this must be some interface between
            Python and the HTML/JS. Here, mocked out.
        """
        self.models = {'DNMR_AB': dnmrplot_AB}
        self.DNMR_AB_defaults = {'v1': 165.00,
                                 'v2': 135.00,
                                 'J': 12.00,
                                 'k': 12.00,
                                 'W': 0.5}
        self.view = MockView()

    def update_view_plot(self, model_name, *args, **kwargs):
        """
        Parse the view's request; call the appropriate model for simulated
        spectral data; and tell the view to plot the data.

        :param model: (str) The type of calculation to be performed.
        :param args: DNMR model is called with positional arguments.
        :param kwargs: other simulations may be called with keyword arguments.

        :return: None (including when model is not recognized)
        """
        if 'DNMR' in model_name:
            plotdata = self.models[model_name](*args)
        else:
            print('model not recognized')
            return
        self.view.plot_data(*plotdata)

    def DNMR_AB_kwargs_to_args(self, **kwargs):
        """Convert kwargs to args for DNMR_AB model."""
        args = []
        for arg_name in ['v1', 'v2', 'J', 'k', 'W']:
            args.append(kwargs[arg_name])
        return args


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
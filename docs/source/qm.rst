The **ABC...** Menu: QM Simulation of Second-Order Spin Systems
---------------------------------------------------------------

**uw-dnmr** can simulate a second-order spin system for up to 8 spin-1/2 nuclei. [2]_
Frequencies for each nucleus 1-n can be entered
using the **V1** ... **Vn** entry widgets along the top of the application window.
Clicking the **Enter Js** button to the right of these entries pops up a window
with a grid of entries for the J coupling constants.
The frequencies of the nuclei can be adjusted in the pop-up window as well as the main window.

.. [2] This is the same limit as in WINDNMR.
   However, the :code:`nmrsim` library behind the QM calculations can simulate systems of up to 11 nuclei,
   so this could be increased at some point in the future.

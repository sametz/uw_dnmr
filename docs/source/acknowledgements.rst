Acknowledgements
================

Hans Reich (University of Wisconsin-Madison) kindly shared his original Visual
Basic 6 code, which served as a
guide to recreating the functionality and structure of WinDNMR.
Some of the VB6 variable names and gross function structure are
inherited by UW-DNMR, particular in the first-order calculations, but the
math routines were written from scratch by G.S., and any flaws in UW-NMR
calculations are solely attributable to G.S.
UW-DNMR also initializes its simulations with the same variables as
WinDNMR, to compare and verify that the simulations are performing correctly.

The second-order calculations are entirely different from WinDNMR's, and draw
primarily from two sources:

* The lectures at `spindynamics.org <http://spindynamics.org/support.php>`_, particularly Ilya Kuprov's MATLAB code in "Simulation design and coding, Part I/II"
* Examples found on the website of Frank Rioux (St. John's University and College of St. Benedict), particulary this example of tensor algebra: `<http://www.users.csbsju.edu/~frioux/nmr/ABC-NMR-Tensor.pdf>`_

Although "baking the spin Hamiltonian from scratch" is educational, and may
enable the modeling of non-spin-1/2 nuclei in the future, it likely comes at
a performance cost, and may be factored out in future versions.


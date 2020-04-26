TESTING HAS BEEN REMOVED
========================

The tests in this folder were used 
when uw_dnmr included its own code for NMR calculations and plotting. 
These routines have now been split off, refactored,
and released as the `nmrsim <https://github.com/sametz/nmrsim>`_ library
which includes its own test suite.

The tests and helper files in tests/model are being retained as a reference.
Parts may be cannibalized for future controller/view tests.

Eventually, tests for the controller logic will appear here. 
If testing for the tkinter gui becomes possible,
those tests will also be found here.
Unit testing of a tkinter gui is known to be problematic....
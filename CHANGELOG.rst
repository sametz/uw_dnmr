##########
Change Log
##########

All notable changes to this project will be documented in this file.

The format is inspired by
`Keep a Changelog <http://keepachangelog.com/en/0.3.0/>`_
and tries to adhere to `Semantic Versioning <http://semver.org>`_.
The author interprets the terms below as follows:

* **pre-alpha status**: the app runs,
  but there is no formal unit or functional testing.
* **alpha status**: pre-alpha, plus implementation of unit and functional tests.
* **beta status**: alpha, plus documentation,
  implementation of all anticipated Version 1.0.0 features,
  and installation requirements.
* **release candidate status**: beta,
  plus standalone executable(s) for Windows, Mac OS X, and Linux.
* **Version 1.0.0 release**: a stable release.

0.2.0 - 2019-01-18 (alpha)
--------------------------

Changed
^^^^^^^

* Internal libraries for NMR calculations and plotting have been replaced with
  the `nmrsim <https://github.com/sametz/nmrsim>`_ library.
  Calculations, particularly of second-order systems of many nuclei,
  should now be much faster.

* The frequency x-axis is now reversed,
  so that frequencies increase to the left (which is the NMR standard).

* The 'Multiplet -> ABX' simulation should now match WINDNMR's output.

* The DNMR AB simulation now initializes with the same rate constant
  as WinDNMR.

Broken
^^^^^^

* The tests in tests/model are no longer needed,
  since the nmrsim library has its own test suite.
  The contents are retained for possible future use,
  when controller/view testing is implemented.

0.1.1 - 2017-10-14 (alpha)
--------------------------

Bug Fix
^^^^^^^

* #A/B/C/D in the toolbar for first order calculations now properly initialized
  with 0 instead of 0.00, and return integers instead of floats (which caused
  typeerrors with the model calculations).

0.1.0 - 2017-10-14 (alpha release)
----------------------------------

Initial Commit

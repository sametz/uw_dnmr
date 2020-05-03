The **Multiplet** Menu: non-QM Solutions
----------------------------------------

These models have alebraic solutions
that don't require a quantum-mechanical approach: [1]_

* **1stOrd:** a first-order multiplet
* **AB:** an AB quartet.
* **AB2:** an AB\ :sub:`2` system.
* **ABX:** an ABX system.
* **ABX3:** an ABX\ :sub:`3` system.
* **AAXX:** an AA'XX' system.
* **AABB:** an AA'BB' system.

Conventions Used
^^^^^^^^^^^^^^^^

**Vcentr:** The central frequency that a signal is distributed about.
For **1stOrd**, this is the centre of the multiplet.
For other models, it is the average frequency (in the absence of coupling)
between the two signals that are the focus of the simulation
(A and B for AB, ABX and ABX\ :sub:`3`;
A/A' and B/B' or X/X' for AA'BB'/AA'XX'). i.e.

.. math::

   V_{centr} = \frac{|\nu_A - \nu_B|}{2}

**Vab**: The difference in frequency between nuclei A and B
(in the absence of coupling), i.e. :math:`\Delta\nu_{AB}`

**Jmn** corresponds the the J\ :sub:`mn` coupling between M and N nuclei.
"Jax" and "Jax_prime" refer to the J\ :sub:`AX` and J\ :sub:`AX′` couplings, respectively.

First-Order Multiplet
^^^^^^^^^^^^^^^^^^^^^

This model will simulate a first-order multiplet.
The simulation is limited to a maximum of 4 different J values
(JAX/JBX/JCX/JDX) but can have multiple couplings of each size.

AB and AB\ :sub:`2`
^^^^^^^^^^^^^^^^^^^

placeholder

ABX
^^^

placeholder

ABX\ :sub:`3`
^^^^^^^^^^^^^^

placeholder

AA'XX' and AA'BB'
^^^^^^^^^^^^^^^^^

placeholder



.. [1] See: Pople, J.A.; Schneider, W.G.; Bernstein, H.J.
   *High-Resolution Nuclear Magnetic Resonance.*
   New York: McGraw-Hill, 1959.

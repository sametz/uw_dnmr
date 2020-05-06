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

These simulations take parameters for Jab, Vab and Vcentr.
Keep in mind that, if you are trying to match an experimental AB pattern,
that Vab is *not* the midpoint of the individual "doublet" for A and B.
As the degree of second-order behavior increases (as Vab decreases),
:math:`\nu_A` and :math:`\nu_B` will be closer to the larger, inner peaks
than the smaller, outer peaks:

TODO: add graphic

ABX
^^^

This ABX model is an analytic solution for the case
where the frequency of H\ :sub:`X` is far from Vcentr.
This simplifies the math,
but the appearance of the H\ :sub:`X` does not change as :math:`\nu_X` changes.
If accuracy is required, the **"ABC..." Calc Type**  should be used
to model the exact second-order behavior.

ABX\ :sub:`3`
^^^^^^^^^^^^^^

This simulation makes two simplifying assumptions:

* the frequency of H\ :sub:`X` is far from Vcentr
* :math:`J_{AX} \approx J_{BX}` (which is usually the case)

This is effectively an AB quartet
where each of the 4 lines is further split into a first-order quartet.
The simulation only displays the AB part of the signal.

AA'XX'
^^^^^^

This simulates one half (e.g. the A part) of an AA'XX' spin system.
The simulation assumes a very large frequency difference between  H\ :sub:`A` and  H\ :sub:`X`.

AA'BB'
^^^^^^

This is a complete second-order (quantum-mechanical) simulation for an AA'BB' spin system.
No simplifying assumptions are made.


.. [1] See: Pople, J.A.; Schneider, W.G.; Bernstein, H.J.
   *High-Resolution Nuclear Magnetic Resonance.*
   New York: McGraw-Hill, 1959.

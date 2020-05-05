The **DNMR** Menu: Simulated Lineshapes for Exchanging Nuclei
-------------------------------------------------------------

Currently **uw-dnmr** can sumulate DNMR lineshapes for:

  * two uncoupled nuclei undergoing exchange
  * two coupled nuclei undergoing exchange

More models from WINDNMR will be added over time,
as they are added to the `nmrsim library`_.

.. _nmrsim library: https://github.com/sametz/uw_dnmr/releases

2-spin
^^^^^^

This lineshape is calculated by the method reported by Sandström. [3]_

AB Coupled
^^^^^^^^^^

This lineshape is calculated using the method reported by J.A. Weil et al. [4]_



.. [3] Sandström, J. Dynamic NMR Spectroscopy; Academic Press: New York, 1982.
.. [4] Brown, K.C.; Tyson, R.L.; Weil, J.A. J. Chem. Educ. 1998, 75, 1632.
   Note:  an important math correction to the previous reference.
   Equation (2b) should read:

   .. math::

      b_\pm &= 4\pi(\nu_o-\nu\pm J/2)(\tau^{-1}+\tau_2^{-1})\mp 2\pi J\tau^{-1}\\

   In the original paper, the final term erroneously used :math:`"\pm"` instead of :math:`"\mp"`.

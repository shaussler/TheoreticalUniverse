.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Contribute
==========

(or reproduce/check results)

Running calculations
--------------------

You can install all dependencies by running:

.. code:: bash

   # Install build dependencies
   pip install wheel setuptools

   # Install pycartan and dependencies
   pip install numpy sympy scipy
   pip install symbtools
   pip install pycartan

   # Build theoretical_python
   python setup.py bdist_wheel

   # Install theoretical_python
   pip install dist/theoretical_python*.whl

git
---

Clone repository:

.. code:: bash

   https://shaussler.github.io/TheoreticalUniverse/

``cd`` and create your branch:

.. code:: bash

   cd TheoreticalUniverse
   git checkout -b your_contribution

Do your changes and send a merge request. Upon acceptance, an automated
pipeline is started and your contribution rolled out.

Build locally
-------------

The site is serverd on ``localhost:8000``. From the
``TheoreticalUniverse/theoretical_universe`` directory, run:

.. code:: bash

   make clean
   sphinx-build ./ _build/html/
   python3 -m http.server 8000 --directory  _build/html/

To build in parallel:

.. code:: bash

   sphinx-build -j 4 ./ _build/html/

To automaticall update on modifications:

.. code:: bash

   sphinx-autobuild -j 4 ./ _build/html/

Dropdown
--------

You can keep a dropdown amdonition while working by setting the ``:class:``
to ``toggle-shown``.

.. code::

   .. admonition:: All Calculation Steps
      :class: dropdown,toggle-shown

neovim configuration
--------------------

I use neovim on Android termux and you might find my configuration helpfull,
should you want to correct, modify or add to this serie of articles:

.. literalinclude:: conf/init.vim
   :language: vim

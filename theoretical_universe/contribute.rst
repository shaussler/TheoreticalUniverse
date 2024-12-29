.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

How to Contribute
=================

.. {{{

I welcome contributions! To get started:

1. Fork the repository on GitHub and clone it locally.
2. Create a new branch for your changes.
3. Make your modifications, ensuring they align with the project's goals.
4. Push the branch to your fork on GitHub.
5. Submit a pull request with a detailed description of your changes.

You can find the repository here: https://github.com/shaussler/TheoreticalUniverse

Once your pull request is reviewed and accepted, an automated pipeline will
run, and your contribution will be deployed.

.. }}}

Running calculations
--------------------

.. {{{

.. tip::

   This is not used anymore, I found a way to simplify calculations with a
   permutation operator. Also the work to be put in writing symbolic
   computation is more than just perform the calculations.

Some of the calculations were performed using symbolic computation software. I
found only one library capable of performing symbolic calculations with
differential forms: `pycartan <https://github.com/TUD-RST/pycartan>`_. However,
this library has not been updated since 2017 and is limited to Euclidean
geometries.

To extend its functionality to Minkowski space, I monkey-patched the library.
You can install all required dependencies by running:

.. code:: bash

   # Install build dependencies
   # --------------------------

   pip install wheel setuptools

   # Install pycartan and dependencies
   # ---------------------------------

   pip install numpy sympy scipy
   pip install symbtools
   pip install pycartan

   # Build theoretical_python
   # ------------------------

   python setup.py bdist_wheel

   # Install theoretical_python
   # --------------------------

   pip install dist/theoretical_python*.whl

.. }}}

Build locally
-------------

.. {{{

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

.. }}}

Check for broken links
----------------------

.. {{{

.. code:: bash

   sphinx-build ./ _build/html/ -b linkcheck

.. }}}

Hiding content under construction
---------------------------------

.. {{{

Since I am working from my mobile phone, the sphinx configuration checks if the
environment variable ``TERMUX_VERSION`` is set in order to determine whether
draft content should be shown. To hide content, use:

.. code:: rst

   .. ifconfig:: draft in ('yes')

. }}}

Dropdown
--------

.. {{{

You can keep a dropdown admonition while working by setting the ``:class:`` to
``toggle-shown``.

.. code::

   .. admonition:: All Calculation Steps
      :class: dropdown,toggle-shown

.. }}}

vim cheatsheet
--------------

.. {{{

========================================================== =======
Action                                                     Command
========================================================== =======
Select previous select                                     ``gv``
Fold to 80 characters                                      ``gq``
Fold all                                                   ``zm``
========================================================== =======

.. }}}

neovim configuration
--------------------

.. {{{

I use neovim on Android termux and you might find my configuration helpfull,
should you want to correct, modify or add to this serie of articles. To install
neovim plugins:

.. code:: bash

   curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

My configuration is included in the repository:

.. literalinclude:: conf/init.vim
   :language: vim

To install in vim:

.. code:: vim

   :PlugInstall

.. }}}

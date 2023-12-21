Hodge Dual of the Faraday Tensor
================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

In this article, I present the Hodge dual of the Faraday tensor.

Matrix representation of antisymmetric bilinear forms.


A vector is represented like so:

.. math::

   v = \begin{bmatrix} a \\ b \\ c \end{bmatrix}
     = a \; \mathbf{e_x} + b \; \mathbf{e_y} + c \; \mathbf{e_z}

We can choose and non-standard representation of our vector like so:

.. math::

   v = \begin{bmatrix}
           a \; \mathbf{e_x}  \\ b \; \mathbf{e_y} \\ c \; \mathbf{e_z}
       \end{bmatrix}


Which expresses that the ith row represents the amount of :math:`\mathbf{e_i}`.

This is more interesting for antisymmetric bilinear forms :math:`\mathbf{e_i}
\wedge \mathbf{e_j}`. Now we can represent like so:

.. math::

   b = \begin{bmatrix}
       b_{xx} \; \mathbf{e_x} \wedge \mathbf{e_x} & b_{xy} \; \mathbf{e_x} \wedge \mathbf{e_y} & b_{xz} \; \mathbf{e_x} \wedge \mathbf{e_z} \\
       b_{yx} \; \mathbf{e_y} \wedge \mathbf{e_x} & b_{yy} \; \mathbf{e_y} \wedge \mathbf{e_y} & b_{yz} \; \mathbf{e_y} \wedge \mathbf{e_z} \\
       b_{zx} \; \mathbf{e_z} \wedge \mathbf{e_x} & b_{zy} \; \mathbf{e_z} \wedge \mathbf{e_y} & b_{zz} \; \mathbf{e_z} \wedge \mathbf{e_z} \\
       \end{bmatrix}

Since :math:`\mathbf{e_i} \wedge \mathbf{e_i} = 0`, we can represent it like
so and begin to highlight symmetries

.. math::

   b = \begin{bmatrix}
                                                  & b_{xy} \; \mathbf{e_x} \wedge \mathbf{e_y} & b_{xz} \; \mathbf{e_x} \wedge \mathbf{e_z} \\
       b_{yx} \; \mathbf{e_y} \wedge \mathbf{e_x} &                                            & b_{yz} \; \mathbf{e_y} \wedge \mathbf{e_z} \\
       b_{zx} \; \mathbf{e_z} \wedge \mathbf{e_x} & b_{zy} \; \mathbf{e_z} \wedge \mathbf{e_y} &                                            \\
       \end{bmatrix}

Looking at the hodge dual of all basis vectors:

.. math::

   \star \mathbf{e_x} = \mathbf{e_y} \wedge \mathbf{e_z} \\
   \star \mathbf{e_y} = \mathbf{e_z} \wedge \mathbf{e_x} \\
   \star \mathbf{e_z} = \mathbf{e_x} \wedge \mathbf{e_y}

Note that the hodge dual of :math:`\mathbf{e_y}` is :math:`\mathbf{e_z} \wedge
\mathbf{e_x}`, and not :math:`\mathbf{e_x} \wedge \mathbf{e_z}`. Let us use that
and orient like the hodge dual:

.. math::

   b = \begin{bmatrix}
                                                    & +b_{xy} \; \mathbf{e_x} \wedge \mathbf{e_y} & -b_{xz} \; \mathbf{e_z} \wedge \mathbf{e_x} \\
       - b_{yx} \; \mathbf{e_x} \wedge \mathbf{e_y} &                                             & +b_{yz} \; \mathbf{e_y} \wedge \mathbf{e_z} \\
       + b_{xz} \; \mathbf{e_z} \wedge \mathbf{e_x} & -b_{zy} \; \mathbf{e_y} \wedge \mathbf{e_z} &                                            \\
       \end{bmatrix}

.. math::

   \star b
   =
   \begin{bmatrix}
                            & +b_{xy} \; \mathbf{e_z} & -b_{xz} \; \mathbf{e_y} \\
   - b_{yx} \; \mathbf{e_z} &                         & +b_{yz} \; \mathbf{e_x} \\
   + b_{xz} \; \mathbf{e_y} & -b_{zy} \; \mathbf{e_x} &                         \\
   \end{bmatrix}

.. math::

   \star b = (b_{yz}-b_{zy}) \; \mathbf{e_x} + (b_{zx}-b_{xz}) \; \mathbf{e_y} + (b_{xy}-b_{yx}) \; \mathbf{e_z}
           = \begin{bmatrix} b_{yz}-b_{zy} \\ b_{zx}-b_{xz} \\ b_{xy}-b_{yx} \end{bmatrix}



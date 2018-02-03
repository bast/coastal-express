.. image:: https://travis-ci.org/bast/coastal-express.svg?branch=master
   :target: https://travis-ci.org/bast/coastal-express/builds
.. image:: https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg
   :target: ../master/LICENSE


Coastal express
===============

Compute nearest neighbor distances along the coast with a view angle.


Installation
------------

.. code:: shell

  $ pip install --process-dependency-links git+https://github.com/bast/coastal-express.git


Example
-------

.. code:: shell

  cx --boundary="$PWD/boundary.txt" \
     --islands="$PWD/islands.txt" \
     --view-angle=20.0 \
     --min-distance=3.0 \
     --max-distance=40.0 \
     --output-dir="$PWD/output"


Available options
-----------------

.. code:: shell

  $ cx --help

  Usage: cx [OPTIONS]

  Options:
    --boundary TEXT      File containing the boundary.
    --islands TEXT       File(s) containing island data - you can use wildcards.
    --view-angle TEXT    View angle in degrees.
    --min-distance TEXT  Min distance.
    --max-distance TEXT  Max distance.
    --output-dir TEXT    Direction of the time arrow (0, 90, 180, or 270).
    --help               Show this message and exit.


Definition of the view angle
----------------------------

The code will form view vectors perpendicular to the coastline. The code will
make sure that along the boundary, the vectors point towards "inside" and along
islands they point towards "outside". The view vector is computed to be
perpendicular to the vector connecting the two neighboring points of the
current point.

The view angle of N degrees defines a view sector N/2 degrees to both sides of
the view vector.  In other words a view angle of N degrees is N degrees wide in
total and is oriented symmetrically around the view vector which is
perpendicular to the coast line.
two neighboring points.

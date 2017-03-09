pytransloadit
=============

.. image:: https://travis-ci.org/mapbox/pytransloadit.svg
   :target: https://travis-ci.org/isaacm/pytransloadit

.. image:: https://coveralls.io/repos/isaacm/pytransloadit/badge.png
   :target: https://coveralls.io/r/isaacm/pytransloadit

Python3 client for Transloadit.

.. image:: https://farm4.staticflickr.com/3951/15672691531_3037819613_o_d.png

Install
-------

To use pytransloadit, install the pip package from github.

.. code-block:: console

    pip install https://github.com/isaacm/pytransloadit

Usage
-----

```python
from pytransloadit import client

cl = client.TransloadItClient('auth-key', 'auth-secret')
api = client.TransloadIt(client=cl)


# list all assemblies
api.assemblies.get()

# list all templates
api.templates.get()
```

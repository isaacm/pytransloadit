pytransloadit
=============

Python client for Transloadit.
See Transloadit API documentation_.

.. _documentation: http://transloadit.com/docs/api-docs/

Install
-------

To use pytransloadit, install the pip package from github.

.. code-block:: console

   pip install git+https://github.com/isaacm/pytransloadit.git

Usage
-----

.. code-block:: python

   from pytransloadit import client

   cl = client.TransloadItClient('auth-key', 'auth-secret')
   api = client.TransloadItAPI(client=cl)


   # list all assemblies
   api.assemblies.get()

   # list all templates
   api.templates.get()


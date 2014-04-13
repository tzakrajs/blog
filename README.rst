BLOG
====

What is it?
-----------
Blog is the beggining of a web framework for small projects based on bridgebeam

How do I install it?
--------------------

Skip to [here](#apache) for Apache + mod_wsgi instructions

To start, you will want to install the module:

.. code-block:: console

    $ sudo python ./setup.py install


Then you can start the server with:

.. code-block:: console

    $ run_server.py
    Bottle v0.12.5 server starting up (using WSGIRefServer())...
    Listening on http://0.0.0.0:8080/
    Hit Ctrl-C to quit.

<a name="apache"></a>Apache + mod_wsgi Setup
------------------------

1. git clone project into a directory which is writeable by apache
1. set WSGIScriptAlias to point at the full path of run_server.py

pypygo
======

.. image:: https://travis-ci.org/ScreenDriver/pypygo.svg?branch=master
        :target: https://travis-ci.org/ScreenDriver/pypygo

.. image:: https://badge.fury.io/py/pypygo.png
        :target: http://badge.fury.io/py/pypygo

.. image:: https://pypip.in/d/pypygo/badge.png
        :target: https://crate.io/packages/pypygo/

pypygo - A Python wrapper for the DuckDuckGo instant answer API

.. code-block:: pycon

    >>> import pypygo
    >>> q = pypygo.query('GitHub')
    >>> q.abstract
    'GitHub is a web-based hosting service'...
    >>> q.results[0].text
    'Official site'
    ...

See the official `DuckDuckGo API <https://duckduckgo.com/api>`_.

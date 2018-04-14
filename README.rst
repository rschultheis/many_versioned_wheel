=======
Many_Versioned_Wheel
=======

Small python library that is used for testing versioning and other things relating to pypi.
This library itself does not do anything useful, it is just a neutral package for testing
things that deal with pypi packages.

Features
========

- It knows how to print its own version. Just run `$ many_versioned_wheel` and you will see the magic happen

Installation
============

The many_versioned_wheel package is on PyPI so all you need is:

.. code-block:: console

    pip install many_versioned_wheel


To make a new version
=====================

- Change the version in many_versioned_wheel/version.py, commit it
- Run commands something like these:

.. code-block:: console

    git tag <the version num>

    python setup.py bdist_wheel

    twine upload dist/*

    git push

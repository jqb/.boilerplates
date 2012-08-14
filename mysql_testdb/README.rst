mysql_testdb-boilerplate
========================

Simple template that makes easy to check some query
in a fast way on mysql. It uses boilerplate_ engine.

.. _boilerplate: https://github.com/jqb/boilerplate


Requirements
------------

U need to have ``boilerplate`` engine installed and
ofcourse you need to have access to some ``mysql``
server.


Installation
------------

Copy / clone template to your ``boilterplate_templates`` directory.


Usage
-----

Create your sandbox directory::

  $ boil mysql_testdb mysqlsandbox

"mysqlsandbox" will be your test db name, so make sure you haven't
alredy got such database on your mysql server.


Above command will create following structure::

    /<path>/<to>/mysqlsandbox/
    ├── close.sql
    ├── data.sql
    ├── fetch.sql
    ├── run.sh
    └── schema.sql


Make sure to change your ``user`` and ``password`` in ``run.sh`` script.
By default it's set up to root/admin.

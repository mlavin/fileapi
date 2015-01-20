Django File API Example
=======================

This is an example project created for the "Creating Enriching Web Applications with Django and Backbone.js"
webcast http://www.oreilly.com/pub/e/3154 and extended by a follow up webcast
"Testing Client-Side Applications with Django" http://www.oreilly.com/pub/e/3302

It demonstrates a basic REST API using Django and a JS client application using Backbone. This
application is tested using integration tests written in Python using Selenium and using
Javascript unit tests using QUnit.

You can find a demo application running at http://fileapi.mlavin.org (Login: guest/guest)
Uploaded files must be less than 1 MB and the directory is cleared every 5 mins.


Project Requirements
--------------------

This project was written and tested using Python 3.3+. The Python dependencies
are listed in the `requirements.txt <https://github.com/mlavin/fileapi/blob/master/requirements.txt>`_ file.
These can easily be installed with `pip <http://pip.readthedocs.org/>`_::

    pip install -r requirements.txt

Using `virtualenv <http://virtualenv.readthedocs.org/>`_ is recommended.


How to Use this Repo
--------------------

The commits in the repo follow the creation of the API and client from start to finish. Branches
have been created to note stopping points along the way. To see the project evolve throughout
this process you should step through the branches in order.

Building the application:

1. `Fresh Project <https://github.com/mlavin/fileapi/tree/1-fresh-project>`_
2. `Read Only API <https://github.com/mlavin/fileapi/tree/2-read-api>`_ (`Diff <https://github.com/mlavin/fileapi/compare/1-fresh-project...2-read-api>`_)
3. `Write API <https://github.com/mlavin/fileapi/tree/3-write-api>`_ (`Diff <https://github.com/mlavin/fileapi/compare/2-read-api...3-write-api>`_)
4. `Template Layout <https://github.com/mlavin/fileapi/tree/4-template-layout>`_ (`Diff <https://github.com/mlavin/fileapi/compare/3-write-api...4-template-layout>`_)
5. `File Listing <https://github.com/mlavin/fileapi/tree/5-file-listing>`_ (`Diff <https://github.com/mlavin/fileapi/compare/4-template-layout...5-file-listing>`_)
6. `File Delete <https://github.com/mlavin/fileapi/tree/6-file-delete>`_ (`Diff <https://github.com/mlavin/fileapi/compare/5-file-listing...6-file-delete>`_)
7. `File Upload <https://github.com/mlavin/fileapi/tree/7-file-upload>`_ (`Diff <https://github.com/mlavin/fileapi/compare/6-file-delete...7-file-upload>`_)
8. `Token Authentication <https://github.com/mlavin/fileapi/tree/8-token-auth>`_ (`Diff <https://github.com/mlavin/fileapi/compare/7-file-upload...8-token-auth>`_)
9. `Configuration <https://github.com/mlavin/fileapi/tree/9-configuration>`_ (`Diff <https://github.com/mlavin/fileapi/compare/8-token-auth...9-configuration>`_)

Testing the application:

1. `Working Application <https://github.com/mlavin/fileapi/tree/1-testing-start>`_
2. `Selenium Intro <https://github.com/mlavin/fileapi/tree/2-testing-selenium-intro>`_ (`Diff <https://github.com/mlavin/fileapi/compare/1-testing-start...2-testing-selenium-intro>`_)
3. `Selenium Timeouts <https://github.com/mlavin/fileapi/tree/3-testing-selenium-timeouts>`_ (`Diff <https://github.com/mlavin/fileapi/compare/2-testing-selenium-intro...3-testing-selenium-timeouts>`_)
4. `Selenium File Interactions <https://github.com/mlavin/fileapi/tree/4-testing-file-interactions>`_ (`Diff <https://github.com/mlavin/fileapi/compare/3-testing-selenium-timeouts...4-testing-file-interactions>`_)
5. `Client Refactor <https://github.com/mlavin/fileapi/tree/5-testing-refactor-client>`_ (`Diff <https://github.com/mlavin/fileapi/compare/4-testing-file-interactions...5-testing-refactor-client>`_)
6. `QUnit Setup <https://github.com/mlavin/fileapi/tree/6-testing-qunit-setup>`_ (`Diff <https://github.com/mlavin/fileapi/compare/5-testing-refactor-client...6-testing-qunit-setup>`_)
7. `QUnit Fixtures <https://github.com/mlavin/fileapi/tree/7-testing-qunit-fixtures>`_ (`Diff <https://github.com/mlavin/fileapi/compare/6-testing-qunit-setup...7-testing-qunit-fixtures>`_)
8. `Sinon Mocks <https://github.com/mlavin/fileapi/tree/8-testing-sinon-mocks>`_ (`Diff <https://github.com/mlavin/fileapi/compare/7-testing-qunit-fixtures...8-testing-sinon-mocks>`_)
9. `Django Integration <https://github.com/mlavin/fileapi/tree/9-testing-django-intergration>`_ (`Diff <https://github.com/mlavin/fileapi/compare/8-testing-sinon-mocks...9-testing-django-intergration>`_)

License
-------

The project content is released under the BSD License. See the 
`LICENSE <https://github.com/mlavin/fileapi/blob/master/LICENSE>`_ file for more details.

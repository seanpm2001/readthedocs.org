User-defined Redirects
======================

You can set up redirects for a project in your project dashboard's :guilabel:`Redirects` page.

Quick Summary
-------------

* Log into your readthedocs.org account.
* From your dashboard, select the project on which you wish to add redirects.
* From the project's top navigation bar, select the :guilabel:`Admin` tab.
* From the left navigation menu, select :guilabel:`Redirects`.
* In the form box "Redirect Type" select the type of redirect you want. See below for detail.
* Depending on the redirect type you select, enter FROM and/or TO URL as needed.
* When finished, click the :guilabel:`Add` button.

Your redirects will be effective immediately.

Limitations
~~~~~~~~~~~

Redirects are only implemented in case of a *404 File Not Found* error.
If you need to redirect a large number of files that still exist,
please reach out to :doc:`/support`.

Page & Exact Redirects can redirect to URLs outside Read the Docs.
Define the `To URL` as the absolute URL you want to redirect to.

Redirect Types
--------------

We offer a few different type of redirects based on what you want to do.

Prefix Redirects
~~~~~~~~~~~~~~~~

The most useful and requested feature of redirects was when migrating to Read the Docs from an old host.
You would have your docs served at a previous URL,
but that URL would break once you moved them.
Read the Docs includes a language and version slug in your documentation,
but not all documentation is hosted this way.

Say that you previously had your docs hosted at ``https://docs.example.com/dev/``,
you move ``docs.example.com`` to point at Read the Docs.
So users will have a bookmark saved to a page at ``https://docs.example.com/dev/install.html``.

You can now set a *Prefix Redirect* that will redirect all 404's with a prefix to a new place.
The example configuration would be::

    Type: Prefix Redirect
    From URL: /dev/

Your users query would now redirect in the following manner::

        docs.example.com/dev/install.html ->
        docs.example.com/en/latest/install.html

Where ``en`` and ``latest`` are the default language and version values for your project.

.. note::

   If you were hosting your docs without a prefix, you can create a ``/`` Prefix Redirect,
   which will prepend ``/$lang/$version/`` to all incoming URLs.


Page Redirects
~~~~~~~~~~~~~~

A more specific case is when you move a page around in your docs.
The old page will start 404'ing,
and your users will be confused.
*Page Redirects* let you redirect a specific page.

Say you move the ``example.html`` page into a subdirectory of examples: ``examples/intro.html``.
You would set the following configuration::

    Type: Page Redirect
    From URL: /example.html
    To URL: /examples/intro.html

**Page Redirects apply to all versions of you documentation.**
Because of this,
the ``/`` at the start of the ``From URL`` doesn't include the ``/$lang/$version`` prefix (e.g.
``/en/latest``), but just the version-specific part of the URL.
If you want to set directs only for some languages or some versions, you should use
:ref:`user-defined-redirects:exact redirects` with the fully-specified path.

Exact Redirects
~~~~~~~~~~~~~~~

*Exact Redirects* are for redirecting a single URL,
and take into account the full URL (including language & version).

Say you're moving ``docs.example.com`` to Read the Docs and want to redirect traffic
from an old page at ``https://docs.example.com/dev/install.html`` to a new URL
of ``https://docs.example.com/en/latest/installing-your-site.html``.

The example configuration would be::

    Type: Exact Redirect
    From URL: /dev/install.html
    To URL:   /en/latest/installing-your-site.html

Your users query would now redirect in the following manner::

        docs.example.com/dev/install.html ->
        docs.example.com/en/latest/installing-your-site.html

Note that you should insert the desired language for "en" and version for "latest" to
achieve the desired redirect.

*Exact Redirects* could be also useful to redirect a whole sub-path to a different one by using a special ``$rest`` keyword in the "From URL".
Let's say that you want to redirect your readers of your version ``2.0`` of your documentation under ``/en/2.0/`` because it's deprecated,
to the newest ``3.0`` version of it at ``/en/3.0/``.

This example would be::

  Type: Exact Redirect
  From URL: /en/2.0/$rest
  To URL: /en/3.0/

The readers of your documentation will now be redirected as::

  docs.example.com/en/2.0/dev/install.html ->
  docs.example.com/en/3.0/dev/install.html

Similarly, if you maintain several branches of your documentation (e.g. ``3.0`` and
``latest``) and decide to move pages in ``latest`` but not the older branches, you can use
*Exact Redirects* to do so.


Sphinx Redirects
~~~~~~~~~~~~~~~~

We also support redirects for changing the type of documentation Sphinx is building.
If you switch between *HTMLDir* and *HTML*, your URL's will change.
A page at ``/en/latest/install.html`` will be served at ``/en/latest/install/``,
or vice versa.
The built in redirects for this will handle redirecting users appropriately.

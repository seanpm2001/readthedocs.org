"""
This URL file is to be used in tests to emulate NGINX 404 internal redirects.

Instead of using ``fast_404`` to just return a 404, we use ``ServeError404`` and
force passing ``request.full_path()`` as ``proxito_path`` argument to the view.

``proxito_path`` is everything coming after ``_proxito_404_`` in the URL
generated by the NGINX internal redirect (proxy_pass).

This allow us to execute this ``handler404`` once Django raises ``Http404`` and
then be able to test redirects, custom 404 pages, among others.
"""
from functools import wraps

from readthedocs.proxito.urls import *  # noqa
from readthedocs.proxito.views.serve import ServeError404


# Allow performing NGINX internal redirects at Django level.
# This is useful for testing El Proxito ``@notfoundfallback``
def map_proxito_path(view_func):

    @wraps(view_func)
    def inner_view(request, exception, *args, **kwargs):
        return view_func(
            request,
            *args,
            proxito_path=request.get_full_path(),
            **kwargs,
        )
    return inner_view


handler404 = map_proxito_path(ServeError404.as_view())

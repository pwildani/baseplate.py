"""Helpers that integrate common client libraries with baseplate's diagnostics.

This package contains modules which integrate various client libraries with
Baseplate's instrumentation. When using these client library integrations,
trace information is passed on and metrics are collected automatically.

To use these helpers, use the
:py:meth:`~baseplate.core.Baseplate.add_to_context` method on your
application's :py:class:`~baseplate.core.Baseplate` object::

    client = SomeClient("server, server, server")
    baseplate.add_to_context("my_client", SomeContextFactory(client))

and then a context-aware version of the client will show up on the
:term:`context object` during requests::

    def my_handler(self, context):
        context.my_client.make_some_remote_call()

"""


class ContextFactory:
    """An interface for adding stuff to the context object.

    Objects implementing this interface can be passed to
    :py:meth:`~baseplate.core.Baseplate.add_to_context`. The return value of
    :py:meth:`make_object_for_context` will be added to the :term:`context
    object` with the name specified in ``add_to_context``.

    """

    def report_runtime_metrics(self, batch):
        """Report runtime metrics to the stats sytem."""

    def make_object_for_context(self, name, span):
        """Return an object that can be added to the context object."""
        raise NotImplementedError

import pytest

from django.core.exceptions import PermissionDenied
from django_tickets_2.models import Ticket


def test_ticket_new_ok(db, ticket_factory):
    ticket = ticket_factory()
    assert ticket.status == Ticket.STATUS_NEW

def test_ticket_pending_ok(db, ticket_factory):
    ticket = ticket_factory.pending()
    assert ticket.status == Ticket.STATUS_PENDING

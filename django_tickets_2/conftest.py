from pytest_factoryboy import register
from django_tickets_2.tests.factories import UserFactory, TicketFactory


register(UserFactory)
register(TicketFactory)

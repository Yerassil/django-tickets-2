from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied


class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)


class Ticket(models.Model):
    author = models.ForeignKey(User, related_name='tickets_authored', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200, null=False)
    description = models.TextField('Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approvers = models.ManyToManyField(User, related_name='tickets_for_approval', through='Approval')
    due_date = models.DateField(blank=True, null=True)
    assignee = models.ForeignKey(User, related_name='tickets_assigned', on_delete=models.CASCADE)

    STATUS_NEW = 'new'
    STATUS_PENDING = 'pending approval'
    STATUS_APPROVED = 'approved'
    STATUS_INPROGRESS = 'in progress'
    STATUS_COMPLETED = 'completed'
    STATUS_CHANGES_REQUESTED = 'changes requested'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = (
        (STATUS_NEW, STATUS_NEW),
        (STATUS_PENDING, STATUS_PENDING),
        (STATUS_APPROVED, STATUS_APPROVED),
        (STATUS_INPROGRESS, STATUS_INPROGRESS),
        (STATUS_CHANGES_REQUESTED, STATUS_CHANGES_REQUESTED),
        (STATUS_CLOSED, STATUS_CLOSED)
    )
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)

    def __str__(self):
        return self.title


class Approval(models.Model):
    user = models.ForeignKey(User, related_name='approvals', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='tickets', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

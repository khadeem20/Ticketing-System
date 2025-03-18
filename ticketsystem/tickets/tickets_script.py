from tickets.models import Ticket
from tickets.models import CustomUser
import random

#grab the existing user- admin
users = list(CustomUser.objects.all())

if not users:
    print('Couldnt find the user objects!!')

else:
    STATUS_CHOICES = ['OPEN', 'IN_PROGRESS', 'CLOSED']
    PRIORITY_CHOICES = ['4', '3', '2', '1']

    tickets = [
    Ticket(
        title=f"Test Ticket {i+1}",
        description=f"This is a description for Test Ticket {i+1}.",
        status=random.choice(STATUS_CHOICES),
        priority=random.choice(PRIORITY_CHOICES),
        created_by=random.choice(users),
        assigned_to=random.choice(users) if random.random() > 0.5 else None
    )
        for i in range(10)
    ]

    Ticket.objects.bulk_create(tickets)
    print("10 tickets successfully created!")
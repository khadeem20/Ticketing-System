from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can define custom roles here
    ADMIN = 'admin'
    AGENT = 'support_agent'
    END_USER = 'end_user'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (AGENT, 'Support Agent'),
        (END_USER, 'End User'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=END_USER,
    )

    # You can also add any other custom fields as needed (e.g., full name, contact info)

    def __str__(self):
        return self.username


class Ticket(models.Model):
    STATUS_CHOICES=[
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed')
    ]


    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent')
    ]

    title= models.CharField(max_length=200)
    description= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    priority= models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='LOW')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')

    def __str__(self):
        return f"{self.tile} - {self.status}"
    
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.ticket.title}"
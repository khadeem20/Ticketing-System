from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from tickets.models import Ticket 

def home(request):
    return render(request,"home.html")

def login_page(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, "login.html")
def signup_page(request):
    return render(request, "signup.html")

def dashboard(request):
    tickets = Ticket.objects.filter(
        created_by = request.user
    )

    open_tickets= len(tickets.filter(status="OPEN"))
    inprogress_tickets= len(tickets.filter(status="In Progess"))
    closed_tickets = len(tickets.filter(status="Closed"))

    latest_tickets= tickets.exclude(status='Closed').order_by('-created_date')[:5]

    context = {
        'user': request.user.username,
        'open_tickets': open_tickets,
        'closed_tickets': closed_tickets,
        'inprogress_tickets': inprogress_tickets,
        'lastest_tickets': latest_tickets
    }
    return render(request, "dashboard.html", context)

def ticket_management(request):
    tickets = Ticket.objects.filter(
        created_by = request.user
    ).order_by('created_date')

    context = {
        'user': request.user.username,
        'tickets': tickets
    }
    return render(request, "ticket_management.html", context)



#Ticket Management Functions
def create_ticket(request):  # Create new support tickets
    return 
"""
def view_ticket()    # View single ticket details
def list_tickets()   # List all tickets with filtering options
def update_ticket()  # Update ticket status/details
def delete_ticket()  # Delete a ticket



def my_tickets()     # View tickets created by current user
def assigned_tickets()  # View tickets assigned to current user/agent


def add_comment()    # Add comments to tickets
def view_comments()  # View all comments on a ticket


def change_status()  # Change ticket status (open, closed, in progress)
def change_priority()  # Update ticket priority level


def dashboard()      # Overview dashboard with statistics
def agent_dashboard()  # Specific view for support agents


def list_categories()  # View ticket categories
def assign_department()  # Assign ticket to department
"""
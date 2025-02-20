from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request,"home.html")

def login_page(request):
    if request.method == 'POST':
        username=request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username=username, passwword=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, "login.html")
def signup_page(request):
    return render(request, "signup.html")



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
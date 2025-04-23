from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .form import OrderForm
from django.contrib.auth.decorators import login_required


# Sign-up view
def signup(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        PASSWORD = request.POST.get('PASSWORD')
        rpass = request.POST.get('rpass')
        mail = request.POST.get('epass')

        if PASSWORD != rpass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Save the new user in the database
        if Signup.objects.filter(user=user).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        obj = Signup()
        obj.user = user
        obj.pasw = make_password(PASSWORD)  # Hash password before saving
        obj.email = mail
        
        obj.save()
        
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Redirect to login page after successful sign-up
    return render(request, 'signup.html')

def check_username(request):
    username = request.GET.get('username')
    exists = Signup.objects.filter(user=username).exists()
    return JsonResponse({'exists': exists})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_obj = Signup.objects.get(user=username)
            if check_password(password, user_obj.pasw):  # Password is correct
                request.session['user'] = user_obj.user  # Save user to session
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid password. Please try again.")
        except Signup.DoesNotExist:
            messages.error(request, "User does not exist.")
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', {'user': request.session.get('user')})

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def product(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())



def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Feedback.objects.create(
                name=name,
                email=email,
                message=message,
            )
            success = True

    return render(request, 'contact.html', {'success': success})


def search(request):
    search=Cakes.objects.all()
    return render(request,'search.html',{'search':search})

def search1(request):
    search1=Cookies.objects.all()
    return render(request,'search1.html',{'search1':search1})

def search2(request):
    search2=Chaats.objects.all()
    return render(request,'search2.html',{'search2':search2})

@login_required(login_url='login')  # ensures user must be logged in
def place_order(request, category, id):
    if 'user' not in request.session:
        messages.error(request, "Please log in to place an order.")
        return redirect('login')

    # Determine which product category
    if category == 'cakes':
        product = get_object_or_404(Cakes, id=id)
    elif category == 'cookies':
        product = get_object_or_404(Cookies, id=id)
    elif category == 'chaats':
        product = get_object_or_404(Chaats, id=id)
    else:
        messages.error(request, "Invalid product category.")
        return redirect('home')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product_name = product.title
            order.amount = product.amount
            order.customer_name = request.session['user']
            order.save()
            return redirect('ordersuccess')
    else:
        form = OrderForm(initial={
            'product_name': product.title,
            'amount': product.amount,
            'customer_name': request.session['user'],
        })

    return render(request, 'order.html', {'form': form, 'product': product})

def order_success(request):
    return render(request, 'success.html')









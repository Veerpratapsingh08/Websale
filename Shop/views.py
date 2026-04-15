from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Package, Order, OrderItem, Enquiry
from decimal import Decimal

# Helper for Cart management
def get_cart(request):
    cart = request.session.get('cart', {})
    return cart

def home(request):
    featured_packages = Package.objects.all()[:3]
    return render(request, "index.html", {"packages": featured_packages})

def about(request):
    return render(request, "about.html")

def services(request):
    categories = Category.objects.all()
    packages = Package.objects.all()
    query = request.GET.get('q')
    if query:
        packages = packages.filter(name__icontains=query)
    
    return render(request, "services.html", {
        "categories": categories,
        "packages": packages
    })

def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    return render(request, "package_detail.html", {"package": package})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        Enquiry.objects.create(name=name, email=email, subject=subject, message=message_text)
        messages.success(request, "Your enquiry has been sent successfully!")
        return redirect('contact')
    return render(request, "contact.html")

# Authentication Views
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect('home')

# Cart Logic
def add_to_cart(request, package_id):
    cart = get_cart(request)
    package_id = str(package_id)
    if package_id not in cart:
        cart[package_id] = {'quantity': 1, 'price': str(Package.objects.get(id=package_id).price)}
    else:
        cart[package_id]['quantity'] += 1
    request.session['cart'] = cart
    messages.success(request, "Added to cart!")
    return redirect('view_cart')

def remove_from_cart(request, package_id):
    cart = get_cart(request)
    package_id = str(package_id)
    if package_id in cart:
        del cart[package_id]
        request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = get_cart(request)
    cart_items = []
    total = Decimal(0)
    for p_id, item in cart.items():
        package = Package.objects.get(id=int(p_id))
        item_total = Decimal(item['price']) * item['quantity']
        cart_items.append({
            'package': package,
            'quantity': item['quantity'],
            'total': item_total
        })
        total += item_total
    return render(request, "cart.html", {"cart_items": cart_items, "total": total})

@login_required
def checkout(request):
    cart = get_cart(request)
    if not cart:
        return redirect('services')
    
    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city')
        )
        for p_id, item in cart.items():
            OrderItem.objects.create(
                order=order,
                product=Package.objects.get(id=int(p_id)),
                price=Decimal(item['price']),
                quantity=item['quantity']
            )
        request.session['cart'] = {}
        return render(request, "checkout_success.html", {"order": order})
    
    return render(request, "checkout.html")

@login_required
def dashboard(request):
    orders = request.user.orders.all().order_by('-created')
    return render(request, "dashboard.html", {"orders": orders})

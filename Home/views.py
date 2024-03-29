from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product,Order
from .forms import ProductForm,OrderForm, OrderUpdationForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def my_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.seller = request.user
            
            prod.save()
            #print(form.image.url)
            print(prod.image.url)
            # Process the form data
            # For example, save it to the database
            #form.save()  # Only if using ModelForm
            return redirect('home')  # Redirect after successful submission
    else:
        form = ProductForm()
    return render(request, 'productform.html', {'form': form})

def index(request):
    field_crops = Product.objects.filter(category__contains = 'FC')[:5]
    veg = Product.objects.filter(category__contains = 'VS')[:5]
    context = {
        'field_crops':field_crops,
        'veg' : veg
    }
    return render(request,'home.html',context=context)
    #return HttpResponse('this is home page')

def about(request):
     return render(request,'about.html')

def services(request):
     return render(request,'services.html')

def contact(request):
     return render(request,'contact.html')

def redirect_page(request):
     return render(request,'home.html')

def ProductDynamicView(request,slug):
    product = get_object_or_404(Product,slug=slug)

    context = {
        'product':product
    }
    return render(request,'ProductView.html',context)

def OrderDynamicView(request,id):
    order = get_object_or_404(Order,id=id)
    if request.user == order .seller:
        if request.method == 'POST':
            form = OrderUpdationForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('orderrecivedlist')
        else:
            form = OrderUpdationForm(instance=order)
        return render(request, 'update_order.html', {'form': form, 'order' : order})
    else:
        context = {
            'order': order
        }
        return render(request,'OrderView.html',context)

def OrdersView(request):
    orders = Order.objects.filter(buyer=request.user)
    return render(request,'OrderList.html',{'orders':orders})

def OrdersRecievedView(request):
    orders = Order.objects.filter(seller=request.user)
    return render(request,'OrderRecived.html',{'orders':orders})

def order_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # Create an order instance
            order = form.save(commit=False)
            order.buyer = request.user
            order.seller = product.seller
            order.product = product
            order.net_price = product.price * order.quantity
            order.save()
            # Redirect to confirmation page
            return redirect('orderplacedlist')
    else:
        form = OrderForm(initial={'quantity' : 1, 'product' : product})
    return render(request, 'order_form.html', {'form': form, 'product': product})





'''def update_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderUpdationForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orderlist')
    else:
        form = OrderUpdationForm(instance=order)
    return render(request, 'update_order.html', {'form': form, 'order' : order})'''

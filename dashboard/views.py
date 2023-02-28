from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum


from .models import Customer, Employee, Order
from .forms import CustomerForm, EmployeeForm, OrderForm

def dashboard(request):
    return render(request, 'base.html')

def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer_list.html', context)

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_list.html', context)

def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order_list.html', context)

def customer_create(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:customer_list')
    context = {'form': form}
    return render(request, 'customer_form.html', context)

def employee_create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employee_list')
    context = {'form': form}
    return render(request, 'employee_form.html', context)

def order_create(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:order_list')
    context = {'form': form}
    return render(request, 'order_form.html', context)

def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('dashboard:customer_list')
    context = {'form': form}
    return render(request, 'customer_form.html', context)

def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employee_list')
    context = {'form': form}
    return render(request, 'employee_form.html', context)

def order_update(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard:order_list')
    context = {'form': form}
    return render(request, 'order_form.html', context)

def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('dashboard:customer_list')

def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('dashboard:employee_list')

def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('dashboard:order_list')

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    orders = Order.objects.filter(customer=customer)
    total_amount = orders.aggregate(Sum('amount'))['amount__sum']
    context = {
        'customer': customer,
        'orders': orders,
        'total_amount': total_amount,
    }
    return render(request, 'customer_detail.html', context)
    
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    orders = Order.objects.filter(employee=employee)
    total_amount = orders.aggregate(Sum('amount'))['amount__sum']
    context = {
        'employee': employee,
        'orders': orders,
        'total_amount': total_amount,
    }
    return render(request, 'employee_detail.html', context)
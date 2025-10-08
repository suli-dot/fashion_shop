from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Category, Request
from .forms import RequestForm

def home(request):
    return render(request, "home.html")

def catalog_view(request):
    query = request.GET.get("q")
    category_id = request.GET.get("category")

    products = Product.objects.all()
    categories = Category.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, "catalog.html", {
        "products": products,
        "categories": categories,
        "selected_category": category_id,
        "query": query
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.product = product
            req.save()

            # отправка письма админу
            send_mail(
                subject=f"Новая заявка на {product.name}",
                message=f"Имя: {req.name}\nКонтакт: {req.contact}\nКоличество: {req.quantity}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
            )

            return render(request, "request_success.html", {"product": product})
    else:
        form = RequestForm()
    return render(request, "product_detail.html", {"product": product, "form": form})

def contact_request(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        message = request.POST.get("message")

        Request.objects.create(product=None, name=name, contact=contact, quantity=1)

        send_mail(
            subject=f"Новая заявка от {name}",
            message=f"Контакт: {contact}\n\nСообщение:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
        )

        return render(request, "request_success.html", {"product": None})

    return redirect("home")

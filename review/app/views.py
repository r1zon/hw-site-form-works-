from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    context = {'form': ReviewForm(),
               'product': product,
               }
    # request.session.flush()
    if 'reviewed_products' not in request.session.keys():
        request.session['reviewed_products'] = list()
    if request.method == 'POST':
        print(request.session['reviewed_products'])
        if pk not in request.session['reviewed_products']:
            form = ReviewForm(request.POST)
            if form.is_valid():
                request.session['reviewed_products'].append(pk)
                request.session.modified = True
                print(request.session['reviewed_products'])
                Review.objects.create(product_id = pk, text = request.POST.get('text'))
        return redirect("product_detail", pk)
    reviews = Review.objects.all().filter(product_id = pk)
    context.update({'reviews': reviews})
    if pk in request.session['reviewed_products']:
        context.update({'is_review_exist': request.session})
    return render(request, template, context)

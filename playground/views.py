from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q, F, Func, Value, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem
from tags.models import TaggedItem

# Create your views here.

def say_hello(request):
    #result = Product.objects.filter(collection__id=3).aggregate(min=Min('unit_price'), max=Max('unit_price'), avg=Avg('unit_price'))
    
    #concat
    #result = Customer.objects.annotate(
    #    full_name = Func(F('first_name'), Value(' '), F('last_name'), function = ('CONCAT'))
    #)
    #result = Customer.objects.annotate(
    #    full_name = Concat('first_name', Value(' '), 'last_name')
    #)

    #result = Customer.objects.annotate(orders_count = Count('order'))


    #discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field = DecimalField())
    #result = Product.objects.annotate(discounted_price = discounted_price)

    #content_type = ContentType.objects.get_for_model(Product)
    #queryset = TaggedItem.objects.select_related('tag').filter(content_type = content_type, object_id = 1)

    #result = TaggedItem.objects.get_tags_for(Product, 1)

    # collection = Collection(pk = 11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()
    
    # collection = Collection.objects.get(pk = 11)
    # collection.delete()
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    return render(request, 'hello.html', {'name': 'Mosh'}) 

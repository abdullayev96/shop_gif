from django.shortcuts import render, get_object_or_404
from .models import *


# menu = [{"title":"Barber Shop", "url_name":"home"},
# #         #{"title":"Admin", "url_name":"add_page"},
# #         #{"title": "contact", "url_name":"contact"},
# #         # {"title":"Back go","url_name": "login"},
# # ]

def home(request):
    return render(request, 'home.html')


def magazine(request):
    posts= Customer.objects.all()
    ctx = {
        'posts':posts,
        "cat_selected": 0,
    }

    return render(request, 'barber.html', ctx)

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #try:
#                 # Women.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('shop')
#             # except:
#             #     form.add_error(None, "Error your requested  try again please")
#
#     else:
#         form =  AddPostForm()
#     return render(request, 'addpage.html', {'form':form, "menu": menu, 'title': "About title"})
#

def show_post(request, post_slug):
    post = get_object_or_404(Customer, slug=post_slug)

    ctx = {
        "post": post,
        "title": post.title,
        "cat_selected": post.cat_id,

    }
    return render(request, 'post.html', ctx)


def show_category(request, cat_id):
    posts = Customer.objects.filter(cat_id=cat_id)
    ctx = {
        "posts": posts,
        "cat_selected": cat_id,

    }
    return render(request, 'barber.html', ctx)





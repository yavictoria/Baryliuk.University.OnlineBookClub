from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from user.models import Profile_user
from main.keeper_service import keeper_service
from django.db.models import Count
from group.models import RelGroupUser


def book_list(request):
    books_list = Book.objects.annotate(num_likes=Count('like')).order_by('-num_likes')

    print(" book_for_u ")
    user = request.user
    profile = Profile_user.objects.filter(user_id=user.id)
    user_books = set()

    if profile.exists():
        profile_u = Profile_user.objects.get(user_id=user.id)
        user_interest = profile_u.interest

        user_groups = RelGroupUser.objects.filter(user_id=user.id)
        for group_membership in user_groups:
            group = group_membership.group  # Get the group object
            group_interests = group.interest
            print("group_interests: ", group_interests)
            user_books |= set(Book.objects.filter(interest=group_interests))

        # Add books based on user's interest to the set
        user_books |= set(Book.objects.filter(interest=user_interest))
        print("user_books: ", user_books)

    return render(request, 'books/list.html', {'instance_list': books_list,
                                               'user_books': user_books})



### a book ###
def a_book(request, id):
    print(f"=== books, action: a_book === ")
    print(f"id: ", id)
    action= "a_book"
    error = keeper_service.pop("error")

    book = get_object_or_404(Book, id=id)

    interests = book.interest.all()
    print("interests", interests)
    interest_names = []  # Initialize an empty list to store interest names
    for el in interests:
        print("el.name: ", el.name)
        interest_names.append(el.name)
    print("interest_names: ", interest_names)

    image_url = ""
    if str(book.images) != "":
        print(f"image.url: {book.images.url}")
        image_url = book.images.url

    context = {
        'book': book,
        'error': error,
        'id': id,
        'image_url': image_url,
        'action': action,
        'interest_names': interest_names
    }

    return render(request, 'books/a_book.html', context)


from django.contrib.auth.decorators import login_required

@login_required
def add_like(request, id):
    book = get_object_or_404(Book, id=id)
    if request.user in book.like.all():
        # User has already liked the book, so remove the like
        book.like.remove(request.user)
    else:
        # User has not liked the book, so add the like
        book.like.add(request.user)
    return redirect('books:a_book', id=id)
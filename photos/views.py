from django.shortcuts import render, redirect

# Create your views here.
from photos.forms.comment_form import CommentForm
from photos.forms.photo_form import PhotoForm
from photos.models import Photo, Comment, Like


def list_photos(request):
    context = {
        'photos': Photo.objects.all()
    }
    return render(request, 'photos/photos_list.html', context)


def details_or_comment_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'photo': photo,
            'form': CommentForm(),
        }
        return render(request, 'photos/photos_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'], )
            comment.photo = photo
            comment.save()
            return redirect('photo details or comment', pk)
        context = {
            'photo': photo,
            'form': form,
        }
        return render(request, 'photos/photos_details.html', context)


def like_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    like = Like()
    like.photo = photo
    like.save()
    return redirect('photo details or comment', pk)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'photo': photo,
        }
        return render(request, 'photo_delete.html', context)
    else:
        photo.delete()
        return redirect('list photos')


# def edit_photo(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = PhotoForm(instance=pet)
#         context = {
#             'form': form,
#             'photo': photo,
#         }
#         return render(request, 'photo_edit.html', context)
#     else:
#         form = PhotoForm(request.POST, instance=photo)
#         if form.is_valid():
#             form.save()
#             return redirect('photo details or comment', photo.pk)
#         context = {
#             'form': form,
#             'photo': photo,
#         }
#         return render(request, 'photo_edit.html', context)


# def create_photo(request):
#
#     if request.method == 'GET':
#         form = PhotoForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'photo_create.html', context)
#     else:
#         form = PhotoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list photo')
#         context = {
#             'form': form,
#         }
#         return render(request, 'photo_create.html', context)


def persist_photo(request, photo, template_name):
    if request.method == 'GET':
        form = PhotoForm(instance=photo)
        context = {
            'form': form,
            'photo': photo,
        }
        return render(request, f'{template_name}', context)
    else:
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details or comment', photo.pk)
        context = {
            'form': form,
            'photo': photo,
        }
        return render(request, f'{template_name}', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    return persist_photo(request, photo, 'photo_edit.html')


def create_photo(request):
    photo = Photo()
    return persist_photo(request, photo, 'photo_create.html')

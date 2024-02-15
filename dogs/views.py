from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from dogs.forms import DogForm, ParentForm
from dogs.models import Category, Dog, Parent


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Питомник - Главная'
    }

    return render(request, 'dogs/index.html', context)


# def categories (request):
#
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Питомник - все породы'
#     }
#
#     return render(request, 'dogs/category_list.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Питомник - все породы'
    }


# def category_dogs(request, pk):
#     category_item = Category.objects.get(pk=pk)
#
#     context = {
#         'object_list': Dog.objects.filter(category_id=pk),
#         'title': f'Список собак породы {category_item.name}'
#     }
#
#     return render(request, 'dogs/dog_list.html', context)


class DogListView(ListView):
    model = Dog

    def get_queryset(self):  # Достаем данные по переданному айдишнику
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))

        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Список собак породы {category_item.name}'

        return context_data


class CategoryCreateView(CreateView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category


class CategoryDeleteView(DeleteView):
    model = Category


class DogCreateView(CreateView):
    model = Dog
    # fields = ('name', 'category', 'photo', 'birth_day', 'owner')
    form_class = DogForm
    success_url = reverse_lazy('dogs:categories')


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm
    success_url = reverse_lazy('dogs:categories')

    def get_success_url(self):
        return reverse('dogs:dog_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):   # Для создания формсета
        context_data = super().get_context_data(**kwargs)

        ParentFormset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=1)

        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)

        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class DogDeleteView(DeleteView):
    model = Dog

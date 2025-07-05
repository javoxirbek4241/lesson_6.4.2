from django.shortcuts import render, redirect, get_object_or_404
from .admin import Watch
from .forms import WatchForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View



# def watch_list(request):
#     watchs = Watch.objects.all().order_by('-id')
#     return render(request, 'watch_list.html', {'watchs':watchs})

# class WatchList(ListView):
#     model=Watch
#     template_name = 'watch_list.html'
#     context_object_name = 'watchs'


class WatchList(View):
    def get(self, request):
        watchs = Watch.objects.all().order_by('-id')
        return render(request, 'watch_list.html', {'watchs':watchs})      


# class WatchDetail(DetailView):
#     model=Watch
#     template_name = 'watch_detail.html'
#     context_object_name = 'watch'

class WatchDetail(View):
    def get(self, request, pk):
        watch = Watch.objects.get(id=pk)
        return render(request, 'watch_detail.html', {'watch':watch})
    

    
# def watch_detail(request, pk):
#     watch = Watch.objects.get(id=pk)
#     return render(request, 'watch_detail.html', {'watch':watch})

# def create_watch(request):
#     if request.method == 'POST':
#         brand = request.POST['brand']
#         desk = request.POST['desk']
#         image = request.FILES.get('image')
#         price = request.POST['price']
#         Watch.objects.create(brand=brand, desk=desk, image=image, price=price)
#         return redirect('watch')
#     return render(request, 'create_watch.html')


# def create_watch(request):
#     form = WatchForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('watch')
#     return render(request, 'create_watch.html', {'form':form})        
    
# class WatchCreate(CreateView):
#     model = Watch
#     form_class = WatchForm
#     template_name = 'create_watch.html'
#     success_url = reverse_lazy('watch')
    

class WatchCreate(View):
    def get(self, request):
        form = WatchForm()
        return render(request, 'create_watch.html', {'form':form})        

    def post(self, request):
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('watch')
        return render(request, 'create_watch.html', {'form':form})       
        

# def update_watch(request, pk):
#     watch = get_object_or_404(Watch, id=pk)
#     # watch = Watch.objects.get(id=pk)
#     if request.method == 'POST':
#         watch.brand = request.POST['brand']
#         watch.desk = request.POST['desk']
#         watch.price = request.POST['price']
#         image = request.FILES.get('image')
#         if image:
#             watch.image = image
#         watch.save()
#         return redirect('watch-detail', pk=watch.id)    
#     return render(request, 'watch_update.html', {'watch': watch})

# def update_watch(request, pk):
#     watch = get_object_or_404(Watch, id=pk)
#     form = WatchForm(request.POST, request.FILES, instance=watch)
#     if form.is_valid():
#         form.save()
#         return redirect('watch-detail', watch.id)
#     else:
#         form = WatchForm(instance=watch)
#     return render(request, 'watch_update.html', {'form':form})
    
# class WatchUpdate(UpdateView):
#     model = Watch
#     form_class = WatchForm
#     template_name = 'watch_update.html'
#     success_url = reverse_lazy('watch')

class Watchupdate(View):
    def get(self, request):
        watch = get_object_or_404(Watch, id=pk)
        form = WatchForm()

    def post(self, request):
        form = WatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('watch-detail', watch.id)
        else:
            form = WatchForm(instance=watch)
        return render(request, 'watch_update.html', {'form':form})

# def delete_watch(request, pk):
#     watch = get_object_or_404(Watch, id=pk)
#     if request.method == "POST":
#         watch.delete()
#         return redirect('watch')
#     return render(request, 'watch_del.html', {'watch':watch})

class WatchDelete(DeleteView):
    model = Watch
    template_name = 'watch_del.html'
    success_url = reverse_lazy('watch')





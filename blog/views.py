from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, CoinTypeForm, AuthorImageForm, PostForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import AuthorImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages





class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_form = CommentForm()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        
        coin_type_form = CoinTypeForm(instance=post.coin_type)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "coin_type_form": coin_type_form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        
        coin_type_form = CoinTypeForm(instance=post.coin_type)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "coin_type_form": coin_type_form,
            },
        )
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


""" the inspiration behind this codeblock came from [Freecode camp](https://www.youtube.com/watch?v=F5mRW0jo-U4) - Python Django Web Framework - Full Course for Beginners.
https://stackoverflow.com/questions/54415181/django-add-post-id-to-the-slug-only-if-it-already-exists
Python Django Web Framework - Full Course for Beginners.
[Codemy](https://codemy.com/) - Django Blog. 

"""



        
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'body', 'coin_type']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.featured_image = self.request.FILES.get('featured_image')  
        form.instance.author_image = self.request.FILES.get('author_image')  
        messages.success(self.request, 'Your post has been created')
        return super().form_valid(form)

""" the inspiration behind this codeblock came from 
Python Django Web Framework - Full Course for Beginners.
[Codemy](https://codemy.com/) - Django Blog. 
https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/


"""


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body', 'coin_type']  

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.featured_image = self.request.FILES.get('featured_image')  
        form.instance.author_image = self.request.FILES.get('author_image')  
        messages.success(self.request, 'Your post has been updated')
        return super().form_valid(form)

""" the inspiration behind this codeblock came from 


Python Django Web Framework - Full Course for Beginners.
[Codemy](https://codemy.com/) - Django Blog. 

"""


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

   
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, 'Your post has been deleted.')
        return HttpResponseRedirect(success_url)



class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, 'Your comment has been deleted.')
        return HttpResponseRedirect(success_url)


class UpdateCommentView(UpdateView):
    model = Comment
    template_name = 'update_comment.html'
    fields = ['body']
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        
        self.object = form.save()
        messages.success(self.request, 'Your comment has been updated.')
        return super().form_valid(form)




def custom_handler404(request, exception):

    return render(request, '404.html', status=404)


def custom_handler500(request):
    
    return render(request, '500.html', status=500)
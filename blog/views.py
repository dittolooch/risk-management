from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from taggit.models import Tag
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status = 'published')
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = '{} ({}) recommends you reading "{}"'.format(
            cleaned_data['name'], cleaned_data['email'], post.title
            )
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
            post.title, post_url, cleaned_data['name'], cleaned_data['comment']
            )
            send_mail(subject, message, 'ceo@kuang.dev',[cleaned_data['to']])
            sent = True

            #...send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post':post, 'form':form, 'sent':sent})


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = "blog/post/list.html"


def post_list(request, tag_slug=None):
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_posts = Post.published.filter(tags__in=[tag])
    else:
        all_posts = Post.published.all()
    paginator = Paginator(all_posts, 3)
    page = request.GET.get('page')


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.get(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'posts':posts,'tag':tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
                                Post,
                                slug = post,
                                status = 'published',
                                publish__year = year,
                                publish__month = month,
                                publish__day = day
                            )


    if request.method == "POST":
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False) # create a comment object without saving it to db

            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(request.build_absolute_uri('?'))
    else:
        comment_form = CommentForm()
    comments = post.comments.filter(active=True)
    return render(request, 'blog/post/detail.html', {'post':post,'comments':comments, 'comment_form':comment_form})

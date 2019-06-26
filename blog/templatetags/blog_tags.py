from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
register = template.Library()

#filters can be called in html
#{{variable|my_filter:"foo"}}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


#tag that works like a calculated variable
@register.simple_tag
def total_posts():
    return Post.published.count()

#tag that renders a template with the calculated returned object
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

#simple tags with argument can be called in html as
# {% get_most_commented_posts 3 as most_commented_posts %}
@register.simple_tag()
def get_most_commented_posts(count=1):
    most_commented_posts = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return most_commented_posts

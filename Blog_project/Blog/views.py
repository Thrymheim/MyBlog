from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'learning-django',
        'favicon' : 'https://www.svgrepo.com/show/353657/django-icon.svg',
        'title': 'django course',
        'author': 'Maziyar kolagar',
        'image': 'Django-Logo.png',
        'date': date(2024, 11, 1),
        'short_description': 'this is django course',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-python',
        'favicon' : 'https://cdn-icons-png.flaticon.com/512/919/919852.png',
        'title': 'python course',
        'author': 'Maziyar kolagar',
        'image': 'python.png',
        'date': date(2024, 11, 2),
        'short_description': 'this is python course',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-machine-learning',
        'favicon' : 'https://cdn-icons-png.flaticon.com/512/8637/8637099.png',
        'title': 'ml course',
        'author': 'Maziyar kolagar',
        'image': 'ml.png',
        'date': date(2024, 11, 3),
        'short_description': 'this is machine learning course',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
]

def get_date(post):
    return post['date']
def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:] #means i want the last two post
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})
def post(request):
    context ={
        'all_posts': all_posts,
    }
    return render(request, 'blog/all-posts.html', context)
def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    '''It iterates through all_posts
       For each post, it checks if the post's slug matches the requested slug
       Only posts that match the condition are yielded'''
    return render(request, 'blog/post-detail.html', {'post': post})



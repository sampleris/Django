from django.shortcuts import render
posts = [

    {
        'author': ' Mpara Romaric',
        'title': 'Blog post1',
        'content': 'First post content',
        'date_posted': 'February 25, 2023'

},
{
 
        'author': ' Mpara Carine',
        'title': 'Blog post2',
        'content': 'second post content',
        'date_posted': 'February 28, 2023'   
}

]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
def bootstrap(request):
    return render(request, 'blog/' )

# Create your views here.

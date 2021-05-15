from django.shortcuts import render, get_object_or_404
from .models import Blog
def home(request):
    blogs = Blog.objects.all()
    return render(request,"home.html", {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
#갖고 와야 할 테이블 (블로그 클래스)
# 즉 저 id값을 가지고 있는 blog의 데이터를 가져오거나 404 에러를 띄워라
    return render(request,"detail.html",{'blog':blog})
 
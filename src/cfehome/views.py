import pathlib
from django.shortcuts import render 
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    try:
        percent = (page_qs.count()*100.0)/qs.count()
    except:
        percent = 0.0
    my_title = "my page"
    my_context = {
        "page_title": my_title, 
        "page_visits_count": page_qs.count(), 
        "total_visits_count": qs.count(), 
        "percent": percent,
    }
    path = request.path
    print(path) 
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template,my_context)

def my_old_home_page_view(request, *args, **kwargs):
    print(this_dir)
    html_ = ""
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)
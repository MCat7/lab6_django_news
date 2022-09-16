from django.shortcuts import get_object_or_404, render, redirect

from .models import TextNews, NewsHeadline


def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    return render(
        request,
        "index.html",
        {
            "latest_news":
                NewsHeadline.objects.order_by('-pub_date')[:5],
            "message": message
        }
    )


def detail(request, new_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "text.html",
        {
            "new": get_object_or_404(NewsHeadline, pk=new_id),
            "textNews": get_object_or_404(TextNews, pk=new_id),
            "error_message": error_message
        }
    )


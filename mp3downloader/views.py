import os.path

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView


@require_http_methods(["POST"])
def AudioView(request):
    url = str(request.POST.get("videourl"))
    video_id = os.path.basename(url)
    return render(request, template_name="download.html", context={"id": video_id})


class HomeView(TemplateView):
    template_name = "index.html"

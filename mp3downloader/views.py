from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def video_id_deu(url):
    position_of_slash = url.find("v=")
    videoid = url[position_of_slash + 2 :]
    return videoid


def mp3(request):
    if request.method == "POST":
        url = str(request.POST.get("videourl"))
        id = video_id_deu(url)
        print(id)
        framecode = f"""<iframe src="https://www.yt-download.org/api/widget/mp3/{id}" width="100%" height="100%" allowtransparency="true" scrolling="yes" style="border:none"></iframe>"""

        return render(
            request, template_name="download.html", context={"framecode": framecode}
        )
    return render(request, "index.html")


print(video_id_deu(url="https://youtu.be/7GxO-brWnD0"))

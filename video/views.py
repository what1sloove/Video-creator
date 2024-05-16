from django.shortcuts import render

from utils.video_creator import create_running_text_video
from video.models import Video


def page(request):
    latest_video = Video.objects.last()
    context = {'file': latest_video}

    if request.GET and len(request.GET.get('message').strip()) != 0:
        result = create_running_text_video(request.GET.get('message'))
        Video.objects.create(title=result['title'], file=result['path'])

    return render(request, 'index.html', context)

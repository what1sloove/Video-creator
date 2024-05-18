import logging
from django.shortcuts import render

from utils.video_creator import create_running_text_video
from video.models import Video

logger = logging.getLogger('main')


def page(request):
    if request.GET:
        latest_video = Video.objects.last()
        context = {'file': latest_video}

        if len(request.GET.get('message').strip()) != 0:
            result = create_running_text_video(request.GET.get('message'))
            logger.info(result['message'])
            Video.objects.create(title=result['title'], message=result['message'], file=result['path'])
        else:
            create_running_text_video('Example')

        return render(request, 'index.html', context)

    return render(request, 'index.html')

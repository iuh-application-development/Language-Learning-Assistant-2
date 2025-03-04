from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

# Create your views here.
def serve_video(request):
    video_path = os.path.join(settings.BASE_DIR, "thanks/static/thanks/video/lovechoice.mp4")
    return FileResponse(open(video_path, "rb"), content_type="video/mp4")


def so_close_so_far(request):
    return render(request, 'thanks/so_close_so_far.html')


def memorable(request):
    return render(request, 'thanks/memorable.html')


def word_apart(request):
    img_url = 'thanks/img/img2.JPG'
    audio_url = 'thanks/audio/lc5.mp3'
    context = {
        'img_url': img_url,
        'audio_url': audio_url
    }
    return render(request, 'thanks/thanks.html', context)


def recall(request):
    img_url = 'thanks/img/img1.JPG'
    audio_url = 'thanks/audio/recall.mp3'
    context = {
        'img_url': img_url,
        'audio_url': audio_url
    }
    return render(request, 'thanks/thanks.html', context)


def thanks(request):
    img_url = 'thanks/img/thanks.jpg'
    audio_url = 'thanks/audio/lc4.mp3'
    context = {
        'img_url': img_url,
        'audio_url': audio_url
    }
    return render(request, 'thanks/thanks.html', context)
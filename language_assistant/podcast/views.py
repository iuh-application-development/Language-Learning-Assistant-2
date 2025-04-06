from django.shortcuts import render, redirect
# Create your views here.

def podcast_list(request):
    # Logic to fetch and display the list of podcasts
    return render(request, 'podcast/podcast_list.html')

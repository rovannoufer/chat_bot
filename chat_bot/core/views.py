from django.shortcuts import render
from django.http import JsonResponse




def chatbot (request):
    if request.method == 'post':
        message = request.post.get('message')
        return JsonResponse(message)
    return render(request, 'chatbot.html')

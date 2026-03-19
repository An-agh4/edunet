from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .gemini_client import get_response
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
@require_POST
def chat_api(request):
    user_prompt = request.POST.get('prompt')
    if user_prompt:
        response = get_response(user_prompt)
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'No prompt provided'})
from django.shortcuts import redirect, render
import random

# Create your views here.

def index(request):
    return render(request, 'game/index.html')

def result(request):
    user_choice = request.POST.get('choice')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if user_choice == computer_choice:
        result_message = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_message = "You win!"
    else:
        result_message = "Computer wins!"

    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result_message
    }
    return render(request, 'game/result.html', context)

def play_again(request):
    return redirect('/')

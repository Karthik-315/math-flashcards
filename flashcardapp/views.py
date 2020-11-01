from django.shortcuts import render, redirect
from random import randint

# Create your views here.

def home(request):
    name="Morty"
    return render(request, 'flash_card_intro.html', {'print_name':name})

def app_page(request):
    user_name = request.POST['username']
    return render(request, 'flash_card_app.html', {'player':user_name})

def addition(request):
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    
    user_answer = ''
    result_text = None
    correct_answer = ''
    
    if(request.method == 'POST'):
        user_answer = int(request.POST['answer'])
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        correct_answer = int(old_num_1) + int(old_num_2)
        if(correct_answer == user_answer):
            result_text_1 = "That is Correct! "
            result_text_2 = old_num_1 + " + " + old_num_2 + " = " + str(user_answer)
            state="success"
        else:
            result_text_1 = "That is Incorrect! "
            result_text_2 = old_num_1 + " + " + old_num_2 + " is not " + str(user_answer) + ", it is " + str(correct_answer)
            state="danger"
            
        return render(request, 'addition.html', {
            'result_text_1':result_text_1,
            'result_text_2':result_text_2,
            'state': state,
            'num1':num_1,
            'num2':num_2,
            })
        
    return render(request, 'addition.html', {
        'num1':num_1,
        'num2':num_2,
        })

def subtraction(request):
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    
    user_answer = ''
    result_text = None
    correct_answer = ''
    
    if(request.method == 'POST'):
        user_answer = int(request.POST['answer'])
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        correct_answer = int(old_num_1) - int(old_num_2)
        if(correct_answer == user_answer):
            result_text_1 = "That is Correct! "
            result_text_2 = old_num_1 + " - " + old_num_2 + " = " + str(user_answer)
            state="success"
        else:
            result_text_1 = "That is Incorrect! "
            result_text_2 = old_num_1 + " - " + old_num_2 + " is not " + str(user_answer) + ", it is " + str(correct_answer)
            state="danger"
            
        return render(request, 'subraction.html', {
            'result_text_1':result_text_1,
            'result_text_2':result_text_2,
            'state': state,
            'num1':num_1,
            'num2':num_2,
            })
        
    return render(request, 'subraction.html', {
        'num1':num_1,
        'num2':num_2,
        })
    return render(request, 'subraction.html', {})

def multiplication(request):
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    
    user_answer = ''
    result_text = None
    correct_answer = ''
    
    if(request.method == 'POST'):
        user_answer = int(request.POST['answer'])
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        correct_answer = int(old_num_1) * int(old_num_2)
        if(correct_answer == user_answer):
            result_text_1 = "That is Correct! "
            result_text_2 = old_num_1 + " X " + old_num_2 + " = " + str(user_answer)
            state="success"
        else:
            result_text_1 = "That is Incorrect! "
            result_text_2 = old_num_1 + " X " + old_num_2 + " is not " + str(user_answer) + ", it is " + str(correct_answer)
            state="danger"
            
        return render(request, 'multiplication.html', {
            'result_text_1':result_text_1,
            'result_text_2':result_text_2,
            'state': state,
            'num1':num_1,
            'num2':num_2,
            })
        
    return render(request, 'multiplication.html', {
        'num1':num_1,
        'num2':num_2,
        })
    return render(request, 'multiplication.html', {})

def division(request):
    num_1 = randint(0,10)
    num_2 = randint(1,10)
    
    user_answer = ''
    result_text = None
    correct_answer = ''
    
    #If division yeilds a fraction, skip and reload.
    if(num_1 % num_2 != 0):
        return redirect('division')
    
    if(request.method == 'POST'):
        user_answer = int(request.POST['answer'])
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        correct_answer = int(old_num_1) / int(old_num_2)
        if(correct_answer == user_answer):
            result_text_1 = "That is Correct! "
            result_text_2 = old_num_1 + " / " + old_num_2 + " = " + str(user_answer)
            state="success"
        else:
            result_text_1 = "That is Incorrect! "
            result_text_2 = old_num_1 + " / " + old_num_2 + " is not " + str(user_answer) + ", it is " + str(correct_answer)
            state="danger"
            
        return render(request, 'division.html', {
            'result_text_1':result_text_1,
            'result_text_2':result_text_2,
            'state': state,
            'num1':num_1,
            'num2':num_2,
            })
        
    return render(request, 'division.html', {
        'num1':num_1,
        'num2':num_2,
        })
    return render(request, 'division.html', {})
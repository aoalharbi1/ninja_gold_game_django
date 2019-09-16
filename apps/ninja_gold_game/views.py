from django.shortcuts import render, HttpResponse, redirect
import random, datetime	

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['message'] = ""

    return render(request, "ninja_gold_game/index.html")

def process_money(request):
    which_form = request.POST['which_form']

    if which_form == "farm":
        num = random.randint(10, 20)
        request.session['gold'] += num 
        request.session['message'] = "<li>Earned {} golds from the {} ({})</li>".format(num, which_form, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + request.session['message']
    elif which_form == "cave":
        num = random.randint(5, 10) 
        request.session['gold'] += num
        request.session['message'] = "<li>Earned {} golds from the {} ({})</li>".format(num, which_form, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + request.session['message']
    elif which_form == "house":
        num = random.randint(2, 5) 
        request.session['gold'] += num
        request.session['message'] = "<li>Earned {} golds from the {} ({})</li>".format(num, which_form, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + request.session['message']
    elif which_form == "casino":
        num = random.randint(-50, 50)
        request.session['gold'] += num
        if num < 0:
            request.session['message'] = "<li class='red'>Entered a casino and lost {} golds ... Ouch ({})</li>".format(num, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + request.session['message']
        else:
            request.session['message'] = "<li>Entered a casino and earned {} golds ({})</li>".format(num, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')) + request.session['message']

    return redirect("/")

def reset(request):
    try:
        del request.session['gold']
        del request.session['message']
    except:
        print("Clear")
    finally:
        return redirect("/")
# By Andy Nguyen
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    print("*"*25, "INDEX METHOD", "*"*25)
    if 'words' not in request.session:
        request.session['words'] = []
    print("*"*25, "END INDEX METHOD", "*"*25)
    return render(request, 'session_words_app/index.html')

def add(request):
    print("*"*25, "ADD METHOD", "*"*25)
    if request.method == 'POST':
        time = strftime("%I:%M:%S%p, %B %d %Y", gmtime())
        temp_list = request.session['words']
        temp_list.insert(0,{"word": request.POST['word'], "color": request.POST['color'], "big_font": request.POST['big_font'], "time": time})
        request.session['words'] = temp_list

        print(f"The following have been stored in session:")
        for val in request.session.keys():
            print("\n", val, request.session[val])
        print("*"*25, "END ADD METHOD", "*"*25)
        return redirect('/')
    else:
        print("*"*25, "END ADD METHOD", "*"*25)
        return redirect('/')

def clear(request):
    print("*"*25, "CLEAR METHOD", "*"*25)
    request.session.clear()
    print("Session has been cleared")
    print("*"*25, "END CLEAR METHOD", "*"*25)
    return redirect('/')

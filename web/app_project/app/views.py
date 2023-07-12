from django.shortcuts import render, redirect

def index(request):
    '''Render main page'''
    return render(request, "app/index.html")

def add_data(request):
    if request.method == "POST":
        form = MessageLogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(index)
    form = MessageLogForm()

    return render(request, 'app/add_page.html', {'form': form})



def add_page(request):
    form = MessageLogForm(use_required_attribute=False)
    return render(request, 'app/add_page.html', {'form': form})



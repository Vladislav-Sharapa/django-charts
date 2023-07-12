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


def get_bar_data(request, week) -> JsonResponse:
    '''Get data for bar chart'''

    if Messagelog.objects.filter(date_rcv__week=week).exists():
        instances = Messagelog.objects.filter(date_rcv__week=week)
        instances_count = instances.values('type_doc').annotate(count=Count('type_doc'))

        return JsonResponse({
            "title": "Bar chart",
            "data": {
            "labels": [x['type_doc'] for x in instances_count],
                "datasets": [{
                    "label": 'DOCUMENTS PROCESSED',
                    "data": [x['count'] for x in instances_count],
                    "borderWidth": 1,
                    "backgroundColor": ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],

            }]}
        })
    return HttpResponse("No data for bar chart")
    

def get_line_data(request, week) -> JsonResponse:
    '''Get data for line chart'''

    if Messagelog.objects.filter(date_rcv__week=week).exists():
        instances = Messagelog.objects.filter(date_rcv__week=week)
        instances_count = instances.values('date_rcv').annotate(count=Count('type_doc'))

        return JsonResponse({
            "title": 'Line chart',
            "data": {
            "labels": [x['date_rcv'] for x in instances_count],
            "datasets": [{
                "label": "DOCUMENTS PROCESSED",
                "data": [x['count'] for x in instances_count],
                "backgroundColor": ['yellow', 'aqua', 'pink', 'lightgreen'],
                "borderColor": ['black'],
                "borderWidth": 0.5,
                "pointRadius": 5,
            }],
        },
        })
    
    return HttpResponse("No data for line chart")


def get_pie_data(request, week) -> JsonResponse:
    '''Get data for pie chart'''

    if Messagelog.objects.filter(date_rcv__week=week).exists():
        instances = Messagelog.objects.filter(date_rcv__week=week)
        instances_count = instances.annotate(concatenated=Concat('custom', Value('-'),'pto')).values('concatenated').annotate(count=Count('*'))
    
        return JsonResponse({
            "title": 'pie chart',
            'data': {
            'labels': [x['concatenated'] for x in instances_count],
            'datasets': [{
                'label': "PROCESSED",
                'data': [x['count'] for x in instances_count],
                'backgroundColor': ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
                'borderWidth': 1,
                'borderRadius': 2,
                'hoverOffset': 5,
            }],
            }
        })
    
    return HttpResponse("No data for pie chart")


def get_area_data(request, week) -> JsonResponse:
    '''Get data for area chart'''

    if Messagelog.objects.filter(date_rcv__week=week).exists():
        instances = Messagelog.objects.filter(date_rcv__week=week)
        instances_count = instances.values('declarant_unp').annotate(count=Count('*'))

        return JsonResponse({
            'title': 'Area chart',
            'data': {
            'labels': [x['declarant_unp'] for x in instances_count],
            'datasets': [{
            'label': "PROCESSED",
            'data': [x['count'] for x in instances_count],
            'backgroundColor': ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
            }],
        }
        })
    
    return HttpResponse("No data for area chart")

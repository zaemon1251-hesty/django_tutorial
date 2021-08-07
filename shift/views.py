from django.shortcuts import render, redirect
from .models import employee, schedule
from .forms import shiftForm
from .services import preProcess, StoreShift
import re

# Create your views here.


def index(request):
    result = []
    if request.method == 'POST':
        print(request.POST)
        lines = []
        lines.append(request.POST['type'])
        lines.append(request.POST['name'])
        if any(request.POST['type'] == t for t in ('submit', 'cancel')):
            if all(request.POST[col] != '' for col in ('date', 'start_at', 'end_at')):
                dt = str(request.POST['date']) + ' ' + \
                    str(request.POST['start_at']) + \
                    '-' + str(request.POST['end_at'])
                lines.append(dt)
            else:
                result.append('worng form')
                return render(request, 'shift/index.html', {'form': shiftForm, 'result': result})
        print('lines')
        print(lines)
        TERM, K, queries = preProcess(lines)
        store = StoreShift(K, TERM)
        for q in queries:
            result.append(store.query_process(q))
    else:
        result = None
    return render(request, 'shift/index.html', {'form': shiftForm, 'result': result})

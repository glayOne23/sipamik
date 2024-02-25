from django.shortcuts import render
# from apps.services.decorators import group_required
from django.contrib import messages
from django.urls import reverse
from json import dumps





# =====================================================================================================
#                                               LOAD PAGE
# =====================================================================================================

def index(request):
    context = {}
        
    # ===[Data]===    
    context['sidebar'] = 'dashboard'

    # ===[Render Template]===
    return render(request, 'adminpage/index.html', context)
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
# Create your views here.
def home(request):
    # trans = _('hello')
    trans = translate(language='ja')
    context = {
        'trans':trans
    }
    return render(request, 'index.html', context)
    
def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

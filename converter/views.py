from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.html import mark_safe
from .forms import TextToHtmlForm

def text_to_html(request):
    converted_html = ''
    if request.method == 'POST':
        form = TextToHtmlForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['text_input']
            converted_html = mark_safe(input_text)  # Convert text to HTML safely

    else:
        form = TextToHtmlForm()

    return render(request, 'converter/text_to_html.html', {'form': form, 'converted_html': converted_html})

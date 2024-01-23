from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import markdown2

from . import util

class FormCreate(forms.Form):
    title_page = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': 'title-page-input', 'placeholder': 'Enter a title', 'autocomplete': 'off'}))
    content_page = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'content-page-input', 'placeholder': 'Enter content in Markdown format', 'autocomplete': 'off'}))
    
class FormEdit(forms.Form):
    content_page = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'content-page-input', 'autocomplete': 'off'}))
    

def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('q', '')
        entry_content = util.get_entry(search_query)
        
        if entry_content is None:
            return HttpResponseRedirect(reverse('encyclopedia:search', args=[search_query]))
        else:
            return HttpResponseRedirect(reverse('encyclopedia:page', args=[search_query]))
    else:
        
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    

def page(request, name):
    # Utilizo la función get_entry para obtener el contenido de la entrada
    entry_content = util.get_entry(name)

    # Si la entrada no existe, Lanzo una excepción Http404
    if entry_content is None:
        """ raise Http404("Paila Intenta Otra cosa") """
        return render(request, "encyclopedia/error.html", )    
    # MD to HTML
    entry_html_content = markdown2.markdown(entry_content)

    # Renderizo la página utilizando el contenido obtenido y el nombre de la entrada
    return render(request, "encyclopedia/page.html", {
        "name": name,
        "content": entry_html_content
    })
    

def search(request, query):
    matching_entries = []
    matching_entries = [entry for entry in util.list_entries() if query.lower() in entry.lower()]

    return render(request, "encyclopedia/pageSearch.html", {
                "newlist": matching_entries,
                "name": query
            } )

def create(request):
    if request.method == "POST":
        form = FormCreate(request.POST)
        if form.is_valid():
            Title = form.cleaned_data["title_page"]
            entries = util.list_entries()
            if Title.lower() in map(str.lower, entries):
                #error message
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    'message': 'An entry with that title already exists.'
                })
            else:           
                Content = form.cleaned_data["content_page"]
                util.save_entry(Title.capitalize(), Content)
                return HttpResponseRedirect(reverse('encyclopedia:page', args=[Title]))
        else:
            return render(request, "encyclopedia/create.html", {
                    "form": form,
                    'message': 'Verifica tu contenido.'
                })
        
    else:
        return render(request, "encyclopedia/create.html", {
                "form": FormCreate()
            })


def edit(request, title):
    if request.method == "POST":
        form = FormCreate(request.POST)
        if form.is_valid():
            Content = form.cleaned_data["content_page"]
            util.save_entry(title.capitalize(), Content)
            return HttpResponseRedirect(reverse('encyclopedia:page', args=[title]))
        else:           
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "form": form,
                'message': 'Verifica tu contenido.'
            })
    else:
        content = util.get_entry(title)
        
        initial_data = {'content_page': content} if content else {}
        form = FormEdit(request.POST or None, initial=initial_data)

        
        return render(request, "encyclopedia/edit.html", {
                "title": title,
                "form": form,
            })
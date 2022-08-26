from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class GamesPage(ListView):
    model = Game
    context_object_name = 'game'
    template_name = 'games/gamepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Games'
        context['url_game'] = 'You can buy here'
        return context


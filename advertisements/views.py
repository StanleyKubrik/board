from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def advertisement_prices(request):
    return render(request, 'advertisements/advertisement_prices.html')


class Advertisement(View):
    count = 0
    answer = 'Thank you for request! Requests: '
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]

    def get(self, request):
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': self.advertisements})

    def post(self, request):
        hit = request.session.get('hit')
        if not hit:
            request.session['hit'] = 0
        else:
            request.session['hit'] += 1
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': self.advertisements,
                                                                          'answer': self.answer + str(hit)})


class Contacts(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Contacts our organization!'
        context['title'] = 'Contacts'
        context['description'] = '\nAddress: ...' \
                                 '\nPhone: ...' \
                                 '\nTelegram: ...' \
                                 '\nInstagram: ... '
        return context


class About(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Information about us!'
        context['title'] = 'About'
        context['description'] = 'We are small bakery with delicious cupcakes, cakes, macaroons etc.'
        return context

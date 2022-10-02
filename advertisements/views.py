from django.shortcuts import render
from django.views.generic import TemplateView


def advertisement_list(request):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})


def advertisement_prices(request):
    return render(request, 'advertisements/advertisement_prices.html')


class About(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'About our organization!'
        context['title'] = 'Information'
        context['description'] = 'Something information about our organization.' \
                                 '\nAddress: ...' \
                                 '\nPhone: ...' \
                                 '\nTelegram: ...' \
                                 '\nInstagram: ... '
        return context

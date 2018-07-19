from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import OptimumDNA, Individual
from .calculations import *


def index(request):
    latest_opt_list = OptimumDNA.objects.all()
    # template = loader.get_template('genetic/index.html')
    context = {'latest_opt_list': latest_opt_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'genetic/index.html', context)


def detail(request, optimumDNA_id):
    try:
        opt = OptimumDNA.objects.get(pk=optimumDNA_id)
    except OptimumDNA.DoesNotExist:
        raise Http404("OptimumDNA does not exist")

    if len(opt.DNA) == 0:
        return HttpResponse("Length of the OptimumDNA is zero. So, unfortunately, there is nothing to show.")

    n_gen = 30
    pop_size = 1000
    mut_percentage = 0
    see_n_best = 20
    all_chars = string.ascii_lowercase + " "

    # Initialize the population
    population = create_population(pop_size, opt.DNA, all_chars)

    # Training
    population, sorted_sentences, sorted_scores, bests = train_population(population, n_gen, opt.DNA,
                                                                          mut_percentage, all_chars, see_n_best)

    return render(request, 'genetic/detail.html', {'opt': opt, 'best_of_population': bests,
                                                   'n_gen': n_gen, 'opt_len': len(opt.DNA),
                                                   'pop_size': pop_size})


def greetings(request):
    return HttpResponse("Hello, world. You're at the genetic greetings page.")

def results(request, optimumDNA_id):
    opts = OptimumDNA.objects.all()
    response = '\n'.join([o.DNA for o in opts])

    return HttpResponse(response)

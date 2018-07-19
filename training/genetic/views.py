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

    n_gen = 10
    pop_size = 1000
    all_chars = string.ascii_lowercase + " "
    mutation_percentage = 0
    see_n_best = 20

    population = create_population(pop_size, opt.DNA, all_chars)
    list_of_scores, sorted_scores, sorted_sentences = [], [], []

    for i in range(n_gen):
        # Selection (by fitness scores)
        list_of_scores, prob_dist = selection(population, opt.DNA)
        sorted_scores, sorted_sentences = sort_together(list_of_scores, population)

        # Reproduction (matching, crossover and mutation)
        avg_generation_score, new_population = reproduce(population, list_of_scores, prob_dist, all_chars,
                                                         mutation_percentage)
        # Replace
        population = new_population


    list_of_scores, prob_dist = selection(population, opt.DNA)

    best_of_population = zip(sorted_sentences[:see_n_best], sorted_scores[:see_n_best])

    for i in range(5):
        print(sorted_scores[i],sorted_sentences[i])

    return render(request, 'genetic/detail.html', {'opt': opt, 'best_of_population': best_of_population,
                                                   'n_gen':n_gen, 'opt_len': len(opt.DNA),
                                                   'pop_size': pop_size})


def greetings(request):
    return HttpResponse("Hello, world. You're at the genetic greetings page.")


def results(request, optimumDNA_id):
    opts = OptimumDNA.objects.all()
    response = '\n'.join([o.DNA for o in opts])
    print(response)

    return HttpResponse(response)

    # response = "You're looking at the results of population with OptimumDNA %s."
    # return HttpResponse(response % optimumDNA_id)

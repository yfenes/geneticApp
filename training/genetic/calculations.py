import random, string
# import numpy as np
from numpy import mean
from numpy.random import choice


def create_population(pop_size, opt_dna_string, all_chars):
    dna_length = len(opt_dna_string)
    population = []

    for i in range(pop_size):
        sentence = ''.join(random.choice(all_chars) for _ in range(dna_length))
        population.append(sentence)

    return population


def fitness(sen1, sen2):
    if len(sen1) != len(sen2):
        print("Error, length of sentences must be the same.\nSentence 1: " + sen1 + "\nSentence 2: " + sen2)
        return -1, -1

    score = 0
    for ind, elem in enumerate(sen1):
        if sen2[ind] == elem:
            score += 1
    percentage_score = 1.0 * score / len(sen1)
    return score, percentage_score


def selection(population, real_sentence):
    current_total_score = 0
    list_of_scores = []

    for sentence in population:
        score, percentage_score = fitness(real_sentence, sentence)
        current_total_score += score
        list_of_scores.append(score)

    # Try catch for zero division error
    try:
        prob_dist = [x / current_total_score for x in list_of_scores]
    except ZeroDivisionError:
        prob_dist = [1] * len(list_of_scores)
    return list_of_scores, prob_dist


def crossover(sen1, sen2):
    pos = int(random.random() * len(sen1))
    return sen1[:pos] + sen2[pos:]


def mutation(sentence, percentage, all_chars):
    if percentage == 0:
        return sentence

    for ind, elem in enumerate(sentence):
        rand = random.random() * 10000
        if rand <= percentage * 100:
            rand_char = ''.join(random.choice(all_chars))
            sentence = sentence[:ind] + rand_char[0] + sentence[ind + 1:]

    return sentence


def reproduce(population, list_of_scores, prob_dist, all_chars, mutation_percentage=0):
    avg_generation_score = mean(list_of_scores)
    new_population = []
    # All draws at once for efficiency
    draw = choice(population, 2 * len(population), p=prob_dist)

    for i in range(len(population)):
        child = crossover(draw[2 * i], draw[2 * i + 1])
        child = mutation(child, mutation_percentage, all_chars)
        new_population.append(child)

    return avg_generation_score, new_population


def sort_together(list1,list2):
    list1, list2 = zip(*sorted(zip(list1, list2), reverse=True))
    return list1, list2
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class OptimumDNA(models.Model):
    DNA = models.CharField(max_length=100)
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.DNA

class Individual(models.Model):

    optimum_DNA = models.ForeignKey(OptimumDNA, on_delete=models.CASCADE)
    DNA = models.CharField(max_length=100)

    # TODO set score to number of matches with optimum DNA.
    # Score = number of gene match with optimum DNA
    score = models.IntegerField(default=0)

    # Precision = Score / DNA_length
    precision = models.FloatField(
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],default=0
    )


    def __str__(self):
        return self.DNA

    # TODO the argument opt always must be the OptimumDNA associated with this Individual
    def fitness(self, optDNA):
        sen1 = self.DNA
        sen2 = optDNA

        if len(sen1) != len(sen2):
            print("Error, length of sentences must be the same.\nSentence 1: " + sen1 + "\nSentence 2: " + sen2)
            return -1, -1
        score = 0
        for ind, elem in enumerate(sen1):
            if sen2[ind] == elem:
                score += 1
        percentage_score = 1.0 * score / len(sen1)
        return score, percentage_score



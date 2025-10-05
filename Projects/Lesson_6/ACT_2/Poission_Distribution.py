import scipy.stats as stats
prob=stats.poisson.pmf(6,10)
print("The probability of raining for 6 days is:",prob)
prob2=stats.poisson.pmf(12,10)+stats.poisson.pmf(13,10)+stats.poisson.pmf(14,10)
print("The probability of raining for 12-14 days is:",prob2)
# Projects about genetic algorithms
IncrementnumberofA.py Increment the number of letters 'A' in a population of 200 individuals using different methods; the first selection method is Steady State Selection: Select the 100 first individuals in the population (the best); the second method is Tournament Selection: Compare 2 individuals selected randomly, the best is selected for the new population, and the loser is eliminated.

To generate the new population I use 3 different methods:
1.- Single Point Crossover: A point on both parents' chromosomes is picked randomly, and designated a 'crossover point'. Bits to the right of that point are swapped between the two parent chromosomes. This results in two offspring, each carrying some genetic information from both parents. 
2.- Double Point Crossover: In two-point crossover, two crossover points are picked randomly from the parent chromosomes. The bits in between the two points are swapped between the parent organisms. 
3.- Uniform Crossover: In uniform crossover, typically, each bit is chosen from either parent with equal probability. Other mixing ratios are sometimes used, resulting in offspring which inherit more genetic information from one parent than the other. 

# Traveling Salesman Problem
For this problem is used the Steady State Selection method, to create the new population; I used the Partially Mapped Crossover (PMX) method and used the inverted exchange mutation on each population to improve the results.


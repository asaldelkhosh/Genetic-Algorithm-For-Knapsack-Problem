# Genetic algorithm for solving Knapsack problem

Solving Knapsack Problem with Genetic Algorithm.
The basic idea behind the Genetic Algorithm is to start with some candidate Individuals (solutions chosen at random) called Population. The initial population is the zeroth population, which is responsible for the spinning of the First Generation. The First Generation is also a set of candidate solutions that evolved from the zeroth generation and is expected to be better.

To generate the next generation, the current generation undergoes natural selection through mini-tournaments, and the ones who are fittest reproduce to create offspring. The offspring are either copies of the parent or undergo crossover where they get a fragment from each parent, or they undergo an abrupt mutation. These steps mimic what happens in nature.

<p align="center">
  <img src="https://user-images.githubusercontent.com/4745789/156874170-608cd9a4-6241-4882-b123-658d14a64c89.png" width="500" />
</p>

## Runtime

The run-time complexity of the Genetic Algorithm to generate a high-quality solution for the Knapsack problem is not exponential, but it is polynomial. If we operate with the population size of PAnd iterate till G generations, and F is the run-time complexity of the fitness function, the overall complexity of the algorithm will be O(P.G.F).

Given that the parameters are known before starting the execution, you can predict the time taken to reach the solution. Thus, we are finding a non-optimal but high-quality solution to the infamous Knapsack problem in Polynomial Time.

While discussing the process of Genetic Algorithm, we saw that there are multiple parameters that can increase or decrease the efficiency of the algorithm; a few factors include

## Resource

[Genetic Knapsack](https://arpitbhayani.me/blogs/genetic-knapsack).

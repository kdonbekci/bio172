# bio172
## Course repo for BIO172 - Ecological Dynamics: Theory and Applications
Will be used for the life history and dispersion project. Structured from 1, ..., N for ease of readability.

## Background

Life histroy traits are the important factors that shape the life of an individual organism. For a given species, important variables could be the **age**, **size**, **beak length**, **size in RAM**, ...

These variables are then used to model vital rates, survival and reproduction, of populations. In this project, we are examining the effects of dispersion on population growth rate.

## Theory

For a simple model that takes only **age** into account, we can define the vital rates as:

$p(a):$ survival rate from age $a$ to $a+1$.

$l(a):$ cumulative survival from birth to age $a$, e.g. $l(4) = p(2) \times p(3)$ ($p(1) = 1$).

$f(a):$ fertility at age $a$.

Using these rates, we can construct a square matrix $A$, called a [Leslie matrix](https://en.wikipedia.org/wiki/Leslie_matrix "Wikipedia article on Leslie matrix") to model the population. The matrix will be of shape $D\times D$ where $D$ is the maximum age in our population.


[logo]: https://wikimedia.org/api/rest_v1/media/math/render/svg/af866391f240e7575bf1436ef4e67aaf4cf9b6d4 "Leslie matrix"




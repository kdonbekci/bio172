## Goals: 
1. Generate [Leslie matrices](https://en.wikipedia.org/wiki/Leslie_matrix), used for modeling growth of populations, from experimental field data species census.
2. Caclulate important model characteristics such as net [reproductive rate](https://en.wikipedia.org/wiki/Net_reproduction_rate) through conventional linear algebra methods, more specifically eigen decomposition of the leslie matrix. 
3. Appproximate the model characteristics through other, less computationally intensive methods. 

## Approach:
The methods to derive some of the most important descriptors of how a species is growing can get computationally infeasible with a lot of data, since many of them rely on matrix decompositions. In this project, we attemted to approximate these descriptors through other methods that involved some assumptions and a lot of calculus :). 


## Outcome:
We were able to approximate most of the descriptors with good accuracy and confidence without relying on expensive matrix math. Upon reflection about what the Leslie matrix stands for it is possible to see how similar approaches can enhance and dramatically reduce the computational complexity of the analysis of growth models in very different domains than biology such as in finance. 
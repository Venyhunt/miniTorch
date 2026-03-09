One of the key concepts of building a neural netwrok is Automatic Differenciation,
I had learned about it in a vague way in our Deep learning classes.
Though it was in a background math sort of way, but now that I am building an engine of my own,
I realised I need to understand these concepts a little more deeply.

so here I go:

Automatic Differenceation is onw of the key concepts that has allowed for the birth and implementation of all of Neural Netwroks.
It's a type of differenciation or technique that allows the chain rule to work, it's the base of forward and backward propagation.

We are counting derivatives automatically in a recursive order, it's the main reason why reverse mode is so efficient for loss count.
Foward mode gives multiple inputs and runs the whole rule for each of those derivatives, reverse mode uses those internmediate nodes
and thier derivatives value and recursively passes the gradients from children(output nodes) to parents(inout node) only once.

Therefore we can count loss in onw sweep of the network.

the next questions are:
why not any other type or techniques of differentiation?
what's computation graph?


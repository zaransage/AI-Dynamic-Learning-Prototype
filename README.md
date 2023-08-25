# AI-Dynamic-Learning-Prototype
A set of prototypes for dynamic AI learning.

## Overview and Introduction:
I have studied machine learning and AI for almost 7 years now and I have a few ideas I want to play around with. Mainly, I want to see if I can reduce some of the inflexability surrounding both the training and updating process of matrix (and maybe tensor) based algebreic state machines.

I have no doubt that perhaps, someone else has run these to ground or maybe has substantially more experience which would be able to refute or confirm the ideas I am pondering in this repo.
However, I find the ideas and problems hit my mind often enough to compel me to action, even if ultimately foolish, so long as I learn something useful from the experience.

I will make some of my assertions below, with full understanding that perhaps I am 'missing' something in my thought process; I invite friendly discourse on the matter.

## Idea and Hypotheses:
The first major assertion here is that there is an ultimate limit to the use of a matrix or set of large matricies in order to enable neural networks to function as they do today.

I will lay out some of my observations and some of the alternatives I aim to try and prototype here.

1. A matrix has a fixed size one the initial trainings is complete.
2. A matrix needs to compute every field to handle the back-propogation process used to update the weights and biases stored in each vector.
3. TThe process to do this is inherently based on looping over and over these fields. This is true, to the best of my knowledge, even with very fast, C-Based imlementations of matrix multiplication.

These items together produce two major concerns with respect to AI:

1. You will eventually reach an intractable level of loops which make training almost impossible
2. You are stuck in a condition where your AI model cannot learn without first shutting down, reprocessing all the data through back propogation and then starting back up.

While there are some mechanisms to side step or improve upon some of these, every method I have seen ultimately boils down to having either of these limitations.
For exaple, even small batch processing of an AI model still seems to need the AI model to shut down in memory before that data can be used.

Along side of this set of concerns, is the topic of how such a behavior as 'back propogation' might actually work inside biological organims like the brain.
To me, while I don't disagree that a type of back propogation might exist, I think the fact that the neurons in the case of biology are able to have their weights changes through sheer use.

As an example, when a being's brain is first brought online, (born) you could potentially think of this as though the neural network is 'randomly initialized'. That is, many behaviors of children are random actions which build into stronger connections in the brain.
In this case, the brain is not looking for a loop per se, to update a weight. It is the very act that when a child performs an action, a set of neural connections draw upon resources in order to fire.

When a behavior in a baby causes a response, those weights are updated, whether positive or negitive. It is the very act of the sensory input of one set of biological processes, from one neuron to the next which induce some neurons to grow and not others.
While this is an unoubted simplification, I use this notion that there is a biological reaction causing the strength or weakness of connections as the replacement for what we use 'back propogation' for today in these matrices.

In this case, we then look at trying to make each cell in the matrix or a replacement container of some kind, respond online to an input or an observation from it's immediate neighbor into itself, upon which a down stream neuron also makes this adjustment.

The fact that you get a weight set back to each cell in the table as a calculation in a matrix today, is because the individual cell in the matrix cannot directly 'inform' the cell next to it. An external process (the thing doing the loop) has to act on it.

I use this simple model to explain why there might always be an upper limit to the actual use of matrices in their current way with a looping mechanism to determine the weights to apply. The very fact that a weight is physically influenced by the response a living organisim gets produces an update behavior without the need for the same direct back propogation we need in a matrix today.

### We now come to my hypotheses:

1. If a neuron is able to watch only the state of a neuron before it and advertise it's state to a neuron or neurons which surround it, the same partial derivitive which is handled by manually looping over all fields in a matrix could be handled on a per-neuron basis.
2. The value of this particular behavior is that the learning and 'thinking' part of the model would update in more real time and in some cases, could converge on a 'good enough' answer before the whole network is actually updated.

In this idea, the individual neurons behave almost like a message queue, in which each neuron is 'aware' of the partial derivitve activation function in use and can infer what that change needs to be by observing that change in the neuron which proceeds it.
This would let all of neurons update in real time, in memory, without needing to turn off the model.

Put another way, each cell has it's own loop =, which only looks at the cell above it and the neuron's machinery is only responsible for applying the derivitive change to it's own state and then making that information available to the next neuron.

## Possible Alternatives:
1. It is entirely possible that the trend of micro batches will permit a model to 'partially' go offline in some way. That is, in memory, where the active state machine lives, if there is a secondary neural network which can 'reach out' to another network loaded into memory indipendently from the first, this could help alleviate some of these issues.

## Notes and Discussion:
  1. Now this obviously begins to get into a world where you are making each cell in a matrix it's own small compute object. That is, you are taking the logic out of the 'for loop' handling updating a matrix and moving it into the job of the neuron (partially).
  2. Naturally, this is going to induce latency in other areas and might not be 'faster' per se. However, the very fact that there is a basis to allow an acive learning process to update these states means you might be able to first train the model in the traditional sense, then 'map' each of those fields into their own neuron to improve it.
  3. Saving the 'state' of the neuron which has been learned could be slow or intractable. You would have to get each of these neurons in some way, either with another looping process or on it's own, to dump it's state into table somewhere or saved as an object out of memory.
  4. Queues and lambda functions (like in memory, function as a service devices) could be a possible avenue to prototype this kind of neural network adjustment, since scale is likely going to be needed to make this kind of neuron work in the beginning.
  5. This idea may not fully remove the delay between the 'thinking' and 'learning' process but it might make the process more of a context switch like biological life forms hold today, verses the complete shut down it takes to load a new trained model today.
  6. There is a possible additional concern that updating the activation functions or having more than one activation function needed in a neuron could be a difficult task. The tradeoff might be that more specificity in the coupling of what the neuron's job is might make the active learning process easier.
     

## References:

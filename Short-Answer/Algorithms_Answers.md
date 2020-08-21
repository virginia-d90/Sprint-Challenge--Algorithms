#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). As size of input increases the runtime will grow at the same rate.
a=0
a=4
a = 8

a=0
a=16
a=32
a=48
a=64

b)O(n log n). The outer loop will run O(n) times. The inner while loop will run O(log n) because of the incrementing of the j.


c)O(n). The function is called n times before reaching its basecase. The input bunnies will match the number of times the function is recursivly called.

## Exercise II

1. Start by finding the middle floor and drop an egg. 
2. If the egg breaks you know that the floor is too high. If not it is too low.
3. Repeat step one on the lower or upper half of the floors depending on the outcome
4. The maximum highest floor will be where two consecutive floors are tested and the lower does not break and the higher does break.

This is implementing a binary search algorithm which has a runtime complexity of O(log n)


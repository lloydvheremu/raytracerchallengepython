# The Ray Tracer Challenge 

## This project follows the book by Jamis Buck
### A Test-Driven Guide to My First 3D Renderer in Python

#### The tests are posed as Cucumber scenarios and I implement them using python's unittest module

It’s structured like any Cucumber scenario, but describes low-level API
interactions:
- It begins with two assumptions (“Given…And”), which must be true to
start. These use left arrows (←) to assign two arrays to two variables, a
and b.
- After everything has been initialized, an action occurs (“When”). The
result of this action is what is to be tested. Note that this also uses the
left arrow, assigning the result of concatenating a and b to another
variable, c.
- Finally, an assertion is made (“Then”), which must be true. This uses the
equals operator (=) to assert that the variable c is equal to the given
array.

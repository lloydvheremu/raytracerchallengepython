# The Ray Tracer Challenge 

## This project follows the book by Jamis Buck
### A Test-Driven Guide to My First 3D Renderer in Python

#### The tests are posed as Cucumber scenarios and I implement them using python's unittest module

Typically, Cucumber is used to describe high-level interactions between a
user and an application, but the tests in this book use it differently. Here,
you’ll see it used to describe lower-level interactions, like how various
inputs to a specific function might affect the function’s output. This lets the
book walk you through the construction of an API, step by step, rather than
just showing you the high-level behavior that you need to try to emulate. For
example, consider the following hypothetical specification which describes
the behavior of concatenating two arrays.

- `Scenario: Concatenating two arrays should create a new array`
- `Given a ← array(1, 2, 3)`
- `And b ← array(3, 4, 5)`
- `When c ← a + b`
- `Then c = array(1, 2, 3, 3, 4, 5)`

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

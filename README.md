# Arkhn DevOps exercise
# Moisan Jocelyn

## STEP 1: A small python program

Given a string composed of the characters `(`, `)`, `[`, `]`, `{`, `}`, you need to tell if this string is balanced or not. What we call a balanced string is one where all the brackets are closed in the right order.

For instance, `([]){}` is balanced, whereas `([)]{}` or `(()` are not.

The input will whether come from the user launching the script with -d "input" or, if no input is provided (-d ""), it will query a `generator` service which was provided. You can also query the generator using "curl -X POST localhost:5001/solve".

You can launch the solver and the generator server using :
```shell
python3 solver.py
python3 generator-server/src/server.py
python3 generator-server/src/server.py & python3 solver.py
```
and then query it as follows:

```shell
$> curl -d '{{[()]}}' localhost:5001/solve
$> curl -d '(((]' localhost:5001/solve
$> curl -X POST localhost:5001/solve
```
The program will print the input and if it was valid or not, showing the first character that was not valid on this instance.

## STEP 2: Dockerizing the program

The goal of this step is to write a Dockerfile in order to containerize both python applications (`generator` and `solver`). Use the following to test the dockerfiles :

```shell
$> docker build -t generator ./generator-server/src
$> docker run -p 5000:5000 -d generator
$> docker build -t solver .
$> docker run -p 5001:5001 -d solver
$> curl -d '{{[()]}}' localhost:5001/solve
$> curl -d '(((]' localhost:5001/solve
$> curl -X POST localhost:5001/solve
```

The two dockerfiles work independently. This means if the solver is launched on docker, and you have the generator running locally, the whole program works. If the generator is launched on docker, and you have the solver running locally, the whole program works as well.
What I have not done is the communication between solver and generator inside docker.

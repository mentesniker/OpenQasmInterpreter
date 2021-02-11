# OpenQasmInterpreter (oqi)

This package interprets a .qasm 2.0 file and then outputs the results to the console. All of the executions are made using the qasm simulator. Moreover you can specify different options to run your circuit. 

To just run your .qasm file you'll have to run:

```{r test-python, engine='bash'}
oqi filename
```

Additionally if you want to see and run your circuit you can execute:
```{r test-python, engine='bash'}
oqi filename d
```

Finally if you want to run your circuit **n** number of times you can specify the repetitions:
```{r test-python, engine='bash'}
oqi filename d n
```
or
```{r test-python, engine='bash'}
oqi filename n
```

In any case the output will include something of the form:
```{r test-python, engine='bash'}
The results are: {'bits': numberOfMeasurements, ...}
```

## Installation
Install it with the pip package manager:
```{r test-python, engine='bash'}
pip install oqi
```

## Features

Custom errors:

![image](screenshots/errors.png)

Draw and run your circuits:

![image](screenshots/draw.png)

## Acknowledgements

The token analyser and many other things needed in order to run the interpreter came from the [qiskit repo](https://github.com/Qiskit). My contribution was to create the pip package and some wrapping in order to run their interpreter.

# 0x02. Python - import & modules
This is an introductory project in Python import and modules
## File Descriptions
* [0-add.py](0-add.py) - imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
  * should not be executed when imported
```
guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py
guillaume@ubuntu:~/0x02$
```
* [1-calculation.py](1-calculation.py) - imports functions from the file `calculator_1.py` and uses all of its functions
  * should not be executed when imported
```
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
```
* [2-args.py](2-args.py) - prints the number of and the list of its arguments.
  * The output should be:
    * Number of argument(s) followed by `argument` or `arguments`, followed by
    * `:` (or `.` if no argument where passed) followed by
    * a new line, followed by (if at least one argument)
    * one argument per line:
      * the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
  * should not be executed when imported
```
guillaume@ubuntu:~/0x02$ ./2-args.py
0 argument.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
guillaume@ubuntu:~/0x02$
```
* [3-infinite_add.py](3-infinite_add.py) - prints the result of the addition of all arguments
  * should not be executed when imported
```
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89
-162
guillaume@ubuntu:~/0x02$
```
* [4-hidden_discovery.py](4-hidden_discovery.py) - prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc)
  * print only names that do not start with `__`
  * should not be executed when imported
```
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_holberton
print_school
guillaume@ubuntu:~/0x02$
```
* [5-variable_load.py](5-variable_load.py) - imports the variable `a` from the file `variable_load_5.py` and prints its value.
  * should not be executed when imported
```
guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$
```
### Advanced

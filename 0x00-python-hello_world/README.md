# 0x00. Python - Hello, World
An introductory project on Python.
## File Descriptions
* [0-run](0-run) - a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.
```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Holberton School
guillaume@ubuntu:~/py/0x00$
```
* [1-run_inline](1-run_inline) - a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`.
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Holberton School: 98
guillaume@ubuntu:~/py/0x00$
```
* [2-print.py](2-print.py) - a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
* [3-print_number.py](3-print_number.py) - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
  * not allowed to cast the variable number into a string
  * code must be 3 lines long
  * have to use the [(new print formatting)](https://pyformat.info/#number)
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```
* [4-print_float.py](4-print_float.py]) - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.
  * not allowed to cast `number` to a string
  * have to use the [(new print formatting)](https://pyformat.info/#number)
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```
* [5-print_string.py](5-print_string.py) - complete the [source code]() in order to print a string stored int he variable `str` three times, followed by a new line, followed by its first 9 characters and a new line.
  * not allowed to use any loops or conditional statements
  * program should be maximum 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$
```
* [6-concat.py](6-concat.py) - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) in order to print `Welcome to Holberton School!`
  * not allowed to use any loops or conditional statements
  * have to use the variables str1 and str2 in your new line of code
  * program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$
```
* [7-edges.py](7-edges.py) - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py) such that:
  * `word_first_3` contains the first 3 letters of the variable `word`
  * `word_last_2` contains the last 2 letters of the variable `word`
  * `middle_word` contains the value of the variable `word` without the first and last letters
  * not allowed to use any loops or conditional statements
  * program should be exactly 8 lines long
```
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$
```
* [8-concat_edges.py](8-concat_edges.py) - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) in order to print `object-oriented programming with Python`, followed by a new line.
  * not allowed to use any loops or conditional statements
  * program should be exactly 5 lines long
  * not allowed to create new variables
  * not allowed to use string literals
```
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$
```
* [9-easter_egg.py](9-easter_egg.py) - Python script that prints "The Zen of Python", by TimPeters, followed by a new line.
  * script should be maximum 98 characters long
```
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
```
### Advanced
* [100-write.py](100-write.py) - Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
  * Use the function `write` from the `sys` module
  * not allowed to use `print`
  * script should print to `stderr`
  * script should exit with the status code `1`
```
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$
```
* [101-compile](101-compile) - a script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`. The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Holberton School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$
```
* [102-magic_calculation.py](102-magic_calculation.py) - Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
 3		0 LOAD_CONST               1 (98)
              	3 LOAD_FAST                0 (a)
              	6 LOAD_FAST                1 (b)
              	9 BINARY_POWER
             	10 BINARY_ADD
             	11 RETURN_VALUE
```

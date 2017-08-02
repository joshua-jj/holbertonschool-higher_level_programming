# 0x00. Python - Hello, World
An introductory project on Python.
## File Descriptions
* *0-run* - a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.
```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Holberton School
guillaume@ubuntu:~/py/0x00$
```
* *1-run_inline* - a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`.
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Holberton School: 98
guillaume@ubuntu:~/py/0x00$
```
* *2-print.py* - a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
* *3-print_number.py* - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
  * not allowed to cast the variable number into a string
  * code must be 3 lines long
  * have to use the [(new print formatting)](https://pyformat.info/#number)
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```
* *4-print_float.py* - complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.
  * not allowed to cast `number` to a string
  * have to use the [(new print formatting)](https://pyformat.info/#number)
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```
* *5-print_string.py* - complete the [source code]() in order to print a string stored int he variable `str` three times, followed by a new line, followed by its first 9 characters and a new line.
  * not allowed to use any loops or conditional statement
  * program should be maximum 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$
```

# Python - if/else, loops, functions


---
## 📌 Project Tasks

| #   | Task Title                                                                 |
|-----|-----------------------------------------------------------------------------|
| 0   | [Positive anything is better than negative nothing](0-positive_or_negative.py) |
| 1   | [The last digit](1-last_digit.py)                                          |
| 2   | [I sometimes suffer from insomnia...](2-print_alphabet.py)                 |
| 3   | [When I was having that alphabet soup...](3-print_alphabt.py)              |
| 4   | [Hexadecimal printing](4-print_hexa.py)                                    |
| 5   | [00...99](5-print_comb2.py)                                                |
| 6   | [Inventing is a combination of brains...](6-print_comb3.py)               |
| 7   | [islower](7-islower.py)                                                    |
| 8   | [To uppercase](8-uppercase.py)                                             |
| 9   | [There are only 3 colors...](9-print_last_digit.py)                        |
| 10  | [a + b](10-add.py)                                                         |
| 11  | [a ^ b](11-pow.py)                                                         |
| 12  | [Fizz Buzz](12-fizzbuzz.py)                                                |

## 📘 Python – General Concepts (Quick Review)

# 🔹 Why is indentation important in Python?

Indentation defines the **structure** of the code. Python uses it to group blocks (e.g. in functions, loops, conditionals). Incorrect indentation leads to errors.

---

# 🔹 How to use `if`, `if ... else` statements?

```python
if condition:
    # do something
elif other_condition:
    # do something else
else:
    # fallback
````

Use them to control the **flow** based on conditions.

---

## 🔹 How to use comments?

```python
# This is a comment
```

Use comments to explain your code. Python ignores lines starting with `#`.

---

# 🔹 How to assign values to variables?

```python
x = 10
name = "Alice"
```

Use `=` to assign values to variables. Python is dynamically typed.

---

# 🔹 How to use `while` and `for` loops?

```python
while condition:
    # repeat while true

for i in range(5):
    # repeat 5 times
```

Use loops to **repeat code** either while a condition is true (`while`) or over a sequence (`for`).

---

# 🔹 How to use `break` and `continue` statements?

* `break`: exits the loop entirely.
* `continue`: skips the current iteration and continues with the next.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

# 🔹 How to use `else` clauses on loops?

You can attach an `else` to a loop; it runs **only if the loop was not broken** by `break`.

```python
for i in range(5):
    print(i)
else:
    print("Loop finished")
```

---

# 🔹 What does the `pass` statement do?

`pass` does nothing. It's a placeholder when a statement is syntactically required.

```python
def my_function():
    pass
```

---

# 🔹 How to use `range`?

```python
range(start, stop, step)
```

Generates a sequence of numbers. Often used in `for` loops.

Example:

```python
for i in range(1, 5):
    print(i)  # prints 1 to 4
```

---

# 🔹 What is a function and how do you use functions?

A function is a reusable block of code.

```python
def greet(name):
    return "Hello " + name
```

Call it with `greet("Alice")`.

---

# 🔹 What does a function return if it has no `return`?

If no `return` is used, the function returns `None` by default.

```python
def do_nothing():
    pass

result = do_nothing()
print(result)  # None
```

---

# 🔹 Scope of variables

* **Local**: inside a function.
* **Global**: outside all functions.

Python uses the **LEGB** rule: Local → Enclosing → Global → Built-in.

---

# 🔹 What is a traceback?

A traceback shows the **error history** when an exception occurs. It helps you find where and why an error happened.

---

# 🔹 What are the arithmetic operators and how to use them?

| Operator | Description        | Example  |
| -------- | ------------------ | -------- |
| `+`      | Addition           | `a + b`  |
| `-`      | Subtraction        | `a - b`  |
| `*`      | Multiplication     | `a * b`  |
| `/`      | Division           | `a / b`  |
| `//`     | Floor Division     | `a // b` |
| `%`      | Modulo (remainder) | `a % b`  |
| `**`     | Power              | `a ** b` |

---


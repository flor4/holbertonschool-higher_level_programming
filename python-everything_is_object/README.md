# Understanding Python Objects: `id`, `type`, Mutability, and Memory

![Mutable vs Immutable in Python](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*Qib7S_iqNXue-chQRM7lwQ.png)


## Introduction
Python is a flexible and powerful programming language, but understanding how it handles **objects in memory** is essential for writing clean, efficient, and bug-free code. In this guide, we will explore key concepts like `id()` and `type()`, the difference between **mutable** and **immutable** objects, how Python manages memory for these objects, and how this affects functions and variables. We’ll also cover advanced topics like **integer pre-allocation** and **aliases**.

---
# Table of Contents

In this guide, we’ll explore Python’s objects, memory management, and the difference between mutable and immutable types. Here’s a quick overview of the topics covered:

1. [Introduction](#introduction)
2. [`id()` and `type()`](#id-and-type)
3. [Mutable Objects](#mutable-objects)
4. [Immutable Objects](#immutable-objects)
5. [Why Does It Matter?](#why-does-it-matter)
6. [Function Arguments: Pass-by-Assignment](#function-arguments-pass-by-assignment)
7. [Assignment vs Referencing](#assignment-vs-referencing)
8. [Integer Pre-allocation (`NSMALLPOSINTS` and `NSMALLNEGINTS`)](#integer-pre-allocation-nsmallposints-and-nsmallnegints)
9. [Aliases](#aliases)
10. [Special Cases: Tuple and Frozen Set](#special-cases-tuple-and-frozen-set)
11. [Conclusion](#conclusion)

## What Are `id()` and `type()`?

Every object in Python has a **unique identity** and a **type**.  

- `id(object)` → returns the memory address of the object.  
- `type(object)` → returns the object’s class/type.  

Example:

```python
a = 42
b = a
print(id(a))  # e.g., 9793232
print(id(b))  # same as id(a)
print(type(a))  # <class 'int'>
````

> Tip: If two variables share the same `id()`, they point to the **same object** in memory.

---
![Mutable vs Immutable in Python](https://tse2.mm.bing.net/th/id/OIP.L9eWZKELyAvlXfcC9LfZMQHaE3?pid=Api)

## Mutable Objects

**Mutable objects** can be **modified after creation**. Common examples:

* `list`
* `dict`
* `set`
* `bytearray`

Example:

```python
lst = [1, 2, 3]
print(id(lst))      # e.g., 140574785643456
lst.append(4)
print(lst)          # [1, 2, 3, 4]
print(id(lst))      # same id → object modified in place
```

---

## Immutable Objects

**Immutable objects** **cannot be changed** once created. Common examples:

* Numbers: `int`, `float`, `complex`
* `str`
* `tuple`
* `frozenset`
* `bytes`

Example:

```python
x = 10
print(id(x))  # e.g., 9793216
x += 5
print(x)      # 15
print(id(x))  # new id → a new object was created
```

> Any operation that seems to “change” an immutable object actually **creates a new object in memory**.

---

## Why Does It Matter?

Understanding mutability affects:

* **Memory management** → mutable objects can be changed without creating new objects.
* **Function behavior** → mutable objects can be modified inside functions; immutables require reassignment.
* **Bug prevention** → unintentional changes to shared mutable objects can cause subtle bugs.

---

## Function Arguments: Pass-by-Assignment

Python uses **pass-by-assignment**, which behaves differently depending on object mutability:

```python
def modify_list(lst):
    lst.append(99)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # [1, 2, 3, 99] → mutable changed

def modify_int(n):
    n += 10
    return n

num = 5
num = modify_int(num)
print(num)      # 15 → immutable requires reassignment
```

---

## Assignment vs Referencing

Variables in Python are **references to objects**:

```python
a = [1, 2]
b = a  # b references the same object
b.append(3)
print(a)  # [1, 2, 3] → both see the same object
```

Immutable objects don’t allow this type of shared modification.

---

## Integer Pre-allocation (`NSMALLPOSINTS` and `NSMALLNEGINTS`)

Python pre-allocates **small integers** for efficiency:

```text
NSMALLPOSINTS = 256  # integers 0..255 pre-created
NSMALLNEGINTS = 5    # integers -1..-5 pre-created
```

Example:

```python
a = 100
b = 100
print(id(a) == id(b))  # True → same pre-allocated object
```

This saves memory and improves performance for commonly used numbers.

---

## Aliases

Multiple variables can reference the **same object**, creating **aliases**:

```python
x = [1, 2]
y = x
x.append(3)
print(y)  # [1, 2, 3] → both refer to the same object
```

Be careful with mutable objects, as changes affect all aliases.

---

## Special Cases: Tuple and Frozen Set

Tuples and frozensets are **immutable**, but can contain **mutable objects**:

```python
t = (1, [2, 3])
t[1].append(4)
print(t)  # (1, [2, 3, 4]) → inner list changed
```

The container is immutable, but its **contents can still be modified** if they are mutable.

---

## Conclusion

By understanding **mutability, memory management, and object identity**, you can:

* Avoid subtle bugs
* Improve performance
* Write more predictable Python code

Learning how Python handles mutable vs immutable objects is a key step toward **mastering the language**.

---
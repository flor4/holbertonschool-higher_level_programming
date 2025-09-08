
---

# 📚 Python - Data Structures: Lists, Tuples

## ✅ Project Tasks:

|  # | Task Description                        | 
| -: | --------------------------------------- |
|  0 🖨️📃| Print a list of integers                |
|  1 🔐📥| Secure access to an element in a list   |
|  2 🔁🧩| Replace element                         |
|  3 🔄📃| Print a list of integers... in reverse! |
|  4 🧬🔁| Replace in a copy                       |
|  5 👀🔣| Can you C me now?                       |
|  6 🧮📊| Lists of lists = Matrix                 |
|  7 ➕👥| Tuples addition                         |
|  8 🎁↩️| More returns!                           |
|  9 🔎📈| Find the max                            |
| 10 ✌️➗| Only by 2                               |
| 11 ❌📍| Delete at                               |
| 12 🔄🔁| Switch                                  |


## 📌 General Concepts

### 🔢 What are lists and how to use them?

Lists are **ordered, mutable collections** in Python. They can store items of any data type and allow duplicate elements.
You can create a list using square brackets:

```python
my_list = [1, 2, 3, 'hello']
```

You can access elements by index, modify them, and use built-in methods like `.append()` or `.remove()`.

---

### 🔡 What are the differences and similarities between strings and lists?

**Similarities:**

* Both are **sequences**.
* You can access elements by index.
* You can use slicing on both.

**Differences:**

* 📄 **Strings are immutable**, while 🧾 **lists are mutable**.
* Strings store only characters, lists can hold multiple data types.
* List methods like `.append()` and `.remove()` don’t exist for strings.

---

### 🧰 What are the most common methods of lists and how to use them?

Here are some popular list methods:

| Method      | Description                                   | Example                  |
| ----------- | --------------------------------------------- | ------------------------ |
| `append()`  | Adds an element at the end                    | `my_list.append(4)`      |
| `extend()`  | Adds elements from another iterable           | `my_list.extend([5, 6])` |
| `insert()`  | Inserts element at a specific position        | `my_list.insert(1, 'a')` |
| `remove()`  | Removes the first matching value              | `my_list.remove('a')`    |
| `pop()`     | Removes and returns the element at a position | `my_list.pop()`          |
| `sort()`    | Sorts the list in place                       | `my_list.sort()`         |
| `reverse()` | Reverses the list in place                    | `my_list.reverse()`      |
| `index()`   | Returns the index of a value                  | `my_list.index(2)`       |
| `count()`   | Returns the count of a value                  | `my_list.count(2)`       |

---

### 📥 How to use lists as stacks and queues?

* **Stacks** (LIFO: Last In, First Out):

  ```python
  stack = []
  stack.append(1)
  stack.append(2)
  stack.pop()  # 2
  ```

* **Queues** (FIFO: First In, First Out):

  ```python
  from collections import deque
  queue = deque([1, 2, 3])
  queue.append(4)
  queue.popleft()  # 1
  ```

---

### ⚡ What are list comprehensions and how to use them?

List comprehensions are a **concise way to create lists**.

```python
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]
```

You can also add conditions:

```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

### 🧱 What are tuples and how to use them?

Tuples are **immutable, ordered sequences**. Once created, you can't change their contents.

```python
my_tuple = (1, 2, 3)
```

Use them when you need fixed collections, like coordinates or return multiple values from a function.

---

### ❓ When to use tuples versus lists?

* Use **lists** when data needs to change (e.g., appending, sorting).
* Use **tuples** for **fixed data**, especially when used as dictionary keys or returned from functions.

🧠 Tip: Tuples are slightly faster and more memory-efficient than lists.

---

### 🔗 What is a sequence?

A **sequence** is an **ordered collection** of elements. Lists, tuples, strings, and ranges are all types of sequences in Python.
They support:

* Indexing
* Slicing
* Iteration
* Length checks with `len()`

---

### 📦 What is tuple packing?

Tuple packing is when you assign multiple values into a single tuple:

```python
packed = 1, 2, 'hello'
# packed is now (1, 2, 'hello')
```

---

### 📤 What is sequence unpacking?

Sequence unpacking extracts values from a tuple/list into variables:

```python
a, b, c = (1, 2, 3)
# a = 1, b = 2, c = 3
```

You can also use `*` to capture multiple elements:

```python
a, *rest = [1, 2, 3, 4]
# a = 1, rest = [2, 3, 4]
```

---

### ❌ What is the `del` statement and how to use it?

The `del` statement is used to delete:

* Variables
* Elements from a list
* Entire lists

```python
my_list = [1, 2, 3]
del my_list[1]  # [1, 3]
del my_list     # Deletes the entire list
```

---

## 📄 Requirements

* ✅ **Python Scripts**
* ✅ **Allowed editors**: `vi`, `vim`, `emacs`
* ✅ All files interpreted on **Ubuntu 20.04 LTS** using **Python 3.8.5**
* ✅ Each file must end with a **new line**
* ✅ The first line of each file must be:

  ```python
  #!/usr/bin/python3
  ```
* ✅ A `README.md` file is **mandatory**
* ✅ Code must follow **pycodestyle** (`v2.7.*`)
* ✅ All files must be **executable**
* ✅ File length will be tested with `wc`

---
# Python - import & modules

## Tasks

0. 🧩 [Import a simple function from a simple file](./0-add.py)  
1. 🧰 [My first toolbox!](./1-calculation.py)  
2. ⚙️ [How to make a script dynamic!](./2-args.py)  
3. ➕ [Infinite addition](./3-infinite_add.py)  
4. 🕵️‍♂️ [Who are you?]
5. 📦 [Everything can be imported](./5-variable_load.py)  

---
## 🚀 Quick Overview

* **✨ Why Python is awesome**  
  Python is simple, readable, powerful, and has a huge community full of libraries.

* **📥 How to import functions from another file**  
  Use `from file import function` to easily reuse code.

* **🔧 How to use imported functions**  
  Call them like any other function in your script.

* **📦 How to create a module**  
  A Python module is just a `.py` file containing functions or classes you want to reuse.

* **🔍 How to use the built-in `dir()` function**  
  `dir(object)` lists all attributes and methods available on an object or module.

* **⛔ How to prevent code from running on import**  
  Place executable code inside:

  ```python
  if __name__ == "__main__":
      # code here runs only when script is executed directly
---
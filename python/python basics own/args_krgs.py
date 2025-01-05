
"""
`**kwargs` (short for "keyword arguments") is used when you want to pass **a variable number of named arguments** (key-value pairs) into a function. These arguments are automatically packaged into a dictionary within the function.

---

### **When and Where to Use `**kwargs`**

You use `**kwargs` in situations where:

1. **Named Arguments** are Expected:
   You need flexibility in passing varying numbers of **key-value pairs** as arguments to the function.

2. **Processing Options or Configuration:**
   When you're building a function that might take optional parameters or settings (like a configuration), and you don’t want to predefine every possible argument.

3. **Passing Arbitrary Named Arguments to Another Function:**
   For functions that act as wrappers or intermediaries for others, you can forward keyword arguments dynamically.

---

### **Examples of `**kwargs` Usage**

---

#### **1. Flexible Number of Named Arguments**
You don’t know in advance how many named arguments the user will provide.

```python
def greet_all(**kwargs):
    for name, greeting in kwargs.items():
        print(f"{greeting}, {name}!")

greet_all(Alice="Hello", Bob="Hi", Charlie="Hey")
# Output:
# Hello, Alice!
# Hi, Bob!
# Hey, Charlie!
```

Here, `Alice="Hello"`, `Bob="Hi"`, and `Charlie="Hey"` are treated as key-value pairs in the `kwargs` dictionary.

---

#### **2. Configurable Functions**
Use `**kwargs` for functions with optional or dynamic settings.

```python
def configure_app(**settings):
    for setting, value in settings.items():
        print(f"Setting {setting} = {value}")

configure_app(debug=True, version="1.2.0", log_level="INFO")
# Output:
# Setting debug = True
# Setting version = 1.2.0
# Setting log_level = INFO
```

---

#### **3. Forwarding Named Arguments**
You can pass `**kwargs` to another function, dynamically forwarding all key-value pairs.

```python
def main_function(a, b, **kwargs):
    print(f"a = {a}, b = {b}")
    sub_function(**kwargs)

def sub_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

main_function(1, 2, x=10, y=20, z=30)
# Output:
# a = 1, b = 2
# x = 10
# y = 20
# z = 30
```

---

### **Differences Between `*args` and `**kwargs`**

| Feature         | `*args`                                     | `**kwargs`                           |
|------------------|---------------------------------------------|---------------------------------------|
| Input Type       | Positional arguments as a tuple            | Named (keyword) arguments as a dictionary |
| Example Function | `def my_func(*args):`                      | `def my_func(**kwargs):`             |
| Input Example    | `my_func(1, 2, 3)`                         | `my_func(a=1, b=2, c=3)`             |
| Access Inside    | Loop through `args` as a tuple             | Loop through `kwargs.items()` as a dictionary |

---

### **When to Prefer `**kwargs`**

1. **When Working with Named Arguments:**
   Use it if the arguments passed should have descriptive names.

2. **When Passing Optional Configuration Parameters:**
   If many optional named arguments are possible, `**kwargs` avoids making a function signature too complicated.

3. **Wrapper Functions:**
   It is often used in decorators or wrapper functions that can accept an arbitrary number of named arguments.

Example in a wrapper:
```python
def wrapper_function(func, **kwargs):
    print("Wrapper doing something before the function call...")
    return func(**kwargs)

def real_function(x, y):
    return x + y

print(wrapper_function(real_function, x=3, y=5))  # Output: 8
```

If you're confused about specific use cases, let me know, and I can provide tailored examples!

"""
def greet_all(**kwargs):
    for name, greeting in kwargs.items():
        print(f"{greeting}, {name}!")

greet_all(Alice="Hello", Bob="Hi", Charlie="Hey")


def main_function(a, b, **kwargs):
    print(f"a = {a}, b = {b}")
    sub_function(**kwargs)

def sub_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

main_function(1, 2, x=10, y=20, z=30)


def configure_app(**settings):
    for setting, value in settings.items():
        print(f"Setting {setting} = {value}")

configure_app(debug=True, version="1.2.0", log_level="INFO")
# Pluralsight Core Python Getting Started

These notes may be rather sparce.  It's either a section heading or actual notes for things that might be forgettable.

## Installing and Starting Python

I watched another video for this and didn't really have any notes for this section.  Any notes are in the main README.

## Scalar Types, Operators, and Control Flow

* REPL - Read Evaluate Print Loop
* REPL uses underscore "_" to reference previous value.
* Relational Operators
  * Falsey & Truthy - Constructing/Casting to a bool from int, float, [], or "
  * `bool("False")` is True since it's a non empty string
* Control Flow  *(if (): else: elif:)*
* While-loops *(while(): break)
* Mix and match single quotes and double quotes to avoid escaping either.
* Triple double quote is for multiline strings (used in docstring).

## Introducing Strings, Collections, and Iteration

All of this was pretty straightforward, so there aren't many notes here.

* String
* String Literals
* Bytes
* List
* Dict
* For-loop
* Putting it all Together

## Modularity

* Whitespace - 4 spaces for block indentation *(by convention)*
* "dunder" - Double Underscore "dunder name" = \_\_name__
* Docstrings
  * Google format is preferred
* Shebang (#! - Shhh...Bang!) - Special comment at the beginning of the file.
  * Determines how to run the Python file
  * Didn't seem to make a difference on Windows; the file ran with or without this line.
  * Pylauncher runs on Windows so if you only have Python 3 installed then it doens't matter

## Objects and Types

### Overview

* Evertying is an object.
  * x = 1000 *(x is a named reference to an immutable integer object whose value is 1000)*
  * x = 500 *(X references a **new** integer object whose value is 500)*
* `id()` - Every object has an id *(used when the* `is` *operator is used)*
* Lists **are** mutable
* Value vs. Identity Equality

### Passing Arguments and Returning Values

* Passing arguments
  * Lists - pass by reference
  * Can rebind lists within functions and the list outside the function will retain its values because its contents was **not** changed.
  * `*` is the repition operator when used with strings *( '-' \* 4 == '----' )*

### Function Arguments

* Default arguments are only evaluated **once** so assigning a time as a default argument will bind a **single** time to that argument which is not ideal.
  * Assigning a default empty list is not ideal as well because that list will only be assigned **once**.
  * Only use **immutable** types as default arguments.

### Python's Type System

* Type declarations are unnecessary
* Highly dynamic

### Scopes

From closest to broadest (LEGB)

1) **Local** - Inside the current function
2) **Enclosing** - Inside enclosing functions
3) **Global** - At the top level of the module
4) **Built-in** - In the special builtins module

* `global` - Allows function scope to access global variables, otherwise a new variable of the same name will be created.

### Everything is an Object

* `type()` - A function that returns the type of the object
* `dir()` - A function that returns a list of the attributes of an object including variables and functions, (kind of like reflection / introspection)

## Built-in Collections

### Tuples

* Use parenthesis to define tuples `(1, 'the', 1.2)`
* Single element tuples have a trailing comma `(123, )`. If the comma was not present then it would be interpreted as just an integer due to the parenthesis precedence.
* `()` is the empty tuple.
* The parenthesis may be omitted in many cases.  `1, 2, 3` is also a tuple.
* **Unpacking** tuples can assign multiple references to tuple values.
* `in` or `not in` operators

### Strings

* `len()`
* `+` concatenation operator *(may use a large amount of "temporaries")*
* `str.join()` is more efficient than `+`
  * `alpha = ';'.join(['abc', 'def', 'ghi'])`
  * results in a string 'abc;def;ghi'
  * `alpha.split(';')`
  * results in the list ['abc', 'def', 'ghi']
  * `''.join()` - is used to concatenate multiple strings *(with no separator)*
* `str.partition()` - splits a string into 3 pieces
  * `'unforgetable'.partition('forget')`
  * results in the tuple ('un', 'forget', 'able')
  * The single underscore `_` is used by convention to throw away values.
* `str.format()` - Most likely will have to look this stuff up anyway.
* **f-strings** - String interpolation.
  * `f'The value is {value}.` where value is evaluated
  * `:` may be used within the curly braces after the value to define precision.

### Ranges

* `range()`
  * `range(5)` returns a list of integers 0 - 4
  * `range(2, 8)` returns a list of integers 2 - 7
  * `range(2, 9, 2)` returns a list of even numbers 2 - 8 (a "step" paramter)
* `enumerate()` creates tuples of a list with their index as the first item in the tuple.

### Lists

* **Negative indexing** `[-1]` - Access elements from the end of the list.
* **Slicing** `thing[3:7]`  - Builds a sub-list from index 3 to 6.
  * Can be combined with negative indexing.
  * Half open range convention `thing[3:]` or `thing[:3]`
* `list.copy()` - Used to copy lists as well as using the "full slice" notation `theCopy = thing[:]`
* `list.index()` - Find the location of an object in a list.
* `list.count()` - Used with an argument will count the number of occurences of that value.
* `del` - Removes the item from the list
  * `del theList[3]` removes that element in the list.
* `list.remove()` - Removes an item from the list by value.
  * `theList.remove(')
* `list.insert()` - Inserts the item
* `list.extend()`
* `list.reverse()`
* `list.sort()` - Send in a function key *(sorts in place)*
* `reversed()` Send in a list and returns a list_reverseiterator object.
* `sorted()` - Send in a list. Returns a **new** list versus sorting in place.

### Dictionaries

* `dict.update()` - Merge dictionaries (update and insert)
* `dict.values()`
* `dict.keys()`
* `dict.items()`
* Can use the `del` function on dictionary entries.
* Pretty printing is a great way to print dictionaries.
  * `from pprint import pprint as pp`

### Sets

* Similar to dictionaries
* An efficient way to remove duplicates of a list
* `set.add()` - Add new elements.  No error if element already exists.
* Set Operations
  * `set.union()` is commutative
  * `set.intersection()` is commutative
  * `set.difference()` is **not** commutative
  * `set.symmetric_difference()` is commutative. First set **or** second set, but **not** both.
  * `set.issubset()`
  * `set.issuperset()`
  * `set.isdisjoint()`

### Protocols

* **Container** - `in` and `not in` supported
* **Sized** - `len()` will determine number of elements
* **Iterable** - Yielding elements one by ones
* **Sequence** - Indexed using `[]`, `.index()`, `.count()`, `reversed()`, iterable, sized, and container.
* **Mutable Sequence**
* **Mutable Set**
* **Mutable Mapping**

## Exceptions

Python takes the "liberal" approach to exceptions versus an exception truly being an "exceptional" case.  Under the covers exceptions typically require many cycles so it seems like things would run slower if throwing an exception is the "normal" course of action.

* `try:`
* `except:`
* `finally:`
* `pass` a noop in Python so there can be an effective empty block.
* **Exceptions Can Not Be Ignored** vs return codes that might be.
  * "More Pythonic" is to raise exceptions even for the little things.
* `raise` will re-raise the exception.

### Exceptions Are Part of the API

### Exceptions and Protocols

* `ValueError()`
* `IndexError()` integer index is out of bounds
* `KeyErrors()` lookup when a mapping fails

### Avoid Explicit Type Checks

### It's Easier to Ask Forgiveness Than Permission

* Prepaire for Failure and check all of the inputs *(Look Before You Leap - LBYL)*
* **Easier to Ask Forgiveness Than Permission** *(EAFP)*
  * The code's "happy path" is emphasized rather than being interspersed with error handling.

### Platform Specific Code

Can Try/Except around entire module definition and the functions will be defined at the module level.

## Iteration and Iterables

### List and Set Comprehensions

* **List Comprehension** - A fragment of code enclosed in square brackets
  * `[len(word) for word in words]` where words is a list
* **Set Comprehension** - A fragment of code enclosed in curly brackets
  * `{len(word) for word in words}` where words is a list (the set will not contain any duplicates)
* **Dictionary Comprehension** - A fragment of code enclosed in curly brackets
  * `{key: len(value) for key, value in theDictionary.items()}` creates a new dict
* **Filtering Comprehensions** - Optional filtering clause
  * `[x for x in range(101) if is_prime(x)]` only adds x to the list if it's prime.

### Iteration Protocols

* **iterable** Can be passed to `iter()` to produce an *iterator*
* **iterator** Can be passed to `next()` to get the enxt value in the sequence
* **Stopping Iteration with an Exception**  WHAT?
  * **A Single End** - Sequences only have one ending, after all, so reaching it is exceptional
  * **Infinite Sequences** - Finding the end of an infinite sequence would be truly exceptional

### Generator Functions

* Iterables defined by functions
* Lazy evaluation
* Can model sequences with no definite end
* Composable into pipelines
* `yield` - Generators functions must include at least one `yield` statement.
  * They may also include `return` statements.
  * Each call to `next()` on a generator executes the code up to the next `yield` statment
* Uses **PyCharm** debugger to illustrate.

### Maintaining State in Generators

### Laziness and the Infinite

* Generators only do enough work to produce requested data.
* This allows generator s to model inifite (or very large) sequences.
* Examples:
  * Sensor readings
  * Mathematical sequences
  * Contents of large files

### Generator Expressions

* The laziness reduces memory in many cases, depending on how the result is accessed.

### Iteration Tools

* Python has many built-in functions for working with iterators `enumerate()` and `sum()`
* The `itertools` module provides many more.
* `itertools.islice()` - Perform lazy slicing of any iterator.
* `itertools.count()` - An unbounded arithmetic sequence of integers.
* **Boolean Aggregation**
  * `any()` - Determins if **any** elements in a series are true
  * `all()` - Determins if **all** elements in a series are true
* `zip()` - Synchronize iterations across two or more iterables
* `chain()` - 

## Classes

### Defining Classes

### Instance Methods

* Must have the `self` parameter on all methods.

### Instance Initializers

* `__init__(self)` - Is an initializer and **not** a constructor.  Used to configure and object that already exists by the time \_\_init__ is called
* `_` **"private"** variables are marked with a leading underscore.

### Collaborating Classes

* **The Law of Demeter**
  * The principle of **least knowledge**
  * Never call methods on objects you receive from other calls
    * *Only talk to your friends*

### Object-Oriented Design with Functions

* Don't create a class if you don't have to.
* Separation of concerns for printing a boarding pass.
* **Tell! Don't ask.**
  * Tell other objects what to do instead of asking them their state and responding to it.

### Polymorphism and Duck Typing

* **Polymorphism** - Using objects of different types througha uniform interface.
  * It applies to both functions as well as more complex types.
* **Duck Typing**

      "When I see a bird that walks like a duck and swims like a duck and quacks like a ducks, I call that bird a duck."
    **James Whitecomb Riley**

  * An objects's fitness for use is only determined at use.
  * This is in contrast to statically typed compiled languages.
  * Suitability is not determined by inheritance or interfaces.

### Inheritance and Implementation

* Python uses **Late Binding** - The object attributes aren't bound until they are called during runtime.
* You can try any method on any object.
* Useful for sharing implementation between classes.

## File IO and Resource Managements

### Opening Files

* `open(file, mode, encoding)` - open a file for reading or writing
  * file: the path to the file (required)
  * mode: read, write, or append (r, w, a), plus binary or text (b, t)
  * encoding: encoding to use in text mode
    * What is the `sys.getdefaultencoding()`? Probably 'utf-8'

### Writing Text

### Reading Text

* `file.open('filename.txt', mode='rt', encoding='utf-8')`
* `file.read(32)` - read 32 characters since this was opened in text mode.
* `file.readline()` reads to a newline character (`'\n'`) or to the end of the file.
* `file.readlines()` reads all of the lines and returns a list.

### File Iteration

### Closing Fiels with Finally

### With-blocks

* `with () as` can be used with any objects that support the context-manager protocol.

### Binary Files

### File-like Objects

* Certain methods may not be defined.

## :books: References

* [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
* [PEP 257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

# functions_and_callables

## Positional Arguments

:page_facing_up: `hypervolume.py` - Demonstrates the use of positional arguments.
:page_facing_up: `tag.py` - Demonstrates the use of keyword arguments.

* `def func_call(*args)`
  * Arguments are passed in as a tuple.
* Positional **ONLY** - `def func_call(x, /)` - This type of definition does **not** allow calling by keywork.
  * Why?
  * Parity with modules implemented in other languages such as C
  * Prevent formal argument names from becoming a part of the API
    * This prevents dependencies on the name
    * Useful when the names have no semantic meaning (like i or j)

## Keyword Arguments (kwargs)

* `def func_call(name, **kwargs)`
  * Traditional parameter followed by keyword arguments.
  * Keyword parameters are passed in as a `dict`
* `def func_call(name, age, *, title='')` - The `*` designates that only keyword arguments may be passed after.

## Extended Call Syntax

* `func_call(*args)` - Allows calling of a function with a tuple. The `*` operator unpacks the tuple so it can be sent into the function.
* `func_call(**kwargs)` - Allows callinf of a function with a dict.  The `**` operator expands the dictionary for the function call.

## Closures

### Local Functions

* A function definied within another function.
* `def` is excuted at runtime, meanting functions are defined at runtime.  A new function is defined each time.
* Same scoping rules apply to local functions. (LEGB)
* Returning a local function to be executed, but references the enclosing scope.  This still works because the local function creates a **closure** which records objects from enclosing scopes.
* ***Closure** keeps recorded objects alive for use after the enclosing scope is gone.
* Implemented with a `__closeure__` attribute.
* **Function Factories** are functions that return other functions.

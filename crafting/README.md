# Crafting

## Problem

In order to **craft** an item it takes certain amounts of resources.
Those resources are available in levels.  Each level may contain certain resources at certain amounts.  Each level has a "cost" (Energy) to run through.
A resource is also considered an item because you can craft different resources from other resources at a certain probability.

Figure out the optimal levels to traverse in order to craft an item.

## Objects

* Item
  * Name
  * Resources Needed[]
* Level
  * Name
  * Resources Generated[]
* Resource

## Steps

* Build out object model
* Build out resource dependencies
* [Unit Tests](https://docs.python.org/3/library/unittest.html)
* Data in JSON files
* Solve

## Example

* Item: Warrior
  * Resources
    * Water x 100
    * Metal x 10
    * Bone x 25

* Resource: Metal
  * Resources
    * Bone @ 60%

* Resource: Bone
  * Resources
    * Water @ 80%

* Resource: Water
  * Resources: null (cannot be crafted)

* Level: 1
  * Energy x 10
  * Resources
    * Bone x 5-6
    * Water x 10-12

* Level: 2
  * Energy x 10
  * Resources
    * Metal x 3-5
    * Water x 20-25

* Level: 3
  * Energy x 10
  * Resources
    * Metal x 5-8
    * Bone x 12-15

## Reference

* [JSON Serialization in Python](https://www.geeksforgeeks.org/serialize-and-deserialize-complex-json-in-python/)
* [JSON Example](https://www.code-learner.com/python-json-example/)
* [Naming Conventions](https://namingconvention.org/python/)
* [pylint - false import errors](https://stackoverflow.com/questions/63373911/how-do-you-make-pylint-in-vscode-know-that-its-in-a-package-so-that-relative-i) ❌ didn't work
* [pyright documentation](https://github.com/microsoft/pyright/blob/master/docs/configuration.md)

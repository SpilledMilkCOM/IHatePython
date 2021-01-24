from item import Item
from resource import Resource

def createWarrior():
    resources = []
    resources.append(Resource("Water", 100))
    resources.append(Resource("Metal", 10))
    resources.append(Resource("Bone", 25))

    result = Item("He-Man", resources)

    return result

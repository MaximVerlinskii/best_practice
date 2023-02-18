# Dependency Inversion Principle (DIP)
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.PARENT, parent)
        )


def some_high_level_logic(name, relationships):
    relations = relationships.relations
    for r in relations:
        if r[0].name == name and r[1] == Relationship.PARENT:
            print(f'{name} has a child called {r[2].name}.')

# Not good ^


# GOOD
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class BetterRelationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.PARENT, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


def some_high_level_logic_2(name, relationships_browser):
    for p in relationships_browser.find_all_children_of(name):
        print(f'{name} has a child called {p}.')


if __name__ == '__main__':
    parent = Person('John')
    child_1 = Person('Mark')
    child_2 = Person('Nikolai')

    relshps = Relationships()
    relshps.add_parent_and_child(parent, child_1)
    relshps.add_parent_and_child(parent, child_2)

    some_high_level_logic('John', relshps)

    # Not good ^

    # GOOD
    relshps_2 = BetterRelationships()
    relshps_2.add_parent_and_child(parent, child_1)
    relshps_2.add_parent_and_child(parent, child_2)
    some_high_level_logic_2('John', relshps_2)

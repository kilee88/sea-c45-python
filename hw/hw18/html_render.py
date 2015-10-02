#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    def __init__(self, name=""):
        self.name = name
        self.children = []

    def append(self, child):
        self.child = children.append(child)

    def render(self, f):
        f.write("<{name}>".format(name=self.name))
        # TODO: WRITE OUT THE CHILDREN HERE
        f.write("<{name}>".format(name=self.name))

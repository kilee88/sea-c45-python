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
        self.children.append(child)

    def render(self, f):
        f.write("\n<{name}>".format(name=self.name))
        for child in self.children:
            child.render(f)
        f.write("\n</{name}>".format(name=self.name))


class Html(Element):
    def __init__(self):
        super(Html, self).__init__(name="html")


class Body(Element):
    def __init__(self):
        super(Body, self).__init__(name="body")


class P(Element):
    def __init__(self, content):
        super(P, self).__init__(name="p")
        #self.content = content
        self.append(content)

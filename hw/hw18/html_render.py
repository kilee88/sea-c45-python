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

    def render(self, f, n=0):
        if(type(self) == Html):
            f.write("<!DOCTYPE html>")
        spaces = "    "
        ind = spaces * n
        n2 = n + 1
        ind2 = spaces * n2
        f.write("\n{ind}<{name}>".format(ind=ind, name=self.name))
        for child in self.children:
            if (type(child) != str):
                child.render(f, n + 1)
            else:
                f.write("\n{ind}{child}".format(ind=ind2, child=child))
        f.write("\n{ind}</{name}>".format(ind=ind, name=self.name))


class Html(Element):
    def __init__(self):
        super(Html, self).__init__(name="html")


class Body(Element):
    def __init__(self):
        super(Body, self).__init__(name="body")


class P(Element):
    def __init__(self, content):
        super(P, self).__init__(name="p")
        self.append(content)


class Title(Element):
    def __init__(self, content):
        super(Title, self).__init__(name="title")
        self.append(content)

    def render(self, f, n=0):
        spaces = "    "
        ind = spaces * n
        content = self.children[0]
        f.write("\n{ind}<title>{content}</title>".format(ind=ind,
                                                         content=content))


class Head(Element):
    def __init__(self):
        super(Head, self).__init__(name="head")

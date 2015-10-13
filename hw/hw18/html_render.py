#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, name="", style=""):
        self.name = name
        self.children = []
        self.style = style

    def append(self, child):
        self.children.append(child)

    def render(self, f, n=0):
        if(type(self) == Html):
            f.write("<!DOCTYPE html>")
        spaces = "    "
        ind = spaces * n
        n2 = n + 1
        ind2 = spaces * n2
        if(type(self) == P):
            style = ' style="{s}"'.format(s=self.style)
        else:
            style = ""
        f.write('\n{ind}<{name}{s}>'.format(ind=ind, name=self.name, s=style))
        for child in self.children:
            if (type(child) != str):
                child.render(f, n + 1)
            else:
                f.write("\n{ind}{child}".format(ind=ind2, child=child))
        f.write("\n{ind}</{name}>".format(ind=ind, name=self.name))


class SelfClosingTag(Element):
    def __init__(self, name=""):
        super(SelfClosingTag, self).__init__(name=name)

    def render(self, f, n=0):
        spaces = "    "
        ind = spaces * n
        f.write("\n{ind}<{name} />".format(ind=ind, name=self.name))


class Hr(SelfClosingTag):
    def __init__(self):
        super(Hr, self).__init__(name="hr")


class Br(SelfClosingTag):
    def __init__(self):
        super(Br, self).__init__(name="br")


class A(Element):
    def __init__(self, link, content):
        self.link = link
        super(A, self).__init__(name="a")
        self.append(content)

    def render(self, f, n=0):
        spaces = "    "
        ind = spaces * n
        f.write('\n{ind}<{name} href="{link}">{c}</{name}>'.format(ind=ind, name=self.name, link=self.link, c=self.children[0]))

class Html(Element):
    def __init__(self):
        super(Html, self).__init__(name="html")


class Body(Element):
    def __init__(self):
        super(Body, self).__init__(name="body")


class P(Element):
    def __init__(self, content, style):
        super(P, self).__init__(name="p", style=style)
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

# from time import sleep
from xml.dom import minidom

from constants import UTF

with open("first_screen.xml", 'r', encoding=UTF) as f:
    dom = minidom.parse("first_screen.xml")
    nodes = dom.getElementsByTagName("node")
    arr = []
    for text in nodes:
        q = text.getAttribute("text")
        if q != '':
            arr.append(q)
    print(arr)


def create_two_lists():
    ...
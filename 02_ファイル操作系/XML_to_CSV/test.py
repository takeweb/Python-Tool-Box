from xml.etree import ElementTree

def dump_node(node, indent=0):
    print("{}{} {} {}".format('    ' * indent, node.tag, node.attrib, node.text.strip()))
    #print("tag:", node.tag)
    #print("attrib:", node.attrib)
    #print("text", node.text.strip())
    for child in node:
        dump_node(child, indent + 1)

if __name__ == '__main__':
    tree = ElementTree.parse('books.xml')
    dump_node(tree.getroot())

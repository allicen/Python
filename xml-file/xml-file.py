from xml.etree.ElementTree import XMLParser

tree = input()


class Depth:
    depth = 0

    color_cube = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    def write_color(self, color, weight):
        get_weight = self.color_cube.get(color)
        update = get_weight + weight
        self.color_cube.update({color: update})

    def start(self, tag, attrib):
        self.depth += 1
        if tag == "cube":
            self.write_color(attrib["color"], self.depth)

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass


target = Depth()
parser = XMLParser(target=target)
parser.feed(tree)
parser.close()

result = ""
for elem in target.color_cube:
    result += str(target.color_cube.get(elem))
    result += " "

print(result.strip())
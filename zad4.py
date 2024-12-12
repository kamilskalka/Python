#Zaimplementowac algorytm Aho-Corasick

class Node:
    def __init__(self):
        self.links = {}
        self.patterns = []
        self.fail_link = None


def create_automaton(patterns):
    root = Node()

    for pattern in patterns:
        current_node = root
        for char in pattern:
            current_node = current_node.links.setdefault(char, Node())
        current_node.patterns.append(pattern)

    queue = []
    for node in root.links.values():
        queue.append(node)
        node.fail_link = root

    while queue:
        current_node = queue.pop(0)
        for key, next_node in current_node.links.items():
            queue.append(next_node)
            fail_node = current_node.fail_link
            while fail_node and key not in fail_node.links:
                fail_node = fail_node.fail_link
            next_node.fail_link = fail_node.links[key] if fail_node else root
            next_node.patterns += next_node.fail_link.patterns

    return root


def find_patterns(text, patterns):
    root = create_automaton(patterns)
    matches = {pattern: [] for pattern in patterns}

    current_node = root
    for idx, char in enumerate(text):
        while current_node and char not in current_node.links:
            current_node = current_node.fail_link

        if not current_node:
            current_node = root
            continue

        current_node = current_node.links[char]
        for pattern in current_node.patterns:
            matches[pattern].append(idx - len(pattern) + 1)

    return matches


text1 = "dfhlsfdsfdalsfdalhfsdaasdlewqtpg98go;iadfhblifdsuhtpeetrulhgsgdjkhlsdhkgkgfk"
patterns1 = ["df", "ls"]
result1 = find_patterns(text1, patterns1)
print(result1)

text2 = "abxabcabcabyasdbasdajsdausdtyasdavsdasidasydasghdasdjasjdajsdjasjdastdavsdasdajdajsdjadjasd"
patterns2 = ["ab", "abc", "aby", "asd"]
result2 = find_patterns(text2, patterns2)
print(result2)

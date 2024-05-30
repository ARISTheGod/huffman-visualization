import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from collections import deque

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.x = None
        self.y = None

def build_huffman_tree(characters, frequencies):
    nodes = [Node(char, freq) for char, freq in zip(characters, frequencies)]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: (x.freq, x.char))
        left, right = nodes.pop(0), nodes.pop(0)
        new_node = Node(None, left.freq + right.freq, left, right)
        nodes.append(new_node)

    return nodes[0]

def set_node_positions(root):
    # Assign initial x position based on in-order traversal
    def assign_x(node, x=0):
        if not node:
            return x
        x = assign_x(node.left, x)
        node.x = x
        return assign_x(node.right, x + 1)

    assign_x(root)

    # Level-order traversal to assign y
    queue = deque([(root, 0)])  # (node, level)
    while queue:
        node, level = queue.popleft()
        node.y = -level  # Assign y based on level

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

def draw_tree(node, ax):
    if node.char:
        label = f"{node.char}({node.freq})"
    else:
        label = f"({node.freq})"

    ax.text(node.x, node.y, label, ha='center', va='center',
            bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round'))

    if node.left:
        ax.add_line(mlines.Line2D([node.x, node.left.x], [node.y, node.left.y]))
        ax.text((node.x + node.left.x) / 2, (node.y + node.left.y) / 2, '0', va='center', ha='center')
        draw_tree(node.left, ax)
    if node.right:
        ax.add_line(mlines.Line2D([node.x, node.right.x], [node.y, node.right.y]))
        ax.text((node.x + node.right.x) / 2, (node.y + node.right.y) / 2, '1', va='center', ha='center')
        draw_tree(node.right, ax)

def decode_message(huffman_tree, encoded_message):
    decoded_message = ""
    current_node = huffman_tree

    for bit in encoded_message:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_message += current_node.char
            current_node = huffman_tree

    return decoded_message

# Add a preorder traversal method to the Node class
def traverse_preorder(self):
    yield self
    if self.left:
        yield from self.left.traverse_preorder()
    if self.right:
        yield from self.right.traverse_preorder()

Node.traverse_preorder = traverse_preorder

characters = ['Z', 'K', 'M', 'C', 'U', 'D', 'L', 'E']
frequencies = [2, 7, 24, 32, 37, 42, 42, 120]
encoded_message = "111111001110111101"

huffman_tree = build_huffman_tree(characters, frequencies)
decoded_message = decode_message(huffman_tree, encoded_message)

fig, ax = plt.subplots(figsize=(12, 8))

set_node_positions(huffman_tree)  # Use the new positioning function
draw_tree(huffman_tree, ax)

ax.set_xlim(-1, 15)
ax.set_ylim(-10, 1)
ax.axis('off')

plt.text(7, -9, f"Decoded Message: {decoded_message}", ha='center', fontsize=10)

plt.savefig("huffman_tree_no_overlap.png")
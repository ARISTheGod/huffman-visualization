# Huffman Coding Visualization

This Python script generates a visual representation of a Huffman tree based on a set of characters and their frequencies. It also decodes an encoded message using the generated Huffman tree.

## Requirements

- Python 3
- matplotlib (install using `pip install -r requirements.txt`)

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ARISTheGod/huffman-visualization.git
   ```
   (Replace `ARISTheGod` with your actual GitHub username)

2. **Navigate to the project directory:**
   ```bash
   cd huffman-visualization
   ```

3. **Install the required library:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the script:**
   ```bash
   python huffman_visualization.py
   ```
5. **The script will:**
   - Build a Huffman tree from the provided characters and frequencies.
   - Decode the hardcoded encoded message.
   - Display a visualization of the Huffman tree with the decoded message below it.
   - Save the visualization as an image file named `huffman_tree_no_overlap.png`.

## Example

**Input:**

- Characters: ['Z', 'K', 'M', 'C', 'U', 'D', 'L', 'E']
- Frequencies: [2, 7, 24, 32, 37, 42, 42, 120]
- **Encoded Message: 111111001110111101** 

**Output:**

- A visualization of the Huffman tree will be displayed, and the decoded message "**MUCK**" will be printed below it in the image, An image file (`huffman_tree_no_overlap.png`) will be saved in the same directory as the code.

## Code Overview

- **`Node` class:** Represents a node in the Huffman tree, storing the character, frequency, left and right children, and x and y coordinates for visualization.
- **`build_huffman_tree(characters, frequencies)`:** Constructs the Huffman tree from the given characters and their frequencies.
- **`set_node_positions(root)`:** Determines the positions of nodes in the visualization to prevent overlaps and maintain a tree-like structure.
- **`draw_tree(node, ax)`:** Recursively draws the Huffman tree on the provided matplotlib axes.
- **`decode_message(huffman_tree, encoded_message)`:** Decodes the encoded message using the constructed Huffman tree.

## Note

- The code uses a hardcoded encoded message in this example. 
> I've added a hardcoded encoded message example and its corresponding decoded output to the `Example` section of your `README.md` file. Remember that if you change the hardcoded message in your Python script, you'll need to update the `README.md` accordingly to keep the documentation consistent.

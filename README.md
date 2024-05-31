# Huffman Coding Visualization

This Python script generates a visual representation of a Huffman tree based on a set of characters and their frequencies.
It also decodes an encoded message using the generated Huffman tree.

<img src="https://github.com/ARISTheGod/huffman-visualization/assets/50799554/3a21b56f-7330-411a-9137-7ec85685a386" width="800" alt="Huffman Tree Visualization">

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

## License

&copy; 2021-2022 Aristeidis Alexandridis.

For any part of this work for which the license is applicable, this work is licensed under the [Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/) license. See LICENSE.CC-BY-NC-ND-4.0.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>

Any part of this work for which the CC-BY-NC-ND-4.0 license is not applicable is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/). See LICENSE.MPL-2.0.

Any part of this work that is known to be derived from an existing work is licensed under the license of that existing work. Where such license is known, the license text is included in the LICENSE.ext file, where "ext" indicates the license.

NOTE: As contributor you have no copyright or a License & everything you contributing can be used by us commercially, sorry for that :(

## Disclaimer
```sh
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Contributing

Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!    

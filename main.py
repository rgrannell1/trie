
from typing import Callable, Dict


class Trie:
  """Construct a trie"""

  def __init__(self) -> None:
    """Initialise an empty trie, with zero descendants and zero target entries"""

    self.children: Dict[str, Trie] = {}
    self.descendants: int = 0
    self.size: int = 0

  def insert(self, key: str) -> None:
    """Insert a string into the trie. Keep track of descendant nodes and
    the number of entries at a target node."""

    cursor = self
    for char in key:
      if char not in cursor.children:
        cursor.children[char] = Trie()
        self.descendants += 1

      cursor = cursor.children[char]

    cursor.size += 1


  def sort(self, sortBy: Callable):
    """Recursively sort child-nodes by a key lambda, in-place"""

    swap = { }

    for char, subtrie in sorted(self.children.items(), key = lambda pair: sortBy(pair[1])):
      swap[char] = subtrie

    self.children = swap

    # the children have been sorted; recursively sort their descendants
    for child in self.children.values():
      child.sort(sortBy)


  def values(self) -> list[str]:
    items = []
    dfs(self, "", items)
    return items


def dfs(trie: Trie, prefix: str, res: list[str]):
  """Preorder traversal of child-nodes"""

  # multiple prefixes can be stored at the same leaf; append them
  # to the result list.
  if trie.size > 0:
    res += [prefix] * trie.size

  # recur into child-elements
  for char, child in trie.children.items():
    dfs(child, prefix + char, res)


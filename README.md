# LeetCode
:writing_hand: The purpose of this repository is to track my LeetCode progress and make some notes and summaries along the way.


#### :world_map: Data Structures / Methods Summary
- Breadth-first search (BFS) / Depth-first search (DFS)
  - [79. Word Search](79_word_search_v2.py)
    - Python: Can not use `[[0]*n]*m` to create list of list!!! The lists will refer to the same id!
  - [1162. As Far from Land as possible](1162_As_Far_from_Land_as_Possible.py)

- Hash Table
  - [380. Insert Delete GetRandom O(1)](380_insert_delete_getrandom.py)
    - Python: In Python 2, dictionary.keys() returns a list contains all the keys. But in Python 3, the same function would return an object called dict_keys([]), and it does not support indexing. Converting the object to a list would cost `O(n)` time.

- Two Pointers
  - [3. Longest Substring Without Repeating Characters]
  - [11. Container With Most Water]
  - [15. 3Sum]
  - [26. Remove Duplicates from Sorted Array]
  - [42. Trapping Rain Water]
  - [88. Merge Sorted Array]

- General Algorithm / Array Manipulation
  - [54. Spiral Matrix (initial idea)](54_spiral_matrix.py)
    - Python: [Use function `yield` instead of `return`](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/) to produce a generator, or a sequence of values without using storing the sequence.
    - [Alternative version using `yield`](54_spiral_matrix_v2.py): Code simplified, speed improved only if we yield matrix entries directly instead of coordinates
    

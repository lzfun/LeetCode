# LeetCode
:writing_hand: The purpose of this repository is to track my LeetCode progress and make some notes and summaries along the way.


#### :world_map: Data Structures / Methods Summary
- **Breadth-first search (BFS) / Depth-first search (DFS)**
  - [79. Word Search](code/79_word_search_v2.py)
    - Python: Can not use `[[0]*n]*m` to create list of list!!! The lists will refer to the same id!
  - [1162. As Far from Land as possible](code/1162_As_Far_from_Land_as_Possible.py)

- **Hash Table**
  - [380. Insert Delete GetRandom O(1)](code/380_insert_delete_getrandom.py)
    - Python: In Python 2, dictionary.keys() returns a list contains all the keys. But in Python 3, the same function would return an object called dict_keys([]), and it does not support indexing. Converting the object to a list would cost `O(n)` time.
- **Dynamic Programming**
  - [91. Decode Ways](notes/91_decode_ways.md)
    
- **Two Pointers**
  - [3. Longest Substring Without Repeating Characters]
  - [11. Container With Most Water]
  - [15. 3Sum]
  - [26. Remove Duplicates from Sorted Array]
  - [42. Trapping Rain Water]
  - [88. Merge Sorted Array]

- **General Algorithm / Array Manipulation**
  - [54. Spiral Matrix (initial idea)](code/54_spiral_matrix.py)
    - Python: [Use function `yield` instead of `return`](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/) to produce a generator, or a sequence of values without using storing the sequence.
    - [Alternative version using `yield`](code/54_spiral_matrix_v2.py): Code simplified, speed improved only if we yield matrix entries directly instead of coordinates
    
  - [59. Spiral Matrix II](code/59_spiral_matrix_II.py)

- **Miscellaneous**
  - [1154. Day of the Year](code/1154_day_of_year.py)
    - Leap year rules: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`

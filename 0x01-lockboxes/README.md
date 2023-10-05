# Lockboxes

* You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

* Write a method that determines if all the boxes can be opened.

1. Prototype: ``` def canUnlockAll(boxes) ```
2. ``` boxes ``` is a list of lists
3. A key with the same number as a box opens that box
4. You can assume all keys will be positive integers
* There can be keys that do not have boxes
5. The first box ``` boxes[0] ``` is unlocked
6. Return ``` True ``` if all boxes can be opened, else return ``` False ```
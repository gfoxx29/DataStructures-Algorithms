
To implement the LRU, we have to use two data structures:
	- A doubly-linked list
	- A hash maps 

Python container OrderedDict is using a doubly linked list to maintain the order of elements in the dictionary. 

	- Deletion and Insertion operation takes O(1)
	- Space complexity O(n)
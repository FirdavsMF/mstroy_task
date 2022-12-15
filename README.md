# Tree generator from list of Node objects.

## Node object field:
* id 
* parent
* **options


## Some comments about Big O Notation

Build Tree: O(n)

#### Tree methods:
* .get_all() : O(n)
* .get_item(item_id) : O(1)
* .get_children(item_id) : O(1)
* .get_all_parents(item_id) : max O(n)

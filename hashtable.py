# Roy Yi
# 10/25/21
# Implement hashtable

class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.ht = [None for _ in range(97)]

    def put(self, key, val):
        idx = hash(key) % len(self.ht)
        if self.ht[idx]:
            self.ht[idx].next = ListNode(key, val)
        else:
            self.ht[idx] = ListNode(key, val)

    def get(self, key):
        idx = hash(key) % len(self.ht)

        node = self.ht[idx]
        while node.key != key:
            node = node.next

        return node.val

def main():
    d = HashMap()
    d.put('a', 25)
    d.put('b', 50)
    d.put("daniel", 40)

    print(d.get('a'))
    print(d.get("daniel"))


# a hashtable is an array of linked lists.
# size of hashtable should be a prime number

# a set is a hashtable with no values associated with key (key is the value)

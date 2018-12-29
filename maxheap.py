# This max heap have O(1) remove method
class Heap:
    def __init__(self):
        self.arr = []
        self.hash = {}
    
    def peek(self):
        return self.arr[0]
    
    def push(self, val):
        self.arr.append(val)
        self.hash[val] = len(self.arr)-1
        self.flow_up(len(self.arr) - 1)
        
    def flow_up(self, idx):
        while idx > 0:
            parent = (idx-1) // 2
            if self.arr[idx] > self.arr[parent]:
                self.swap(idx,parent)
                idx = parent
            else:
                break

    def swap(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]
        self.refresh_hash(a)
        self.refresh_hash(b)

    def refresh_hash(self, idx):
        self.hash[self.arr[idx]] = idx

    def flow_down(self, idx):
        while idx < len(self.arr):
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            left_val = self.arr[left_child] if left_child < len(self.arr) else -sys.maxsize
            right_val = self.arr[right_child] if right_child < len(self.arr) else -sys.maxsize
            
            if self.arr[idx] < left_val and right_val < left_val:
                self.swap(idx, left_child)
                idx = left_child
            elif self.arr[idx] < right_val and left_val < right_val:
                self.swap(idx, right_child)
                idx = right_child
            else:
                break
    
    def remove(self, val):
        if val not in self.hash:
            return
        idx = self.hash[val]
        del self.hash[val]
        if idx == len(self.arr) - 1:
            self.arr.pop()
        else:
            # swap with last val
            self.arr[idx] = self.arr[-1]
            self.refresh_hash(idx)
            self.arr.pop()

            self.flow_up(idx)    
            self.flow_down(idx)

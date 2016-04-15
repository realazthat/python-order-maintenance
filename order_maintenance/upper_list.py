



LOGM = 30
M = 1<<LOGM
MASK = M - 1

def ceildiv(a, b):
    return -(-a // b)

class UpperNode:
    def __init__(self,label,next_node,prev_node):
        self.label = label
        self.next_node = next_node
        self.prev_node = prev_node

    def insert(self):
        j = 1
        cur = self.next_node
        v0 = self.label
        wj = 1

        #move cur forward
        while cur is not None and cur.label-v0 <= j*j:
            wj = ceildiv((cur.label - v0), j)
            j += 1
            cur=cur.next_node

        cur = self.next_node

        for k in range(1, j):
            cur.label = v0 + int(wj * k)
            cur = cur.next_node


        nlabel = (v0 + self.next_node.label) >> 1
        result = UpperNode(nlabel, self.next_node, self)

        self.next_node.prev_node = result
        self.next_node = result
        return result

    def remove(self):
        self.next_node.prev_node = self.prev_node
        self.prev_node.next_node = self.next_node
        self.next_node = self.prev_node = None

    def compare(self,other):
        return self.label - other.label

    def split(self):
        if self.next_node:
            other = self.next_node
            self.next_node = UpperNode(M-1, None, None)
            other.prev_node = UpperNode(0, None, None)
            return other
        else:
            return createUpperList()
def createUpperList():
    begin = UpperNode(0, None, None)
    end = UpperNode(M-1, None, begin)
    begin.next_node = end
    return begin

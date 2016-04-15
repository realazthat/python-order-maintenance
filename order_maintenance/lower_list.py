

from .upper_list import M, LOGM, createUpperList

MSTEP = (M//LOGM)


class LowerNode:
    def __init__(self,upper, label, next_node, prev_node, value=None):
        self.upper = upper
        self.label = label
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value


    def insert(self,value=None):
        n = M
        #Create node and link it
        result = LowerNode(self.upper, -1, self.next_node, self, value)
        if self.next_node is not None:
            n = self.next_node.label
            self.next_node.prev_node = result
            
        self.next_node = result
        #Update labels
        if n == self.label+1:
            #Scan to extents of subtree
            count = 0
            begin = self
            while begin.prev_node is not None and begin.prev_node.upper == self.upper:
                begin = begin.prev_node
                count += 1
            end = self
            while end.next_node is not None and end.next_node.upper == self.upper:
                end = end.next_node
                count += 1
                
            end = end.next_node
            #Redistribute nodes
            upper = self.upper
            cur = begin
            while True:
                #Relabel nodes
                label = 0
                for j in range(LOGM):
                    if cur == end:
                        return result

                    cur.label = label
                    cur.upper = upper


                    cur = cur.next_node
                    label += MSTEP
                upper = upper.insert()
        else:
            result.label = min((self.label + n)>>1, self.label + LOGM)
            assert isinstance(result.label, int)
        return result

    def remove(self):
        uniqueUpper = True
        if self.next_node is not None:
            self.next_node.prev_node = self.prev_node
            uniqueUpper = self.next_node.upper != self.upper 
        if self.prev_node is not None:
            self.prev_node.next_node = self.next_node
            uniqueUpper = uniqueUpper and (self.prev_node.upper != self.upper)
        
        if uniqueUpper:
            self.upper.remove()


    def split(self):

        if self.next_node is None:
            return None

        other = self.next_node
        nupper = self.upper.split()
        if nupper.prev_node:
            nupper = nupper.prev_node
        
        self.next_node = None
        other.prev_node = None
        
        cur = other
        while cur is not None and cur.upper == self.upper:
            cur.upper = nupper

            cur = cur.next_node
        return other

    def compare(self,other):
        d = self.upper.compare(other.upper)
        if d != 0:
            return d
        return self.label - other.label

def createLowerList(*args):
    root = LowerNode(createUpperList(), 0, None, None)
    if len(args) < 1:
        return root
    
    for arg in reversed(args):
        root.insert(arg)

    result = root.next_node
    root.remove()
    return result

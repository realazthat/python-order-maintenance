
import unittest

from order_maintenance.lower_list import createLowerList
from order_maintenance.upper_list import createUpperList


def print_upper_list(l):
    assert l is not None
    cur = l

    i = 0
    while cur is not None:
        print ('%s: %s' % (i,cur.label))
        cur = cur.next_node
        i += 1
    print ('(%s)' % (i,))
def print_lower_list(l):
    assert l is not None
    cur = l

    i = 0
    while cur is not None:
        print ('%s: %s' % (i,cur.value))
        cur = cur.next_node
        i += 1
    print ('(%s)' % (i,))

class TestList(unittest.TestCase):

    def test_lower_list(self):
        self.do_test_list(createLowerList)
    def test_upper_list(self,):
        self.do_test_list(createUpperList)
    def do_test_list(self,createList):

        #Basic insert and com
        a = createList()
        b = a.insert()

        self.assertEqual(a.next_node, b)
        self.assertEqual(b.prev_node, a)
        self.assertLess(a.compare(b), 0)
        self.assertTrue(b.compare(a) > 0)
        self.assertTrue(a.compare(a) == 0)
        
        #More insertions
        base = createList()
        for i in range(1000):
            base.insert()
        
        l = base.next_node
        while l is not None:
            self.assertLess(l.prev_node.compare(l), 0)
            self.assertTrue(l.compare(l.prev_node) > 0)
            self.assertTrue(l.compare(l) == 0)
            self.assertTrue(l.compare(base) > 0)
            self.assertTrue(base.compare(l) < 0)
            l = l.next_node
            i += 1

        #Try remove
        for i in range(500):
            base.next_node.remove()
        l = base.next_node
        while l is not None:
            self.assertTrue(l.prev_node.compare(l) < 0)
            self.assertTrue(l.compare(l.prev_node) > 0)
            self.assertTrue(l.compare(l) == 0)
            self.assertTrue(l.compare(base) > 0)
            self.assertTrue(base.compare(l) < 0)
            l = l.next_node
        

        #Try inserting again
        for i in range(1000):
            base.insert()
        l = base.next_node
        while l is not None:
            self.assertTrue(l.prev_node.compare(l) < 0)
            self.assertTrue(l.compare(l.prev_node) > 0)
            self.assertTrue(l.compare(l) == 0)
            self.assertTrue(l.compare(base) > 0)
            self.assertTrue(base.compare(l) < 0)
            l = l.next_node

if __name__ == '__main__':
    unittest.main()

'''
Created on Dec 20, 2018

@author: pc
'''
import random
import unittest
from business.sortari import InsertionSort, CombSort


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testInsertionSort(self):
        self.l=[]
        InsertionSort(self.l,key=lambda x:x,cmp=None,reversed=True)
        self.assertTrue(self.l==[])
        
        self.l=[1]
        InsertionSort(self.l,key=lambda x:x,cmp=None,reversed=True)
        self.assertTrue(self.l==[1])

        self.l=[1,3,2]
        InsertionSort(self.l,key=lambda x:x,cmp=None,reversed=True)
        self.assertTrue(self.l==[1,2,3])
        
        self.l=[1,3,2,5,4]
        InsertionSort(self.l,key=lambda x:x,cmp=None,reversed=True)
        self.assertTrue(self.l==[1,2,3,4,5])
        
        self.l=[1,3,2,5,4,7,6]
        InsertionSort(self.l,key=lambda x:x,cmp=None,reversed=True)
        self.assertTrue(self.l==[1,2,3,4,5,6,7])
        
    def test(self):
        for i in range(100):
            l=[]
            lungime=random.randint(100,110)
            for j in range(lungime):
                x=random.randint(1,100)
                l.append(x)
            CombSort(l, key=lambda x:x, cmp=None, reversed=True)
            for i in range(len(l)-1):
                self.assertTrue(l[i]<=l[i+1])
            print(l)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInsertionSort']
    unittest.main()
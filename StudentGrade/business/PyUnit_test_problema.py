
import unittest
from domain.validare_problema import valid_problema, ValidationError
from Repository.repository_problema import repo_problema
from business.problema_service import problema_service


class Test(unittest.TestCase):


    def setUp(self):
        val=valid_problema()
        repo=repo_problema()
        self.ctr=problema_service(repo,val)
        self.ctr.adauga_problema("1_1", "descriere", "12.12.2018")


    def tearDown(self):
        pass


    def testAdauga(self):
        self.assertTrue(self.ctr.getNumarProbleme()==1)
        self.assertRaises(ValidationError,self.ctr.adauga_problema ,"", "", "")
        
        
    def testSterge(self):
        self.assertTrue(self.ctr.getNumarProbleme()==1)
        self.ctr.stergeProblema("1_1")
        self.assertTrue(self.ctr.getNumarProbleme()==0)

    def testActualizeaza(self):
        pr=self.ctr.adauga_problema("1_2","descriere","15.10.2018")
        self.ctr.actualizeaza_problema("1_2", "descriereNoua", "14.10.2018")
        self.assertTrue(pr.get_descriere()=="descriereNoua")
        self.assertTrue(pr.get_deadline()== "14.10.2018")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
import unittest
from business.student_service import student_service
from Repository.repository_student import repo_student, DuplicatedIdError
from domain.validare_student import valid_student, ValidationError


class Test(unittest.TestCase):


    def setUp(self):
        val=valid_student()
        repo=repo_student()
        self.ctr=student_service(repo,val)
        self.ctr.adauga_student(1, "Ion", 7)
        self.ctr.adauga_student(2, "Mihai", 7)

    def tearDown(self):
        pass

    def testAdauga(self):
        
        self.assertTrue(self.ctr.getNumarStudenti()==2)
        self.assertRaises(ValidationError,self.ctr.adauga_student,5, "ion", 0)
        self.assertRaises(DuplicatedIdError,self.ctr.adauga_student,2,"Andrei",4) 
        
    
    def testSterge(self):
        self.assertTrue(self.ctr.getNumarStudenti()==2)
        self.ctr.stergeStudent(1)
        self.assertTrue(self.ctr.getNumarStudenti()==1)

    
    def testActualizeaza(self):
        st=self.ctr.adauga_student(4, "Andrei", 2)
        self.assertTrue(self.ctr.getNumarStudenti()==3)
        self.ctr.actualizeaza_student(4, "Adi", 4)
        self.assertTrue(st.get_nume()=="Adi")
        self.assertTrue(st.get_grup()==4)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
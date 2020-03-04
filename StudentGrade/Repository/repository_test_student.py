from Repository.repository_student import repo_student
from domain.Student import student

def test_create_repo():
    repo_st=repo_student()
    assert repo_st.getNumar()==0
    
def test_adauga_repo_student():
    repo_st=repo_student()
    st = student(12,'Ion', 30)
    repo_st.adauga_repo_student(st)
    assert repo_st.getNumar() == 1
    st2 = student(1,'Ana', 88)
    repo_st.adauga_repo_student(st2)
    assert repo_st.getNumar() == 2
    
def test_sterge_repo_student():
    repo_st=repo_student()
    st = student(12,'Ion', 30)
    repo_st.adauga_repo_student(st)
    repo_st.sterge_repo_student(st.get_studentID())
    assert repo_st.getNumar() == 0

def test_actualizeaza_repo_student():
    repo_st=repo_student()
    st = student(12,'Ion', 30)
    nume_nou='Ana'
    grup_nou= 88
    repo_st.adauga_repo_student(st)
    repo_st.actualizeaza_repo_student(st.get_studentID(),nume_nou,grup_nou)
    assert st.get_nume()==nume_nou
    assert st.get_grup()==grup_nou
    
def testGetToti():
    repo_st=repo_student()
    st = student(12,'Ion', 30)
    st1 = student(1,'Ana', 88)
    repo_st.adauga_repo_student(st)
    repo_st.adauga_repo_student(st1)
    lista = repo_st.getToti()
    assert lista == [st,st1]
    
def run_tests():
    test_adauga_repo_student()
    test_sterge_repo_student()
    test_actualizeaza_repo_student()
    testGetToti()

run_tests()
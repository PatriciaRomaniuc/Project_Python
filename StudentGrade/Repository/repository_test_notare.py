from Repository.repository_notare import repo_notare
from domain.Notare import notare
from domain.Student import student
from domain.Problema import problema

def test_create_repo():
    repo_not=repo_notare()
    assert repo_not.getNumar()==0
    
def test_adauga_repo_notare():
    repo_not=repo_notare()
    st = student(12,'Ion', 30)
    pr = problema("12_2","descriere","02.08.2018")
    nota=notare(st,pr,8)
    repo_not.adauga_repo_nota(nota)
    assert repo_not.getNumar() == 1
    
def test_sterge_repo_notare():
    repo_not=repo_notare()
    st = student(12,'Ion', 30)
    pr = problema("12_2","descriere","02.08.2018")
    nota=notare(st,pr,8)
    repo_not.adauga_repo_nota(nota)
    id=str(st.get_studentID())+" "+str(pr.get_nrLab_nrPr())
    repo_not.sterge_repo_nota(nota.get_id())
    assert repo_not.getNumar() == 0

def test_actualizeaza_repo_notare():
    repo_not=repo_notare()
    st = student(12,'Ion', 30)
    pr = problema("12_2","descriere","02.08.2018")
    nota=notare(st,pr,8)
    repo_not.adauga_repo_nota(nota)
    notaNoua=9
    repo_not.actualizeaza_repo_nota(nota.get_id(), notaNoua)
    assert nota.get_nota()==9
    
def testGetToti():
    repo_not=repo_notare()
    st = student(12,'Ion', 30)
    pr = problema("12_2","descriere","02.08.2018")
    nota1=notare(st,pr,8)
    repo_not.adauga_repo_nota(nota1)
    st = student(2,'Andrei', 29)
    pr = problema("2_2","descriere","12.10.2018")
    nota2=notare(st,pr,6)
    repo_not.adauga_repo_nota(nota2)
    lista = repo_not.getToti()
    assert lista == [nota1,nota2]
    
def run_tests():
    test_adauga_repo_notare()
    test_sterge_repo_notare()
    test_actualizeaza_repo_notare()
    testGetToti()

run_tests()
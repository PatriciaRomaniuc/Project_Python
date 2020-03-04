from Repository.repository_problema import repo_problema
from domain.Problema import problema

def test_create_repo():
    repo_pr=repo_problema()
    assert repo_pr.getNumar()==0
    
def test_adauga_repo_problema():
    repo_pr=repo_problema()
    pr = problema("12_2","descriere","02.08.2018")
    repo_pr.adauga_repo_problema(pr)
    assert repo_pr.getNumar() == 1
    pr1 = problema("12_3","descriere","02.08.2018")
    repo_pr.adauga_repo_problema(pr1)  
    assert repo_pr.getNumar() == 2
    
def test_sterge_repo_problema():
    repo_pr=repo_problema()
    pr = problema("12_2","descriere","02.08.2018")
    repo_pr.adauga_repo_problema(pr)
    repo_pr.sterge_repo_problema(pr.get_nrLab_nrPr())
    assert repo_pr.getNumar() == 0

def test_actualizeaza_repo_problema():
    repo_pr=repo_problema()
    pr = problema("12_2","descriere","02.08.2018")
    desc_noua="descriereNoua"
    deadline_nou="09.09.2018"
    repo_pr.adauga_repo_problema(pr)
    repo_pr.actualizeaza_repo_problema(pr.get_nrLab_nrPr(),desc_noua,deadline_nou)
    assert pr.get_descriere()==desc_noua
    assert pr.get_deadline()==deadline_nou
    
def testGetToti():
    repo_pr=repo_problema()
    pr = problema("12_2","descriere","02.08.2018")
    pr1 = problema("12_9","descriere","09.09.2018")
    repo_pr.adauga_repo_problema(pr)
    repo_pr.adauga_repo_problema(pr1)
    lista = repo_pr.getToti()
    assert lista == [pr,pr1]
    
def run_tests():
    test_adauga_repo_problema()
    test_sterge_repo_problema()
    test_actualizeaza_repo_problema()
    testGetToti()

run_tests()
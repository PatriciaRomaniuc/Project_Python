from Repository.repository_problema import repo_problema
from domain.Problema import problema

class problemaFileRepo(repo_problema):
    
    def __init__(self,fileName):
        repo_problema.__init__(self)
        self.__fileName=fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        try:
            f=open(self.__fileName,'r')
        except IOError:
            return
        
        for line in f.readlines():
            if line!="":
                line=line.strip()
                data=line.split(" ")
                nrPr_nrLab=data[0]
                descriere=data[1]
                deadline=data[2]
                pr=problema(nrPr_nrLab,descriere,deadline)
                repo_problema.adauga_repo_problema(self, pr)
        f.close()
        
    def __appendToFile(self,pr):
        f=open(self.__fileName,"a")
        f.write("\n")
        f.write(pr.get_nrLab_nrPr()+" "+pr.get_descriere()+" "+pr.get_deadline())
        f.close()
        
    def __writeToFile(self,prbs):
        f = open(self.__fileName, "w")
        for pr in prbs:
            f.write(pr.get_nrLab_nrPr()+" "+pr.get_descriere()+" "+pr.get_deadline())
        f.close()
        
    def adauga_repo_problema(self,elem):
        repo_problema.adauga_repo_problema(self, elem)
        self.__appendToFile(elem)
        
    def sterge_repo_problema(self,id):
        repo_problema.sterge_repo_problema(self, id)
        prbs=repo_problema.getToti(self)
        self.__writeToFile(prbs)
        
    def actualizeaza_repo_problema(self,id,descriereNoua, deadlineNou):
        repo_problema.actualizeaza_repo_problema(self, id, descriereNoua, deadlineNou)
        prbs=repo_problema.getToti(self)
        self.__writeToFile(prbs)
        
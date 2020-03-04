
from domain.Problema import problema
from domain.validare_problema import ValidationError

class problema_service(object):
                     
    def __init__(self, __repo, __validator):
        self.__repo = __repo
        self.__validator = __validator

    def adauga_problema(self,__nrLab_nrPr,__descriere,__deadline):
        '''
        Functie ce adauga o problema, o valideaza si adauga in repository
        :param __nrLab_nrPr: numarul laboratorului si  numarul problemei-string
        :param __descriere: descrierea problemei -string
        :param __deadline: deadline-ul problemei- string
        '''
        pr=problema(__nrLab_nrPr,__descriere,__deadline)
        
        self.__validator.validate(pr)
        self.__repo.adauga_repo_problema(pr)
        
        return pr
        
    def getProblemaByID(self,id):
            return self.__repo.getByNrLab_nrPr(id)
    def getProblema(self):
        '''
        Functie ce returneaza toate problemele
        '''
        l = self.__repo.getToti()
        return l
    def getNumarProbleme(self):
        l = self.__repo.getToti()
        return len(l)
    def actualizeaza_problema(self,nrLab_nrPr,descriereNoua,deadlineNou):
        '''
        Functie ce actualizeaza o problema
        :param pr:problema ce trebuie actualizata-problema
        :param nrLab_nrPrNou: numarul si laboratorul nou-string
        :param descriereNoua: descrierea noua-string
        :param deadlineNou: deadline-ul nou-string
        '''
        self.__repo.actualizeaza_repo_problema(nrLab_nrPr,descriereNoua,deadlineNou)

    def stergeProblema(self, nrLab_nrPr):
        '''
        Functie ce sterge o problema
        :param pr: problema ce trebuie stearsa-problema
        '''
        self.__repo.sterge_repo_problema(nrLab_nrPr)

        


class RepoError(Exception):
    pass

class repo_problema(object):
    
    def __init__(self):
        self.__elems =[]
    
    def getNumar(self):
        return len(self.__elems)

    def getToti(self):
        return self.__elems
    
    def getByNrLab_nrPr(self, nrLab_nrPr):
        for i in range(self.getNumar()):
            if self.__elems[i].get_nrLab_nrPr() == nrLab_nrPr:
                
                return self.__elems[i]
        return None
    def adauga_repo_problema(self,elem):
        '''
        Functie ce adauga o problema in repository
        :param elem:un element al listei -problema
        '''
        l=self.getToti()
        if elem in l:
            raise RepoError("Elementul exista!")
        self.__elems.append(elem)
        
    def sterge_repo_problema(self,nrLab_nrPr):
        '''
        Functie ce sterge o problema din repository
        :param nrLab_nrPr:
        '''
        problema=self.getByNrLab_nrPr(nrLab_nrPr)
        if self.__elems.__contains__(problema):
            self.__elems.remove(problema)
        
    def actualizeaza_repo_problema(self, nrLab_nrPr,descriereNoua,deadlineNou):
        '''
        Functie ce actualizeaza o problema in repository
        :param nrLab_nrPr:
        :param descriereNoua:
        :param deadlineNou:
        '''
        problema=self.getByNrLab_nrPr(nrLab_nrPr)
        problema.set_descriere(descriereNoua)
        problema.set_deadline(deadlineNou)

   

    
    




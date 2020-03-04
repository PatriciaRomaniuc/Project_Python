class RepoError(Exception):
    pass
class repo_notare(object):
    
    def __init__(self):
        self._elems =[]
    
    def getNumar(self):
        return len(self._elems)

    def getToti(self):
        return self._elems
    
    def getById(self, id):
        for i in range(self.getNumar()):
            if self._elems[i].get_id() == id:
                return self._elems[i]
        return None
        
    def adauga_repo_nota(self,elem):
        '''
        Functie ce adauga o nota in repository
        :param elem:lista de note
        '''
        if elem in self._elems:
            raise RepoError("Elementul exista!")
        self._elems.append(elem)
        
    def sterge_repo_nota(self, id):
        notare=self.getById(id)
        if (self._elems.__contains__(notare)):
            self._elems.remove(notare)  
              
    def actualizeaza_repo_nota(self, id, notaNoua):
        '''
        Functie ce actualizeaza o nota in repository
    
        '''
        notare=self.getById(id)
        notare.set_nota(notaNoua)
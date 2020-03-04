from domain.Student import student

class DuplicatedIdError(Exception):
    pass
class repo_student(object):
    
    def __init__(self):
        self.__elems =[]
    
    def getNumar(self):
        return len(self.__elems)

    def getToti(self):
        return self.__elems

    def adauga_repo_student(self,elem):
        
        l=self.getToti()
        for el in l:
            if el.get_studentID()==elem.get_studentID():
                errors="Id-ul trebuie sa fie unic"
                raise DuplicatedIdError(errors)
        
        self.__elems.append(elem)
        
    def actualizeaza_repo_student(self, studentID, numeNou,grupNou):
        student=self.getById(studentID,0)
        student.set_nume(numeNou)
        student.set_grup(grupNou) 
    
    def sterge_repo_student(self, studentID):
        student=self.getById(studentID,0)
        if (self.__elems.__contains__(student)):
            self.__elems.remove(student)

    def getById(self, studentID,indice):
        '''
        Functie recursiva ce returneaza studentul corespunzator id-ului dat. 
        :param studentID: id-ul studentului -int 
        :param indice: indicele elementului curent din lista 
        '''
        if indice>=len(self.__elems):
            return None
        if self.__elems[indice].get_studentID() == studentID:
                return self.__elems[indice]
        indice+=1
        return self.getById(studentID, indice)
    
    def cauta_repo_student(self,elem,indice):
        '''
        Functie recursiva de cautare 
        :param elem: elementul cautat
        :param indice: indicele elementului curent din lista 
        '''
        if elem not in self.__elems:
            raise DuplicatedIdError("Element inexistent!")
        if indice>=len(self.__elems):
            return None
        if self.__elems[indice]==elem:
            return elem
        indice+=1
        return self.cauta_repo_student(elem, indice)
      
    
        


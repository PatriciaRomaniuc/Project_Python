from business import sortari
from domain.Student import student
import random
from Repository import repository_student
from domain.validare_student import ValidationError, valid_student
class student_service(object):
                     
    def __init__(self, __repo, __validator):
        self.__repo = __repo
        self.__validator = __validator

    def adauga_student(self,__studentID,__nume,__grup):
        '''
        Functie ce adauga un student, il valideaza si adauga in repository
        :param __studentID:id-ul studentului-int
        :param __nume:numele studentului-string
        :param __grup:grupul studentului-int
        '''
        st= student(__studentID,__nume,__grup)
        
        self.__validator.validate(st)
        self.__repo.adauga_repo_student(st)
        
        return st
    
    def getStudenti(self):
        '''
        Functie ce retuneaza toti studentii
        '''
        l = self.__repo.getToti()
        return l
    def getNumarStudenti(self):
        '''
        Functie ce returneaza numarul de studenti
        '''
        l=self.getStudenti()
        return len(l)
    
    def getStudentById(self,id):
        student=self.__repo.getById(id,0)
        return student
    
    def actualizeaza_student(self,studentID, numeNou, grupNou):
        '''
        Functie ce actualizeaza un student
        :param studentID: id-ul stundentului ce trebuie actualizat-int
        :param numeNou: numele nou-string
        :param grupNou:grupul nou-int
        '''
        self.__repo.actualizeaza_repo_student(studentID, numeNou, grupNou)

    def stergeStudent(self, studentID):
        '''
        Functie ce sterge un student 
        :param studentID: id-ul studentuluis
        '''
        self.__repo.sterge_repo_student(studentID)
    
    def genereaza_random(self,n):
        '''
        Functie ce genereaza random un numar de n studenti
        :param n: numarul cerut de studenti-int
        '''
        l=[]
        Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet='abcdefghijklmnopqrstuvwxyz'
        for x in range(n):
            lungime=random.randint(2,7)
            studentID= random.randint(1,101)
            grup=random.randint(1,101)
            nume=''
            nume+=random.choice(Alphabet)
            for i in range(lungime):
                nume+=random.choice(alphabet)
            st=student(studentID,nume,grup)
            l.append(st)
        return l

    
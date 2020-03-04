from domain.StudentProblema import StudentProblema
from domain.Notare import notare
from business.sortari import InsertionSort,key_alfabetic,key_note

class notare_service(object):
    def __init__(self,__repo,__validator,Repo_st,Repo_pr):
        self.__repo = __repo
        self.__validator = __validator
        self.Repo_st = Repo_st
        self.Repo_pr = Repo_pr
        
    
    def adauga_nota(self,__student,__problema,__nota):
        '''
        Functie ce adauga o nota, o valideaza si o adauga in repository
        :param __student: student
        :param __problema:problema
        :param __nota: nota-float
        '''
        n =notare(__student,__problema,__nota)
        self.__validator.validate(n)
        self.__repo.adauga_repo_nota(n)
        
    def getNote(self):
        '''
        Functie ce retuneaza toate notele
        '''
        l = self.__repo.getToti()
        return l
    
    def sterge_notare(self,id):
        '''
        FUnctie care sterge o notare 
        '''
        self.__repo.sterge_repo_nota(id)
        
    def actualizeaza_notare(self,id,notaNoua):
        '''
        functie care actualizeaza o nota
        :param id: id-int
        :param notaNoua: int
        '''
        self.__repo.actualizeaza_notare(id,notaNoua)
    
    
    def sorteaza(self):
        '''
        Functie care sorteaza alfabetic dupa studenti, dupa medie
        '''
        l=self.getNote()
        InsertionSort(l,key=key_alfabetic,cmp=None,reversed=True)
        InsertionSort(l,key=key_note,cmp=None, reversed=True)
        
        return l 
    
    def medie_note(self,student):
        '''
        Functie care calculeaza media notelor unui student
        :param student:
        '''
        l=self.getNote()
        suma = 0
        numar = 0
        for i in range(len(l)):
            if l[i].get_student() == student:
                suma += int(l[i].get_nota())
                numar += 1
        if numar == 0:
            return -1
        else:
            return suma/numar
        
    def studenti_medie_note_5(self):
        '''
        Functie care returneaza lista de studenti ce au media notelor sub 5
        '''
        
        l=self.getNote()
        studenti=[]
        for i in range(len(l)):
            if self.medie_note(l[i].get_student()) < 5 : 
                studenti.append(l[i])
        return studenti
        
    
    def getAllDescInDescriere(self,desc):
        '''
        Functie care returneaza o lista de entitati StudentProblema pentru probleme ce contin descrierea desc
        :param desc: string- descrierea ceruta
        output: rez-lista de entitati
        '''
        rez=[]
        notari=self.getNote()
        for n in notari:
            if desc in n.get_problema().get_descriere():
                sp=StudentProblema(n.get_student().get_studentID(),1,n.get_student().get_nume())
                found=False
                for n in rez:
                    if n.get_studentID()==sp.get_studentID():
                        n.set_nr_problema(n.get_nr_problema()+1)
                        found=True
                if found==False:
                    rez.append(sp)
        return rez
    
    def entitateaXCuCeiMaiMultiY(self,desc):
        '''
        Metoda care returneaza entitatea StudentProblema cu cele mai multe probleme care contin descrierea desc
        Input: desc- string
        Output: sp-StudentProblema, daca s-a gasit un astfel de obiect
                None - in caz contrar
        '''
    
        sps=self.getAllDescInDescriere(desc)
        if len(sps)==0:
            return None
        maxim=-1
        sp = sps[0]
        for elem in sps:
            if elem.get_nr_probleme() > maxim:
                maxim = elem.get_nr_probleme()
                sp = elem
        return sp
            
    


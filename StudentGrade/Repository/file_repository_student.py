from Repository.repository_student import repo_student
from domain.Student import student

class student_repo_file():
    '''
    
    '''
    def __init__(self,fileName):
        self.__fileName=fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        
        try:
            f=open(self.__fileName,"r")
        except IOError:
            return 
        rez=[]
        for line in f.readlines():
            if line!="":
                data=line.split(" ")
                studentID=data[0]
                nume=data[1]
                grup=data[2]
                st=student(studentID, nume, grup)
                rez.append(st)
        f.close() 
        return rez 
    def __writeToFile(self,sts):
        f = open(self.__fileName, "w")
        for st in sts:
            f.write(str(st.get_studentID())+" "+st.get_nume()+" "+str(st.get_grup()))
        f.close()
    
    def __appendToFile(self,st):
        f=open(self.__fileName,"a")
        f.write("\n")
        f.write(str(st.get_studentID())+" "+st.get_nume()+" "+str(st.get_grup()))
        f.close()
    
    def adauga_repo_student(self,st):
        all=self.__loadFromFile()
        all.append(st)
        self.__appendToFile(st)
        
    def sterge_repo_student(self,st):
        all.self.__loadFromFile()
        
        all.remove(st)
        self.__writeToFile(all)
        
    def actualizeaza_repo_student(self,elem,numeNou,grupNou):
        all=self.__loadFromFile()
        elem.set_nume(numeNou)
        elem.set_grup(grupNou)
        
        self.__writeToFile(all)

def test_repo():
    fileName="test.txt"
    repo=student_repo_file(fileName)
    assert repo.getNumar()==0
    repo.adauga_repo_student(student(5,"Andrei",9))
    assert repo.getNumar()==1

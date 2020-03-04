from Repository.repository_notare import repo_notare
from domain.Notare import notare
class NotareFileRepository(repo_notare):

    def __init__(self,fileName):
        repo_notare.__init__(self)
        self.__fileName=fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):

        try:
            f=open(self.__fileName,"r")
        except IOError:
            return
        for line in f.readlines():
            if line!="":
                data=line.split(",")
                student=data[0]
                problema=data[1]
                nota=data[2]
                Notare=notare(student,problema,nota)
                repo_notare.adauga_repo_nota(self, Notare)
        f.close()
        
    def __appendToFile(self,elem):
        f=open(self.__fileName,"a")
        f.write("\n")
        f.write(elem.get_student()+","+elem.get_problema()+","+str(elem.get_nota()))
        f.close()   
          
    def __writeToFile(self,note):
        f = open(self.__fileName, "w")
        for nota in note:
            f.write("\n")
            f.write(nota.get_student()+","+nota.get_problema()+","+str(nota.get_nota()))
        f.close()     
        
    def adauga_repo_nota(self,elem):
        repo_notare.adauga_repo_nota(self, elem)
        self.__appendToFile(elem)
        
    def sterge_repo_nota(self,id):
        repo_notare.sterge_repo_nota(self,id)
        note=repo_notare.getToti(self)
        self.__writeToFile(note)
        
    def actualizeaza_repo_nota(self,id,notaNoua):
        repo_notare.actualizeaza_repo_nota(self, id, notaNoua)
        note=repo_notare.getToti(self)
        self.__writeToFile(note)


    
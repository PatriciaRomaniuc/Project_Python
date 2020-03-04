class notare(object):
    
    def __init__(self,__student,__problema,__nota):
        '''
        Initializeaza notarea (clasa de legatura)
        :param __student: student
        :param __problema: problema
        :param __nota: float
        '''
        self.__student = __student
        self.__problema = __problema
        self.__nota=__nota
        
    def get_id(self):
        return str(str(self.__student.get_studentID())+" "+self.__problema.get_nrLab_nrPr())
    
    def get_nota(self):
        return self.__nota

    def set_nota(self, value):
        self.__nota = value


    def __str__(self):
        '''
        Converteste in string
        '''
        
        return str(self.__student)+","+str(self.__problema)+","+str(self.__nota)
        

    def get_student(self):
        return self.__student


    def get_problema(self):
        return self.__problema


    def set_student(self, value):
        self.__student = value


    def set_problema(self, value):
        self.__problema = value
    

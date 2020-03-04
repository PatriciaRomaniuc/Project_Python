class student(object):
    
    def __init__(self,__studentID,__nume,__grup):
        '''
        Initializeaza studentul
        :param __studentID: int
        :param __nume: string
        :param __grup: int
        '''
        self.__studentID=__studentID
        self.__nume=__nume
        self.__grup=__grup
        
    def get_studentID(self):
        '''
        Functie care returneaza studentID-ul unui student
        '''
        return self.__studentID
    
    def get_nume(self):
        '''
        Functie care returneaza numele unui student
        '''
        return self.__nume
    
    def get_grup(self):
        '''
        Functie care returneaza grupul din care face parte studentul
        '''
        return self.__grup
    
    def set_studentID(self,value):
        '''
        Functie care seteaza sau modifica studentID-ul unui student
        '''
        self.__studentID=value
        
    def set_nume(self,value):
        '''
        Functie care seteaza sau modifica numele unui student
        '''
        self.__nume=value
        
    def set_grup(self,value):
        '''
        Functie care seteaza sau modifica grupul din care face parte studentul
        '''
        self.__grup=value
        
    def __str__(self):
        '''
        Converteste in string
        '''
        
        return str(self.__studentID)+" "+self.__nume+" "+str(self.__grup)



    
class problema(object):
    
    def __init__(self,__nrLab_nrPr,__descriere,__deadline):
        '''
        Initializeaza problema
        :param __nrLab_nrPr: string
        :param __descriere:string
        :param __deadline:string
        '''
        self.__nrLab_nrPr=__nrLab_nrPr
        self.__descriere=__descriere
        self.__deadline=__deadline
        
    def __str__(self):
        '''
        Converteste in string
        '''
        
        return self.__nrLab_nrPr+" "+self.__descriere+" "+self.__deadline
   
    def get_nrLab_nrPr(self):
        '''
        Functie care returneaza numarul laboratorului si numarul problemei 
        '''
        
        return self.__nrLab_nrPr
    
    def get_descriere(self):
        '''
        Functie care returneaza descrierea unei probleme
        '''
        return self.__descriere
    
    def get_deadline(self):
        '''
        Functie care returneaza deadline-ul unei probleme
        '''
        return self.__deadline
    
    def set_nrLab_nrPr(self,value):
        self.__nrLab_nrPr=value
        
    def set_descriere(self,value):
        self.__descriere=value
        
    def set_deadline(self,value):
        self.__deadline=value  
    
class StudentProblema():
    '''
    Entitate student-problema pentru raportul 4 -DTO
    '''
    
    def __init__(self,__studentID,__nr_probleme,__nume):
        '''
        
        :param __studentID: int- id-ul studentului
        :param __nr_probleme: int- numarul de probleme
        :param __nume: string- numele studentului
        '''
        self.__studentID = __studentID
        self.__nr_probleme = __nr_probleme
        self.__nume = __nume

    def get_student_id(self):
        return self.__studentID


    def get_nr_probleme(self):
        return self.__nr_probleme


    def get_nume(self):
        return self.__nume


    def set_student_id(self, value):
        self.__studentID = value


    def set_nr_probleme(self, value):
        self.__nr_probleme = value


    def set_nume(self, value):
        self.__nume = value


    
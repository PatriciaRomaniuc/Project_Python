class ValidationError(Exception):
    pass
class valid_notare(object):
    def validate(self,notare):
        '''
        Functia care valideaza entitatea notare
         
        :param nota: nota
        '''
        errors = []
        if notare.get_nota()=="": 
            errors.append("Nota invalida")
        if (notare.get_student()==""): 
            errors.append("Studentul nu poate fi nul!")
        if (notare.get_problema()==""): 
            errors.append("Problema nu poate fi nula!")
        if len(errors)>0:
            raise ValidationError (errors)



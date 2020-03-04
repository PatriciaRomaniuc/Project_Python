
class ValidationError(Exception):
    pass

class valid_problema(object):
    
    def validate(self, pr):
        '''
        Functie care valideaza problema data
        in:pr
        pre:pr-problema
        out: ValueError
        post:ValueError-string de erori
        '''
        errors = ""
        if pr.get_nrLab_nrPr()=="":
            errors+="Numarul laboratorului nu poate fi nul!\n"
            
        #validare_descriere(pr.get_descriere())
        if pr.get_descriere()=="":
            errors+="Descrierea nu poate fi nula!\n"       
        if pr.get_deadline()=="":
            errors+="Deadline-ul nu poate fi nul!\n"
        if len(errors)>0:
            raise ValidationError(errors)





class ValidationError(Exception):
    pass

class valid_student(object):
    
    def validate(self, st):
        '''
        Functie care valideaza studentul dat
        in:st
        pre:st-student
        out: ValueError
        post:ValueError-string de erori
        '''
        errors = ""
        if int(st.get_studentID())<=0 and int(st.get_studentID())>=1000000000:
            errors+="studentID invalid!\n"
        if st.get_nume()=="":
            errors+="Numele studentului nu poate fi un string vid!\n"
        if st.get_grup()==0:
            errors+="Grupul nu poate fi nul!\n"
        if len(errors)>0:
            raise ValidationError(errors)



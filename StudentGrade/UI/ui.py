class ui(object):
    
    def __init__(self, __student_service,__problema_service,__notare_service):
        self.__student_service = __student_service
        self.__problema_service = __problema_service
        self.__notare_service = __notare_service
        
    def ui_print_student(self):
        '''
        Functie apelata in meniu pentru printarea unui student
        '''
        studenti=self.__student_service.getStudenti()
        print(studenti)
        if len(studenti) == 0:
            print("Nu exista studenti")
        else:
            print("studentID    Nume   Grup")
        for st in studenti:
            print(st.__str__())
            
    def ui_add_student(self):
        '''
        Functie apelata in meniu pentru adaugarea unui student

        '''
        studentID = input("Dati id-ul studentului:")
        nume = input("Dati numele studentului:")
        grup = input("Dati grupul studentului:")
        self.__student_service.adauga_student(studentID, nume, grup)
        
    def ui_actualizeaza_student(self):
        '''
        Functie apelata in meniu pentru actualizarea unui student

        '''
        studentID= input("Dati id-ul studentului:")
        numeNou=input("Dati numele nou:")
        grupNou=input("Dati grupul nou:")
        self.__student_service.actualizeaza_student(studentID,numeNou,grupNou)
    
    def ui_sterge_student(self):
        '''
        Functie apelata in meniu pentru stergerea unui student

        '''
        studentID= input("Dati id-ul studentului:")
        self.__student_service.stergeStudent(studentID)
    
    def ui_add_problema(self):
        '''
        Functie apelata in meniu pentru adaugarea unei probleme
        '''
        nrLab_nrPr=input("Dati numar laboratorului_numarul problemei:")
        nrLab_nrPr.strip(' ')
        descriere=input("Dati descrierea problemei:")
        deadline=input("Dati deadline-ul problemei:")
        self.__problema_service.adauga_problema(nrLab_nrPr, descriere, deadline)
    
    def ui_print_problema(self):
        '''
        Functie apelata in meniu pentru printarea unei probleme
        '''
        probleme=self.__problema_service.getProblema()
        if len(probleme) == 0:
            print("Nu exista probleme")
        else:
            print("nrLab_nrPr  descriere  deadline")
        for pr in probleme:
            print(pr.__str__())
    
    def ui_actualizeaza_problema(self):
        '''
        Functie apelata in meniu pentru actualizare unei probleme
        '''
        nrLab_nrPr=input("Dati numarul laboratorului_numarul problemei ce trebuie actualizat:")
        descriereNou=input("Dati noua descriere a problemei:")
        deadlineNou=input("Dati noul deadline-ul al problemei:")
        self.__problema_service.actualizeaza_problema(nrLab_nrPr,descriereNou,deadlineNou)
    
    def ui_sterge_problema(self):
        '''
        Functie apelata in meniu pentru stergerea unei probleme
        '''
        nrLab_nrPr=input("Dati numarul laboratorului_numarul problemei ce trebuie sters:")
        
        self.__problema_service.stergeProblema(nrLab_nrPr)
    
    def ui_genereaza_random(self):
        n=int(input("Dati numarul de studenti dorit(n):"))
        l=self.__student_service.genereaza_random(n)
        for el in l:
            print(el)
        

    def ui_add_notare(self):
        '''
        Functia apelata in meniu pentru adaugarea unei notari
        '''
        studentID=input("Dati id-ul studentului:")
        student=self.__student_service.getStudentById(studentID)
        nrLab_nrPr=input("Dati numarul laboratorului_numarul problemei:")
        problema=self.__problema_service.getProblemaByID(nrLab_nrPr)
        nota=input("Dati nota:")
        self.__notare_service.adauga_nota(student,problema, nota)
    
    
    def ui_print_notare(self):
        '''
        Functia apelata in meniu pentru printarea  notarilor 
        '''
        note=self.__notare_service.getNote()
        if len(note)==0:
            print("Nu exista note!")
        else:
            for nota in note:
                print(nota.__str__())
    
    def ui_actualizeaza_notare(self):
        '''
        Functia apelata in meniu pentru actualizarea unei notari

        '''
        id=input("Dati id-ul notarii:")
        notaNoua=input("Dati nota noua:")
        self.__notare_service.actualizeaza_notare(id, notaNoua)
    
    def ui_sterge_notare(self):
        '''
        Functia apelata in meniu pentru stergerea unei notari

        '''
        id=input("Dati id-ul notarii:")
        self.__notare_service.sterge_notare(id)

    def ui_studenti_note_sub5(self):
        '''
        
        '''
        lista=self.__notare_service.studenti_medie_note_5()
        for el in lista:
            print(str(el))
        
    def ui_sortare(self):
        '''
        
        '''
        l=self.__notare_service.sorteaza()
        for el in l:
            print(str(el))
        
    def ui_printSP(self, sp):
        if sp == None:
            print("Nu s-a gasit nicun student!")
        else:
            print(sp.get_nume() + " are " + str(sp.get_nr_probleme()) + " probleme care au descrierea data.")
        
    def ui_raport(self):
        desc = input("Introduceti descrierea: ")
        sp = self.__notare_service.entitateaXCuCeiMaiMultiY(desc)
        self.ui_printSP(sp)
              
    def meniu_principal(self):
        print("----Meniu----")
        print("1.Adauga")
        print("2.Printeaza")
        print("3.Actualizeaza")
        print("4.Sterge")
        print("5.Generare random")
        print("6.Rapoarte")
        print("7.EXIT")
    def meniu_adauga(self):
        print("1.Adauga student")
        print("2.Adauga problema")
        print("3.Adauga nota")
    def meniu_printeaza(self):
        print("1.Printeaza toti studentii")
        print("2.Printeaza toate problemele")
        print("3.Printeaza note")
    def meniu_actualizeaza(self):
        print("1.Actualizeaza student")
        print("2.Actualizeaza problema")
        print("3.Actualizeaza notare")
    def meniu_sterge(self):
        print("1.Sterge student")
        print("2.Sterge problema")
        print("3.Sterge notare")
    def meniu_rapoarte(self):
        print("1.Sorteaza alfabetic si dupa note")
        print("2.Afiseaza studentii cu note sub 5")
        print("3.Raport lab 9")
    def run(self):
        while True:
            self.meniu_principal()
            comanda=int(input("Alegeti o comanda:"))
            if comanda==1:
                self.meniu_adauga()
                cmd=int(input("Alegeti o comanda:"))
                if cmd==1:
                    self.ui_add_student()
                elif cmd==2:
                    self.ui_add_problema()
                elif cmd==3:
                    self.ui_add_notare()
                else:
                    print("Comanda introdusa nu exista!")
            elif comanda==2:
                self.meniu_printeaza()
                cmd=int(input("Alegeti o comanda:"))
                if cmd==1:
                    self.ui_print_student()
                elif cmd==2:
                    self.ui_print_problema()
                elif cmd==3:
                    self.ui_print_notare()
                else:
                    print("Comanda introdusa nu exista!")
            elif comanda==3:
                self.meniu_actualizeaza()
                cmd=int(input("Alegeti o comanda:"))
                if cmd==1:
                    self.ui_actualizeaza_student()
                elif cmd==2:
                    self.ui_actualizeaza_problema()
                elif cmd==3:
                    self.ui_actualizeaza_notare()
                else:
                    print("Comanda introdusa nu exista!")
            elif comanda==4:
                self.meniu_sterge()
                cmd=int(input("Alegeti o comanda:"))
                if cmd==1:
                    self.ui_sterge_student()
                elif cmd==2:
                    self.ui_sterge_problema()
                elif cmd==3:
                    self.ui_sterge_notare()
                else:
                    print("Comanda introdusa nu exista!")
            elif comanda==5:
                self.ui_genereaza_random()
            elif comanda==6:
                self.meniu_rapoarte()
                cmd=int(input("Alegeti o comanda:"))
                if cmd==1:
                    self.ui_sortare()
                elif cmd==2:
                    self.ui_studenti_note_sub5()
                elif cmd==3:
                    self.ui_raport()
            elif comanda==7:
                return
            else:
                print("Comanda introdusa nu exista!")
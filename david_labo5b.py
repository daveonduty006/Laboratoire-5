"""
Laboratoire 5:
Vous devez implémenter un système de facturation pour un garage automobile. Le système 
de facturation doit avoir la liste des véhicules et les réparations à faire.

Étape 1:
Créer le constructeur de la classe automobile. Votre automobile doit avoir les 
informations suivantes: Modèle, marque, année et couleur.

Étape 2:
Définir des méthodes permettant de retourner sous forme de string toutes les 
informations par rapport à l'automobile.

Étape 3:
Créer le constructeur de la classe réparations. Votre objet réparation contenir 
l'information par rapport au nom de la réparation, à son coût, au nombre d'heures de 
travail et si la travail a été faite.

Étape 4:
Définir une méthode permettant de retourner sous forme de string toutes les 
informations par rapport à la réparation.

Étape 5 :
Définir une classe système de facturation et l'instancier avec les 5 informations 
suivantes:
    Nissan Altima 2012 Bleu, Freins 800$ 6h non-fait
    Ford Taurus 2000 Vert, BieletteAv-G 200$ 4h fait
    Honda Civic 2020 Noir, Pare-Brise 1200$ 2h non-fait
    Ford Escape 2011 Gris, Démarreur 800$ 5h non-fait
    Toyota Corolla 2002 Bleu, Installation de pneus 80$ 1h fait

Étape 6:
Définir des méthodes permettant, d'ajouter des réparations, d'enlever des réparations, 
d'avoir le nombre total d'heures de réparations faites, le revenu total des 
réparations faites, le revenu horaire moyen, le nombre d'heures total de réparations 
non faites, et le revenu total manqué des réparations non faites.

Étape 7:
Définir un menu permettant à un utilisateur de choisir une des options suivantes:
    ajouter ou enlever une réparation(en incluant les véhicules associés)
    voir la liste de réparations(en incluant les véhicules associés)
    voir le nombre total d'heures de réparations faites
    voir le revenu total de réparation faites
    voir le nombre d'heures total de réparations non-faites
    voir le revenu total manqué des réparations non-faites.
"""

"""
classe car
    attributs
        maker
        model
        origin
        color
    méthodes
        get_maker
        get_model
        get_origin
        get_color

classe reparation(car)
    attributs
        job_name
        job_cost
        job_length
        job_state
    méthodes
        get_job_name
        get_job_cost
        get_job_length
        get_job_state

classe facturation(reparation)
    méthodes
        add_job
        remove_job
        get_done_jobs_length
        get_done_jobs_cost
        get_pay_rate
        get_unfinished_jobs_length
        get_unfinished_jobs_cost

emp_menu():
    ajouter ou enlever une réparation(en incluant les véhicules associés)
    voir la liste de réparations(en incluant les véhicules associés)
    voir le nombre total d'heures de réparations faites
    voir le revenu total de réparation faites
    voir le nombre d'heures total de réparations non-faites
    voir le revenu total manqué des réparations non-faites.   
"""

class Car:

    def __init__(self, maker:str, model:str, year:int, color:str):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
 
    def __str__(self):
        return f"{self.maker} {self.model} {self.year} {self.color}"
           
class Repair:

    def __init__(self, job_name, job_cost, job_length, job_state): 
        self.job_name = job_name
        self.job_cost = job_cost
        self.job_length = job_length
        self.job_state = job_state

    def __str__(self):
        return f"{self.job_name} {self.job_cost} {self.job_length} {self.job_state}"

class Billing:
        
    def __init__(self, cars:list, jobs:list):
        self.cars = cars
        self.jobs = jobs

    def add_job(self):
        pass

    def display(self):
        i = 1
        for car, job in zip(self.cars, self.jobs):
            print(f"{i}. {car}: {job}")
            i += 1
            

    def menu(self):
        exit = False
        while not exit:
            user_sel = 0
            while not 1 <= user_sel <= 7:
                print("Menu des options: ")
                print("1. ajouter/enlever une réparation")
                print("2. voir liste des réparations")
                print("3. voir total des heures de réparations faites")
                print("4. voir revenu total de réparations faites")
                print("5. voir total des heures de réparations non-faites")
                print("6. voir revenu total manqué de réparations non-faites.")
                print("7. terminer")
                user_sel = int(input("Choix: "))
            if user_sel == 1:
                op_sel = 0
                while not 1 <= op_sel <= 2:
                    print("1. Ajouter une réparation à un véhicule")
                    print("2. Enlever une réparation à un véhicule")
                    op_sel = int(input("Choix: "))
                self.add_job(self.bills)
                


cars = []
cars.append(Car("Nissan","Altima",2012,"Bleu"))
cars.append(Car("Ford","Taurus",2000,"Vert"))
cars.append(Car("Honda","Civic",2020,"Noir"))
cars.append(Car("Ford","Escape",2011,"Gris"))
cars.append(Car("Toyota","Corolla",2002,"Bleu"))

jobs = []
jobs.append(Repair("Freins",800,6,"non-fait"))
jobs.append(Repair("BieletteAv-G",200,4,"fait"))
jobs.append(Repair("Pare-Brise",1200,2,"non-fait"))
jobs.append(Repair("Démarreur",800,5,"non-fait"))
jobs.append(Repair("Pneus",80,1,"fait"))

bills = Billing(cars, jobs)
bills.display()


        





"""classe facturation(reparation)
    méthodes
        add_job
        remove_job
        get_done_jobs_length
        get_done_jobs_cost
        get_pay_rate
        get_unfinished_jobs_length
        get_unfinished_jobs_cost
"""



"""Définir une classe système de facturation et l'instancier avec les 5 informations 
suivantes:
    Nissan Altima 2012 Bleu, Freins 800$ 6h non-fait
    Ford Taurus 2000 Vert, BieletteAv-G 200$ 4h fait
    Honda Civic 2020 Noir, Pare-Brise 1200$ 2h non-fait
    Ford Escape 2011 Gris, Démarreur 800$ 5h non-fait
    Toyota Corolla 2002 Bleu, Installation de pneus 80$ 1h fait
"""
"""
Laboratoire 5:
Vous devez implémenter un système de facturation pour un garage automobile. Le système 
de facturation doit avoir la liste des véhicules et les réparations à faire.

classe car
    attributs
        maker
        model
        year
        color
    méthodes
        get_maker
        get_model
        get_year
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

def auto_repair_shop():

    def execution():
        Car.instantiate_from_car_db()
        Reparation.instantiate_from_rep_db()
        shop_db = create_dict(Car.car_list, Reparation.rep_list)
        menu(shop_db)                

    class Car:
        car_list = []

        def __init__(self, maker, model, year, color):
            self.maker = maker
            self.model = model
            self.year = year
            self.color = color
            Car.car_list.append(str(self))      

        def get_maker(self):
            return f"{self.maker}"

        def get_model(self):
            return f"{self.model}"

        def get_year(self):
            return f"{self.year}"

        def get_color(self):
            return f"{self.color}"

        @classmethod
        def instantiate_from_car_db(cls):
            with open("car_db.txt", "r", encoding="utf8") as f:
                lines = f.readlines()
            for line in lines:
                data = line.replace("\n", "").split()
                Car(data[0], data[1], data[2], data[3])           

        def __str__(self):
            return f"{self.maker} {self.model} {self.year} {self.color}"

    class Reparation:
        rep_list = []

        def __init__(self, job_name, job_cost, job_length, job_state): 
            self.job_name = job_name
            self.job_cost = job_cost
            self.job_length = job_length
            self.job_state = job_state
            job_data = []
            job_data.append(self.get_job_name())
            job_data.append(self.get_job_cost())
            job_data.append(self.get_job_length())
            job_data.append(self.get_job_state())
            Reparation.rep_list.append(job_data)

        def get_job_name(self):
            return f"{self.job_name}"

        def get_job_cost(self):
            return f"{self.job_cost}"

        def get_job_length(self):
            return f"{self.job_length}"

        def get_job_state(self):
            return f"{self.job_state}"

        @classmethod
        def instantiate_from_rep_db(cls):
            with open("rep_db.txt", "r", encoding="utf8") as f:
                lines = f.readlines()
            for line in lines:
                data = line.replace("\n", "").split()
                Reparation(data[0], data[1], data[2], data[3])   

        def __str__(self):
            return f"{self.job_name} {self.job_cost} {self.job_length} "\
                   f"{self.job_state}"

    class Facturation:
        
        def __init__(self, shop_db, avg_payrate):
            self.shop_db = shop_db

    def create_dict(car_list, rep_list):
        job_db = {}
        for i in range(0,4):
            job_db[car_list[i]] = rep_list[i]
        return job_db

    def menu(shop_db):
        exit = False
        while exit:
            user_sel = -1
            while not 0 <= user_sel <= 7:
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
                Facturation(shop_db, user_sel)
        

    execution()


auto_repair_shop()





       
        


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
#Laboratoire 5:
#Vous devez implémenter un système de facturation pour un garage automobile. Le système de facturation doit avoir la liste des véhicules et les 
#réparations à faire.

#Étape 1:
#Créer le constructeur de la classe automobile. Votre automobile doit avoir les informations suivantes: Modèle, marque, année et couleur.

#Étape 2 :
#Définir une méthode permettant de retourner sous forme de string toutes les informations par rapport à l'automobile.

#Étape 3:
#Créer le constructeur de la classe réparations. Votre objet réparation contenir l'information par rapport au nom de la réparation, à son coût, 
#au nombre d'heures de travail et si le travail a été fait ou non-fait.

#Étape 4:
#Définir une méthode permettant de retourner sous forme de string toutes les informations par rapport à la réparation.

#Étape 5:
#Définir une classe système de facturation et l'instancier avec les 5 informations suivantes:
#Nissan Altima 2012 Bleu, Freins 800$ 6h non-fait
#Ford Taurus 2000 Vert, BieletteAv-G 200$ 4h fait
#Honda Civic 2020 Noir, Pare-Brise 1200$ 2h non-fait
#Ford Escape 2011 Gris, Démarreur 800$ 5h non-fait
#Toyota Corolla 2002 Bleu, Installation de pneus 80$ 1h fait

#Étape 6:
#Définir des méthodes permettant, d'ajouter des réparations, d'enlever des réparations, d'avoir le nombre total d'heures de réparations faites, 
#le revenu total des réparations faites, le revenu horaire moyen, le nombre d'heures total de réparations non faites, et le revenu total manqué 
#des réparations non faites.

#Étape 7:
#Définir un menu permettant à un utilisateur de choisir une des options suivantes:
#ajouter ou enlever une réparation(en incluant les véhicules associés)
#voir la liste de réparations(en incluant les véhicules associés)
#revenue horaire moyen
#voir le nombre total d'heures de réparations faites
#voir le revenu total de réparation faites
#voir le nombre d'heures total de réparations non-faites
#voir le revenu total manqué des réparations non-faites.


class Car:

    def __init__(self, maker:str, model:str, year:int, color:str):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
 
    def __str__(self):
        return f"{self.maker} {self.model} {self.year} {self.color}"
           
class Repair:

    job_data = []

    def __init__(self, job_name:str, job_cost:int, job_length:int, job_state:str): 
        self.job_name = job_name
        self.job_cost = job_cost
        self.job_length = job_length
        self.job_state = job_state
        #Ajout d'une liste contenant les attributs de l'object Repair, à chaque instanciation, dans la variable de classe job_data
        Repair.job_data.append([job_name,job_cost,job_length,job_state])

    def __str__(self):
        return f"{self.job_name} {self.job_cost}$ {self.job_length}h {self.job_state}"

class Billing:
        
    def __init__(self, cars:list, jobs:list):
        self.cars = cars
        self.jobs = jobs

    #Méthode ajoutant un nouvel objet Car et Repair dans leur liste respective (self.cars et self.jobs)
    def add_job(self):
        self.display()
        print()
        car_maker= input("Entrez le constructeur du véhicule: ")
        car_model = input("Entrez le modèle: ")
        car_year = int(input("Entrez l'année: "))
        car_color = input("Entrez la couleur: ")
        job_name = input("Entrez le nom de la réparation: ")
        job_cost = int(input("Entrez le coût: ").replace("$",""))
        job_length = int(input("Entrez la durée en heure: ").replace("h",""))
        job_state = input("Entrez l'état actuel (fait, non-fait): ")
        self.cars.append(Car(car_maker, car_model, car_year, car_color))
        self.jobs.append(Repair(job_name, job_cost, job_length, job_state))

    #Méthode enlevant un objet Car et Repair dans leur liste respective
    def remove_job(self):
        self.display()
        index = int(input("Entrez l'index: "))
        self.cars.pop(index-1)
        self.jobs.pop(index-1)
        Repair.job_data.pop(index-1)

    #Méthode affichant le revenu horaire moyen des réparations faites dans le système Billing 
    def show_hourly_income(self):
        print()
        income = 0
        hours = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "fait":
                income += Repair.job_data[i][1]
                hours += Repair.job_data[i][2]
        hourly_income = income / hours
        print(f"{hourly_income:.2f}$")

    #Méthode affichant le nombre d'heures total des réparations faites dans le système Billing
    def show_done_job_hours(self):
        print()
        hours = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "fait":
                hours += Repair.job_data[i][2]
        print(f"{hours}h")

    #Méthode affichant le revenu total des réparations faites dans le système Billing
    def show_total_income(self):
        print()
        income = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "fait":
                income += Repair.job_data[i][1]
        print(f"{income}$")

    #Méthode affichant le nombre d'heures total des réparations non-faites dans le système Billing
    def show_pending_job_hours(self):
        print()
        hours = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "non-fait":
                hours += Repair.job_data[i][2]
        print(f"{hours}h")

    #Méthode affichant le revenu total jusqu'ici manqué des réparations non-faites dans le système Billing 
    def show_missed_total_income(self):
        print()
        income = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "non-fait":
                income += Repair.job_data[i][1]
        print(f"{income}$")        

    #Méthode affichant une liste indexée (via la création d'un objet zip) contenant chaque réparation avec son véhicule associé
    def display(self):
        print()
        i = 1
        for car, job in zip(self.cars, self.jobs):
            print(f"{i}. {car}: {job}")
            i += 1   

    #Méthode présentant un menu à l'employé pour obtenir l'accès aux méthodes du système Billing 
    def menu(self):
        exit = False
        while not exit:
            user_sel = 0
            while not 1 <= user_sel <= 8:
                print()
                print("Menu des options: ")
                print("1. Ajouter/Enlever une Réparation")
                print("2. Voir Liste des Réparations")
                print("3. Voir Revenu Horaire Moyen")
                print("4. Voir Total des Heures de Réparations Faites")
                print("5. Voir Revenu Total des Réparations Faites")
                print("6. Voir Total des Heures de Réparations Non-Faites")
                print("7. Voir Revenu Total Manqué des Réparations Non-Faites.")
                print("8. Terminer")
                user_sel = int(input("Choix: "))
            if user_sel == 1:
                op_sel = 0
                while not 1 <= op_sel <= 2:
                    print()
                    print("1. Ajouter une réparation à un véhicule")
                    print("2. Enlever une réparation à un véhicule")
                    op_sel = int(input("Choix: "))
                if op_sel == 1:
                    self.add_job()
                else: 
                    self.remove_job()
            elif user_sel == 2:
                self.display()
            elif user_sel == 3:
                self.show_hourly_income()
            elif user_sel == 4:
                self.show_done_job_hours()
            elif user_sel == 5:
                self.show_total_income()
            elif user_sel == 6:
                self.show_pending_job_hours()
            elif user_sel == 7:
                self.show_missed_total_income()
            else:
                exit = True

#Fonction contrôllant le flux du programme via l'instanciation des objets et l'appel éventuel de la méthode menu du système Billing
def execution():
    cars = []
    cars.append(Car("Ford","Escape",2011,"Gris"))
    cars.append(Car("Ford","Taurus",2000,"Vert"))
    cars.append(Car("Honda","Civic",2020,"Noir"))
    cars.append(Car("Nissan","Altima",2012,"Bleu"))
    cars.append(Car("Toyota","Corolla",2002,"Bleu"))

    jobs = []
    jobs.append(Repair("Freins",800,6,"non-fait"))
    jobs.append(Repair("BieletteAv-G",200,4,"fait"))
    jobs.append(Repair("Pare-Brise",1200,2,"non-fait"))
    jobs.append(Repair("Démarreur",800,5,"non-fait"))
    jobs.append(Repair("Pneus",80,1,"fait"))

    bills = Billing(cars, jobs)
    bills.menu()      
    print("\nBonne journée!")


#Appel à la fonction execution pour démarrer le programme
execution()

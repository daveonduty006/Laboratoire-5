class Car:

    def __init__(self, maker:str, model:str, year:int, color:str):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
 
    def __str__(self):
        return f"{self.maker} {self.model} {self.year} {self.color}"
           
class Repair:

    def __init__(self, job_name:str, job_cost:float, job_length:float, job_state:str): 
        self.job_name = job_name
        self.job_cost = job_cost
        self.job_length = job_length
        self.job_state = job_state

    def __str__(self):
        return f"{self.job_name} {self.job_cost}$ {self.job_length}h {self.job_state}"

class Billing:
        
    def __init__(self, cars:list, jobs:list):
        self.cars = cars
        self.jobs = jobs

    def add_job(self):
        self.display()
        print()
        car_maker= input("Entrez le constructeur du véhicule: ")
        car_model = input("Entrez le modèle: ")
        car_year = int(input("Entrez l'année: "))
        car_color = input("Entrez la couleur: ")
        job_name = input("Entrez le nom de la réparation: ")
        job_cost = float(input("Entrez le coût: ").replace("$",""))
        job_length = float(input("Entrez la durée en heure: ").replace("h","").replace("heure", ""))
        job_state = input("Entrez l'état actuel (fait, non-fait): ")
        cars.append(Car(car_maker, car_model, car_year, car_color))
        jobs.append(Repair(job_name, job_cost, job_length, job_state))

    def remove_job(self):
        self.display()
        index = int(input("Entrez l'index: "))
        self.cars.pop(index-1)
        self.jobs.pop(index-1)

    def done_job_hours(self):
        print()
        data = []
        for job in self.jobs:
            data.append(job)
        print(data)

    def display(self):
        print()
        i = 1
        for car, job in zip(self.cars, self.jobs):
            print(f"{i}. {car}: {job}")
            i += 1           

    def menu(self):
        exit = False
        while not exit:
            user_sel = 0
            while not 1 <= user_sel <= 7:
                print()
                print("Menu des options: ")
                print("1. Ajouter/Enlever une Réparation")
                print("2. Voir Liste des Réparations")
                print("3. Voir Total des Heures de Réparations Faites")
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
                if op_sel == 1:
                    self.add_job()
                else: 
                    self.remove_job()
            elif user_sel == 2:
                self.display()
            elif user_sel == 3:
                self.done_job_hours()

            
                


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
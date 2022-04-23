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
        Repair.job_data.append([job_name,job_cost,job_length,job_state])

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
        job_cost = int(input("Entrez le coût: ").replace("$",""))
        job_length = int(input("Entrez la durée en heure: ").replace("h",""))
        job_state = input("Entrez l'état actuel (fait, non-fait): ")
        self.cars.append(Car(car_maker, car_model, car_year, car_color))
        self.jobs.append(Repair(job_name, job_cost, job_length, job_state))

    def remove_job(self):
        self.display()
        index = int(input("Entrez l'index: "))
        self.cars.pop(index-1)
        self.jobs.pop(index-1)
        Repair.job_data.pop(index-1)

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

    def show_done_job_hours(self):
        print()
        hours = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "fait":
                hours += Repair.job_data[i][2]
        print(f"{hours}h")

    def show_total_income(self):
        print()
        income = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "fait":
                income += Repair.job_data[i][1]
        print(f"{income}$")

    def show_pending_job_hours(self):
        print()
        hours = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "non-fait":
                hours += Repair.job_data[i][2]
        print(f"{hours}h")

    def show_missed_total_income(self):
        print()
        income = 0
        for i in range(len(Repair.job_data)):
            if Repair.job_data[i][3] == "non-fait":
                income += Repair.job_data[i][1]
        print(f"{income}$")        

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


execution()

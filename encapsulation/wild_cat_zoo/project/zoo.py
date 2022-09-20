class Zoo:
    def __init__(self, name, budget: int, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return 'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return 'Not enough space for animal'
        self.__budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        def calculate_salary():
            total = 0
            for current_worker in self.workers:
                total += current_worker.salary
            return total

        total_salaries = calculate_salary()
        if total_salaries > self.__budget:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= total_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        def calculate_needed_money_for_all_animals():
            total = 0
            for current_animal in self.animals:
                total += current_animal.money_for_care
            return total

        needed_money = calculate_needed_money_for_all_animals()
        if needed_money > self.__budget:
            return f'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= needed_money
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def __return_status(self, object, ll: list):
        def current_objects_types(current_object):
            type = [i for i in ll if i.__class__.__name__ == current_object]
            return type

        def object_string(current_object):
            list_of_current_objects = current_objects_types(current_object)
            string = f'----- {len(list_of_current_objects)} {current_object}s:\n'
            for current in list_of_current_objects:
                string += current.__repr__() + '\n'
            return string

        return object_string(object)

    def animals_status(self):
        output = ''
        for current_animal in ['Lion', 'Tiger', 'Cheetah']:
            output += self.__return_status(current_animal, self.animals)
        return output.strip()

    def workers_status(self):
        output = ''
        for current_worker in ['Keeper', 'Caretaker', 'Vet']:
            output += self.__return_status(current_worker, self.workers)
        return output.strip()

    # def animals_status(self):
    #     def animal_type(animal):
    #         type = [i for i in self.animals if i.__class__.__name__ == animal]
    #         return type
    #
    #     def this_animal_string(animal):
    #         list_of_this_animal = animal_type(animal)
    #         string = f'----- {len(list_of_this_animal)} {animal}s:\n'
    #         for current in list_of_this_animal:
    #             string += current.__repr__() + '\n'
    #         return string
    #
    #     output = f'You have {len(self.animals)} animals\n'
    #     possible_animals = ['Lion', 'Tiger', 'Cheetah']
    #     for current_animal in possible_animals:
    #         output += this_animal_string(current_animal)
    #     return output.strip()
    #
    # def workers_status(self):
    #     def worker_type(worker):
    #         type = [i for i in self.workers if i.__class__.__name__ == worker]
    #         return type
    #
    #     def this_worker_string(worker):
    #         list_of_this_workers = worker_type(worker)
    #         string = f'----- {len(list_of_this_workers)} {worker}s:\n'
    #         for current in list_of_this_workers:
    #             string += current.__repr__() + '\n'
    #         return string
    #
    #     output = f'You have {len(self.workers)} workers\n'
    #     possible_workers = ['Keeper', 'Caretaker', 'Vet']
    #     for current_worker in possible_workers:
    #         output += this_worker_string(current_worker)
    #     return output.strip()

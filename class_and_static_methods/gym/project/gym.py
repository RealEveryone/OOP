from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):

        def find_object(ll, object_id):
            for current_object in ll:
                if current_object.id == object_id:
                    return current_object

        subscription = find_object(self.subscriptions, subscription_id)
        customer = find_object(self.customers, subscription.customer_id)
        trainer = find_object(self.trainers, subscription.trainer_id)
        exercise = find_object(self.plans, subscription.exercise_id)
        equipment = find_object(self.equipment, exercise.equipment_id)

        return repr(subscription) + '\n' + repr(customer) + '\n' \
               + repr(trainer) + '\n' + repr(equipment) + '\n' + repr(exercise)

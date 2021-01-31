import requests


class Employee:
    """A sample Employee class"""

    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.first_name}{self.last_name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

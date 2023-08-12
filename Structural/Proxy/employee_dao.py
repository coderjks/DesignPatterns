from abc import abstractmethod


class EmployeeDao:

    @abstractmethod
    def get(self, client, employee_id):
        pass

    @abstractmethod
    def create(self, client, employee):
        pass

    @abstractmethod
    def update(self, client, employee_id):
        pass

    @abstractmethod
    def delete(self, client, employee_id):
        pass

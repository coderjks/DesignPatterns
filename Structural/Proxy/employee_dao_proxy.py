from employee_dao import EmployeeDao
from employee_dao_impl import EmployeeDaoImpl


class EmployeeDaoProxy(EmployeeDao):

    def __init__(self):
        self.employee_impl = EmployeeDaoImpl()

    def create(self, client, employee):
        if client == 'ADMIN':
            self.employee_impl.create(client, employee)
        else:
            raise Exception('Access Denied')

    def update(self, client, employee_id):
        if client == 'ADMIN':
            self.employee_impl.update(client, employee_id)
        else:
            raise Exception('Access Denied')

    def delete(self, client, employee_id):
        if client == 'ADMIN':
            self.employee_impl.delete(client, employee_id)
        else:
            raise Exception('Access Denied')

    def get(self, client, employee_id):
        if client == 'USER' or client == 'ADMIN':
            return self.employee_impl.get(client, employee_id)
        else:
            raise Exception('Access Denied')

from employee_dao import EmployeeDao
from employee import Employee


class EmployeeDaoImpl(EmployeeDao):

    def get(self, client, employee_id):
        print('Fetching record for employee_id: {0}'.format(employee_id))
        return Employee()

    def create(self, client, employee):
        print('Creating new employee')

    def update(self, client, employee_id):
        print('Updating employee having id : {0}'.format(employee_id))

    def delete(self, client, employee_id):
        print('Deleting employee having id : {0}'.format(employee_id))

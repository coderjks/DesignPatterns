from employee_dao_proxy import EmployeeDaoProxy
from employee import Employee

if __name__ == "__main__":
    try:
        employee = Employee()
        employee_proxy = EmployeeDaoProxy()
        employee_proxy.create('ADMIN', employee)
        employee_proxy.delete('ADMIN', 1)
        employee_proxy.get('USER', 3)
        employee_proxy.update('ADMIN', 3)
        employee_proxy.update('USER', 3)
    except Exception as e:
        print(e)

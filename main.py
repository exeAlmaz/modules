from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

date_start = datetime.now()



if __name__ == '__main__':
    calculate_salary('this salary')
    get_employees('this employ')
    print(date_start)

date_count = datetime.now() - date_start
print(f'Время на обработку {date_count}')
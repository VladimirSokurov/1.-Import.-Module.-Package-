from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from docx import newdocument
if __name__ == '__main__':
    calculate_salary()
    get_employees()
    now = datetime.now()
    print(now.date())


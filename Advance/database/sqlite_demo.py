import sqlite3
from employee import Employee

# This will create the database once and use that evey time when you run a program
# It will throw error if you try to craete a table which is alreday craeted in previous run.
conn = sqlite3.connect('employee.db')
#conn = sqlite3.connect(':memory:') It will create new database evry time when we run this program , Hence it will not throw table already exsit.
c = conn.cursor()

#c.execute("""CREATE TABLE employee(
#           first text,
#          last text,
#           pay integer
#          )""")


def insert_emp(emp):
    with conn: #Behaviou like context manager so no need to commit our changes to database. It will take commit to database.
        c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
    with conn:
        c.execute("SELECT * FROM employee where last=:last", {'last':lastname})
        return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay =:pay
                      WHERE first =:first AND last =:last""",
                      {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employee WHERE first=:first AND last=:last",
            {'first':emp.first, 'last':emp.last})





emp_1 = Employee('John', 'Doe', 9000)
emp_2 = Employee('David', 'Sun', 9008)


# #c.execute("INSERT INTO employee VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# #conn.commit()


# #c.execute("INSERT INTO employee  VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# #conn.commit()
# #c.execute("INSERT INTO employee VALUES ('Jayashankara', 'D M', 5000)")
# #c.execute("SELECT * FROM employee WHERE last='Doe'")
# c.execute("SELECT * FROM employee WHERE last=?", ('Doe',))
# c.execute("SELECT * FROM  employee WHERE last=:last", {'last':'Doe'})


# print(c.fetchone())
# print(c.fetchall())

# conn.commit()

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')

print(emps)

update_pay(emp_1, 100000000)
emps = get_emps_by_name('Doe')

remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()

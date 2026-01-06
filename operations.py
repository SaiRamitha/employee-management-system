from database import connect_db

def add_employee(emp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        (emp.emp_id, emp.name, emp.role, emp.salary)
    )
    conn.commit()
    conn.close()

def view_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_employee(emp_id, salary):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET salary=? WHERE emp_id=?",
        (salary, emp_id)
    )
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )
    conn.commit()
    conn.close()

def search_employee(emp_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
    employee = cursor.fetchone()
    conn.close()
    return employee

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Task, Category

engine = create_engine("sqlite:///Task.db")
mysession = sessionmaker(bind=engine)
session = mysession()

def list_users():
    print ("Listing all users:")
    users = session.query(User).all()
    for user in users:
        print(user)

def get_user_by_id():
    id_num = input("Enter your User's ID number: ")
    user = session.query(User).filter_by(id=id_num).first()
    print(
        "ID: ", user.id,
        "NAME: ", user.name
    )

def get_user_by_name():
    name = input("Enter your User's name:")
    user = session.query(User).filter_by(name=name).first()
    print(
        "NAME: ", user.name
    )  

def create_new_user():
    user_name = input("Enter new user name: ")
    new_user = User(name=user_name)
    session.add(new_user)
    session.commit()

def delete_user_command(user_id):
    input("Enter user ID: ")
    user = session.query(User).filter_by(id=user_id).first()
    session.delete(user)
    session.commit()

def list_tasks():
    print("Listing all tasks:")
    tasks = session.query(Task).all()
    for task in tasks:
        print(task)

def get_task_command(task_id):
    input("Enter task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    print(task)

def update_task_command(task_id, new_title, new_description, new_due_date, new_status, new_user_id, new_category_ids):
    input("Enter task ID: "),
    input("Enter new title: "),
    input("Enter new description: "),
    input("Enter new due date: "),
    input("Enter new status: "),
    input("Enter new user ID: "),
    input("Enter new category IDs (comma-separated): ")
    task = session.query(Task).filter_by(id=task_id).first()
    task.title = new_title
    task.description = new_description
    task.due_date = new_due_date
    task.status = new_status
    task.user_id = new_user_id
    task.category_ids = [int(cat_id) for cat_id in new_category_ids.split(',')]
    session.commit()

def create_task_command(title, description, due_date, status, user_id, category_ids):
    input("Enter task title: "),
    input("Enter task description: "),
    input("Enter due date: "),
    input("Enter task status: "),
    input("Enter user ID: "),
    input("Enter category IDs (comma-separated): ")
    new_task = Task(title=title, description=description, due_date=due_date, status=status, user_id=user_id)
    new_task.category_ids = [int(cat_id) for cat_id in category_ids.split(',')]
    session.add(new_task)
    session.commit()

def delete_task_command(task_id):
    input("Enter task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    session.delete(task)
    session.commit()

def list_categories():
    print("Listing all categories:")
    categories = session.query(Category).all()
    for category in categories:
        print(category)

def get_category_command(category_id):
    input("Enter category ID: ")
    category = session.query(Category).filter_by(id=category_id).first()
    print(category)

def update_category_command(category_id, new_name):
    input("Enter category ID: "), input("Enter new name: ")
    category = session.query(Category).filter_by(id=category_id).first()
    category.name = new_name
    session.commit()

def create_category_command(category_name):
    input("Enter category name: ")
    new_category = Category(name=category_name)
    session.add(new_category)
    session.commit()

def delete_category_command(category_id):
    input("Enter category ID: ")
    category = session.query(Category).filter_by(id=category_id).first()
    session.delete(category)
    session.commit()

def exit_program():
    print("Exiting program. Goodbye!")

if __name__ == "__main__":
    exit_program()

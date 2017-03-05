from todo_model import Task
from database.maria_db import MariaDBData
from todo_repository import TodoRepository
import json


task = Task("programar 222",  "Fazer Programas em Python 2222")
#print (task.description)


#mariaDB = MariaDBData()

#mariaDB.connect_to_db('localhost', 'root', 'root', 'TODO')

#query = """    
#         INSERT INTO task ( title ,description) VALUES ( %s , %s )
#        """
#values = (task.title, task.description)

#mariaDB.new_data(query, values)
#resultTask = mariaDB.get_data('select * from task')



todo_repository = TodoRepository()

#res = todo_repository.new_task(task)

#print(type(res))
#print(res.obj_to_json())

#result_task = todo_repository.list_task()

#todo_repository.delete_task(20)

#task_update = Task("Alterada 10", "Fwz o update?")
#task_update.id = 10

#todo_repository.update_task(task_update)

#print(json.dumps(result_task, ensure_ascii=False) )

task = todo_repository.get_task(25)

print(type(task))
print(task.obj_to_json())


tasks = todo_repository.list_task()
print(tasks)
print(type(tasks[0]))

"""
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('_'): v for k, v in vars(o).items()}

#print( json.dumps(task, cls=MyEncoder)) 



object_dict = lambda o: {key.lstrip('_'): value for key, value in o.__dict__.items()}
print( json.dumps(task, default=object_dict, allow_nan=False, sort_keys=False, indent=4))
"""






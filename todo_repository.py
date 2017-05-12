
from database.maria_db import MariaDBData
from todo_model import Task


class TodoRepository(object):

    mariaDB = MariaDBData()

    def __init__(self):
        self.mariaDB.connect_to_db('localhost', 'root', 'root', 'TODO')

    def __del__(self):
        self.mariaDB.disconnect_from_db()

    def list_task(self):
        list_task = []
        result_task = self.mariaDB.get_data('select * from task')

        for row_task in result_task:
            list_task.append(self.to_task(row_task))

        return list_task

    def list_task_raw(self):
        list_task = []
        sql = """
        SELECT id , title , description , 
        done as Control_done , 
        date_start as Control_date_start , 
        date_stop as  Control_date_stop 
        FROM TODO.task
        """
        result_task = self.mariaDB.get_data(sql)
        return result_task

    def get_task(self, id):
        result_task = self.mariaDB.get_data(
            "select * from task where id={0}".format(id))
        task_get = None
        print(type(result_task))
        if not result_task:
            task_get = None
        else:
            task_get = self.to_task(result_task[0])
        return task_get

    def new_task(self, task):
        query = """ INSERT INTO task ( title ,description) VALUES ( %s , %s ) """
        values = (task.title, task.description)
        id_task = self.mariaDB.execute_query(query, values)
        result = self.get_task(id_task)
        task_new = result
        return task_new

    def update_task(self, task):
        query_update = """
         UPDATE task
         SET 
         title  = %s ,
         description = %s 
           WHERE id = %s
         """
        print (type(task))
        print(task.id)
        print(task.description)
        values = (str(task.title), str(task.description), str(task.id))
        self.mariaDB.execute_query(query_update, values)
        return self.get_task(task.id)

    def delete_task(self, task_id):
        query_delete = "DELETE FROM task WHERE id = {0} ".format(task_id)
        self.mariaDB.execute_query(query_delete, None)
        return task_id

    def to_task(self, result_task):
        my_task = Task(result_task['title'],
                       result_task['description'])
        my_task.id = int(result_task['id'])
        my_task.done = result_task['done']
        return my_task

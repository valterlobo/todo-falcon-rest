

import json


class Task(object):

     # Iniciar a task
    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def json_to_obj(cls, j):
        dic = json.loads(j)
        print(dic)
        task = Task("", "")
        if 'id' in dic:
            task.id = int(dic['id'])
        task.title = dic['title']
        task.description = dic['description']
        return task

    @classmethod
    def list_obj_to_json(cls, list):
        str_list_json = json.dumps(
            ([obj.obj_to_json() for obj in list]), ensure_ascii=False).replace('\\', '')
        return str_list_json

    def obj_to_json(self):
        return json.dumps(self, cls=MyEncoder).replace("Task__", '')

   # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    # description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

   # done
    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, done):
        self.__done = done

   # date_start
    @property
    def date_start(self):
        return self.__date_start

    @date_start.setter
    def date_start(self, date_start):
        self.__date_start = date_start

   # date_start
    @property
    def date_stop(self):
        return self.__date_stop

    @date_stop.setter
    def date_stop(self, date_stop):
        self.__date_stop = date_stop


class MyEncoder(json.JSONEncoder):

    def default(self, o):
        return {k.lstrip('_'): v for k, v in vars(o).items()}

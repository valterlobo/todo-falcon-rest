import json
from copy import deepcopy
from copy import copy

import falcon

from todo_model import Task
from todo_repository import TodoRepository


class TodoListResource(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        todo_repository = TodoRepository()
        result_task = todo_repository.list_task_raw()
        print(type(result_task))
        print(result_task)
        self.sub_obj_dic(result_task)
        resp.body = json.dumps(result_task)
        del todo_repository

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        str_json = body.decode('utf-8')
        # print (str_json)
        # print (type(str_json))
        task = Task.json_to_obj(str_json)
        todo_repository = TodoRepository()
        # print (type(task))
        todo_repository.new_task(task)
        del todo_repository

    def sub_obj_dic(self, obj_dic):

        for item in obj_dic:
            print ("----------------------------")
            print (type(item))
            item_clone = copy(item)
            for key, value in item_clone.items():
                print (key.split('_', 1))
                obj = key.split('_', 1)
                if (len(obj) > 1):
                    key_obj_sub = obj[0]
                    print(key_obj_sub)
                    if not key_obj_sub in item:
                        item[key_obj_sub] = {}
                    item[key_obj_sub][obj[1]] = value
                    del item[key]


class TodoResource(object):

    def on_get(self, req, resp, id):
        todo_repository = TodoRepository()
        task_get = todo_repository.get_task(id)
        if not task_get:
            raise falcon.HTTPNotFound()

        resp.body = task_get.obj_to_json()
        resp.status = falcon.HTTP_200
        del todo_repository

    def on_put(self, req, resp, id):
        resp.status = falcon.HTTP_200
        body = req.stream.read()
        todo_repository = TodoRepository()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        task = todo_repository.get_task(id)
        if not task:
            raise falcon.HTTPNotFound()

        task_update = Task.json_to_obj(body.decode('utf-8'))
        task_update.id = id
        todo_repository.update_task(task_update)
        del todo_repository

    def on_delete(self, req, resp, id):
        todo_repository = TodoRepository()
        task = todo_repository.get_task(id)
        if not task:
            raise falcon.HTTPNotFound()
        todo_repository.delete_task(id)
        resp.status = falcon.HTTP_200
        del todo_repository

import json
from copy import copy

import falcon

from todo_model import Task
from todo_repository import TodoRepository


class TodoListResource(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        todo_repository = TodoRepository()
        result_list_task = todo_repository.list_task()
        print(type(result_list_task))
        print(result_list_task)
        list = []
        for obj in result_list_task:
            list.append(obj.obj_to_json())
        resp.body = json.dumps(list)
        del todo_repository


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

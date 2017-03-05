import falcon
from  todo_resource import TodoListResource
from  todo_resource import TodoResource



app = falcon.API()

todo_resource_list = TodoListResource()
todo_resource  = TodoResource()

app.add_route('/todo/v1/task', todo_resource_list)

app.add_route('/todo/v1/task/{id}', todo_resource)



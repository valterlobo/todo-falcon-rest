import falcon
from todo_resource import TodoListResource
from todo_resource import TodoResource
from auth_middleware import AuthMiddleware




app = falcon.API(middleware=[
    AuthMiddleware()
])

todo_resource_list = TodoListResource()
todo_resource = TodoResource()

app.add_route('/todo/v1/task', todo_resource_list)

app.add_route('/todo/v1/task/{id}', todo_resource)




Example API  TASK - Falcon / Ptyhon 

https://falconframework.org/

TODO API : 
HTTP Method	URI	Action
GET	http://[hostname]/todo/api/v1.0/tasks	Retrieve list of tasks
GET	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Retrieve a task
POST	http://[hostname]/todo/api/v1.0/tasks	Create a new task
PUT	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Update an existing task
DELETE	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Delete a task

Task fields:
    id: unique identifier for tasks. Numeric type.
    title: short task description. String type.
    description: long task description. Text type.
    done: task completion state. Boolean type.



 Faltando: 
  01 - Colocar em arquivo de configuração dados do Banco de dados 
  02 - Otimizar conexões e revisar o abrir e fechar
  03 - Revisar JSON ( DECODE / ENCONDE)
  04 - Remover PRint do codigo .
  05 - Testes de Performance HTTP (https://gist.github.com/denji/8333630))
  06 - Escolher a porta para inciar / Servidor HTTP



# Configurar o Ambiente de TESTE
pip install virtualenv
virtualenv test
source ./test/bin/activate
pip install falcon
pip install mysqlclient
pip install gunicorn

gunicorn todo_api:app
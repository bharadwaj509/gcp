from flask import Flask, request, Response, g
from flask_restful import abort, Api, Resource
from webargs import fields
from webargs.flaskparser import use_args
from google.cloud import bigquery

app = Flask(__name__)
api = Api(app)

messages = []
message = {'name':'','state':'','age':'','id':'','gender':''}


@app.after_request
def app_after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Cookie,Auth-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Content-Type', 'application/json')
    return response


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class Message(Resource):
    def get(self):
        client = bigquery.Client()
        QUERY = ('SELECT name, state, number, year, gender  FROM [bigquery-public-data:usa_names.usa_1910_2013]')
        query = client.run_sync_query('%s LIMIT 100' % QUERY)
        query.timeout_ms = 10000
        query.run()

        for row in query.rows:
            print(row)
            message['name'] = row[0]
            message['state'] = row[1]
            message['age'] = row[2]
            message['id'] = row[3]
            message['gender'] = row[4]
            messages.append(message)

        print len(messages)
        return messages


    @use_args(messages)
    def post(self, args):
        messages["message"] = args['message']
        return messages["message"], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(Message, '/messages')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

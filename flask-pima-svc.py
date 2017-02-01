# nobel_viz.py
from flask import Flask, request,  jsonify,  json
from pymongo import MongoClient
import pickle
import numpy as np 

url = 'mongodb://test1:test1@ds119578.mlab.com:19578/python_ml_models1'
client = MongoClient(url)
loaded_model = {}
db = client.python_ml_models1
collection = db.m1
for cursor in collection.find({}):
    #print(cursor)
    data = cursor['bin-data']
    info = pickle.loads(data)
    loaded_model = info


data_1 = [ 6.0,  148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50. ]
data_0 = [ 1.0, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31.0]
data = np.reshape(data_1, (1,-1))

result = loaded_model.predict(data) 

print(result)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def login():
	
	prediction = []

	if request.method == 'POST':
		print(request)
		#print('------- request data')
		#print(request.data)

		json_data = json.loads(request.data)
		
		print('--- json data')
		print(json_data)

		json_data = np.reshape(json_data, (1,-1))

		pred = loaded_model.predict(json_data)  
		print('------ prediction')
		print(pred)

		for i in range(len(pred)):
			print(prediction.append(pred[i]))

		print(prediction)

	else:
		print('not post')


	output = json.dumps(prediction)
	#output = json.dumps([1,2,3])

	return jsonify(info=output)

	#return jsonify(prediction=prediction) 



# data = [
#         {'param': 'foo', 'val': 887199},
#         {'param': 'bar', 'val': 399488}
#     ]


# @app.route('/data', methods=['GET'])
# def get_data():
# 	return jsonify(results=data)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	data = [
#         {'param': 'foo', 'val': 2},
#         {'param': 'bar', 'val': 10}
#     ]
# 	if request.method == 'POST':
# 		print(request)
# 		print('------- request data')
# 		print(request.data)

# 		json_data = json.loads(request.data)
# 		print('--- json data')
# 		print(json_data)
# 	else:
# 		print('not post')

# 	return jsonify(results=data)

if __name__ == '__main__':    
	app.run(port=8000)

# from flask import Flask, current_app, send_from_directory
# app = Flask(__name__)  

# #@app.route("/") 
# #def hello():    
# #	return "Hello - World!"

# # @app.route('/x')
# # def root():
# #     return render_template('index.html')

# # @app.route('/')
# # def hello_world():
# #     return current_app.send_static_file('index.html')

# @app.route('/')
# def root():
#     return send_from_directory('.', 'index.html')

# if __name__ == "__main__":    
# 	app.run(port=8000, debug=True) 
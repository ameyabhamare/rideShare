from flask import Flask
from flask import request
import hashlib
import time
import pandas as pd

app = Flask(__name__)
  
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    df = pd.read_csv('Database.csv')
    
    content = request.get_json()
    name = content['name']
    start = content['start']
    end = content['end']
    price = content['price']
    mode = content['mode']
    time_stamp = time.time()
    
    data = name + start + end + price + mode + str(time_stamp)
    
    unique_id = hashlib.sha256(data.encode())
    unique_id = str(unique_id.hexdigest())
    
    df = df.append({'Unique ID' : unique_id, 'Name' : name, 'Start' : start, 'End' : end, 'Price' : price,'Mode' : mode,'TimeStamp' : time_stamp}, ignore_index = True)
    
    df.to_csv('Database.csv', index = None, header = True) 
    return (unique_id)
    
app.run(host='0.0.0.0', port= 8090)

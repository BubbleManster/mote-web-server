
from flask import Flask, request, render_template
import os 
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('page.html')

@app.route('/methods', methods=['GET', 'POST'])
def methodfn():
    # handling javascript-side responses
    # In other words, check what javascript is sending to this script.
    # POST request
    if request.method == 'POST':
        data=request.get_json()  # parse as JSON
        if data.get("clear")=="true":
            os.system("python ./scripts/all-off.py")
        os.system(f"python ./scripts/rgb.py {data.get('color').replace(',', ' ')}") 
            
        return 'Success', 200

if __name__ == '__main__':
   app.run()

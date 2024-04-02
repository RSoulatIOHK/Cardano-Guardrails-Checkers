
from distutils.log import debug 
from fileinput import filename
from constitution_watcher import checkProposal
from flask import *  
import json
app = Flask(__name__)   
  
@app.route('/')   
def main(): 
    print("Hello")  
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file']
        
        savefile = f'./uploads/{f.filename}'
        f.save(savefile)
        outfile = checkProposal(savefile)
        data = json.load(open(outfile))
        return render_template("results.html", name = f.filename, jsonfile = data)   
  
if __name__ == '__main__':   
    app.run(debug=True)
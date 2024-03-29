
from distutils.log import debug 
from fileinput import filename
from constitution_watcher import param_checkers
from flask import *  
import json
app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file']
        savefile = f'./proto/uploads/{f.filename}'
        f.save(savefile)
        outfile = param_checkers(savefile)
        data = json.load(open(outfile))
        return render_template("Acknowledgement.html", name = f.filename, jsonfile = json.dumps(data))   
  
if __name__ == '__main__':   
    app.run(debug=True)
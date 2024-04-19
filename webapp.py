
from constitution_watcher import checkProposalJSON, checkProposalReturnFile
from flask import *  
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, IntegerField
from paramMap import paramMap
import hashlib
import json
import os.path as os

app = Flask(__name__)   
app.secret_key = "test123"  

bootstrap = Bootstrap5(app)

class ProposalForm(FlaskForm):
    txFeeFixed = IntegerField('txFeeFixed')
    txFeePerByte = IntegerField('txFeePerByte')
    utxoCostPerByte = IntegerField('utxoCostPerByte')
    stakeAddressDeposit = IntegerField('stakeAddressDeposit')
    stakePoolDeposit = IntegerField('stakePoolDeposit')
    minPoolCost = IntegerField('minPoolCost')
    treasuryCut = IntegerField('treasuryCut')
    monetaryExpansion = IntegerField('monetaryExpansion')
    maxBlockBodySize = IntegerField('maxBlockBodySize')
    maxTxSize = IntegerField('maxTxSize')
    maxBlockHeaderSize = IntegerField('maxBlockHeaderSize')
    poolRetireMaxEpoch = IntegerField('poolRetireMaxEpoch')
    stakePoolTargetNum = IntegerField('stakePoolTargetNum')
    poolPledgeInfluence = IntegerField('poolPledgeInfluence')
    costModels = IntegerField('costModels')
    maxValueSize = IntegerField('maxValueSize')
    collateralPercentage = IntegerField('collateralPercentage')
    maxCollateralInputs = IntegerField('maxCollateralInputs')
    maxBlockExecutionUnits = IntegerField('maxBlockExecutionUnits')
    maxTxExecutionUnits = IntegerField('maxTxExecutionUnits')
    executionIUnitPrices = IntegerField('executionIUnitPrices')
    govActionLifetime = IntegerField('govActionLifetime')
    committeeMinSize = IntegerField('committeeMinSize')
    committeeMaxTermLimit = IntegerField('committeeMaxTermLimit')
    govDeposit = IntegerField('govDeposit')
    dRepDeposit = IntegerField('dRepDeposit')
    dRepActivity = IntegerField('dRepActivity')
    minFeeRefScriptCoinsPerByte = IntegerField('minFeeRefScriptCoinsPerByte')
    submit = SubmitField('Submit')


@app.route('/')
def home():
    proposalForm = ProposalForm()
    proposalForm.txFeeFixed.data = 155381
    return render_template("index.html", message=None, form=proposalForm, result = None)

@app.route('/index.html', methods=['GET', 'POST'])   
def index():
    proposalForm = ProposalForm()
    # Parse the message
    result = request.args.get('result')
    if not (result == None) and os.isfile("./data/checks_" + result + ".json"):
        with open("./data/checks_" + result + ".json", 'r') as file:
            result = json.load(file)
    else:
        result = None
    if request.method == 'GET':
        if all (field.data == None for field in proposalForm if (field.name != "submit")) and result == None:
            return render_template("index.html", form=proposalForm, result = None)
        if result == None:
            return render_template("index.html", form=proposalForm, result = None)
        else:
            return render_template("index.html", form=proposalForm, result = result)
    else:          
        proposal = {
            "start_epoch" : 40,
            "parameter_changes": {}
        }
        for field in proposalForm:
            if field.name != "submit" and field.name != "csrf_token":              
                key = [key for key, value in paramMap.items() if value["name"] == field.name][0]
                if field.data != None:
                    proposal["parameter_changes"][key] = field.data
        return render_template("index.html", form=proposalForm, result = checkProposalJSON(proposal))
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':
        proposalForm = ProposalForm()   
        f = request.files['file']
        if f.filename == "":
            return redirect(url_for("index", result = None))
        filename = str(hashlib.md5(f.filename.encode()).hexdigest()) + ".json"
        savefile = f'./uploads/{filename}'
        f.save(savefile)
        savedFile = checkProposalReturnFile(savefile)
        return redirect(url_for("index", result = savedFile))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':   
    app.run(debug=True)
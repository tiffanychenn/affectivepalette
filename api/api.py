from flask import Flask, request
from panas import get_affective_state_from_panas
from sentimentanalysis import clean_text


app = Flask(__name__)

@app.route('/')
def index():
    return "working"

@app.route("/panas", methods=["POST"])
def panas():
    panas_scores = {
            "interested": int(request.form['interested']), 
            "alert": int(request.form['alert']), 
            "attentive": int(request.form['attentive']), 
            "excited": int(request.form['excited']), 
            "enthusiastic": int(request.form['enthusiastic']), 
            "inspired": int(request.form['inspired']), 
            "proud": int(request.form['proud']), 
            "strong": int(request.form['strong']), 
            "determined": int(request.form['determined']), 
            "active": int(request.form['active']), 
            "upset": int(request.form['upset']), 
            "jittery": int(request.form['jittery']), 
            "nervous": int(request.form['nervous']), 
            "distressed": int(request.form['distressed']), 
            "guilty": int(request.form['guilty']), 
            "ashamed": int(request.form['ashamed']), 
            "hostile": int(request.form['hostile']), 
            "irritable": int(request.form['irritable']), 
            "scared": int(request.form['scared']), 
            "afraid": int(request.form['afraid']), 
        }
    return {"result": get_affective_state_from_panas(panas_scores)}

@app.route("/newsarticle", methods=["POST"])
def newsarticle():
    return {"result": clean_text(request.form['text'])}

if __name__ == "__main__":
    app.run(debug=True)
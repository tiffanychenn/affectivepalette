from flask import Flask, request
from panas import get_affective_state_from_panas
from sentimentanalysis import clean_text


app = Flask(__name__)

@app.route('/')
def index():
    return "working"

@app.route("/panas", methods=["POST"])
def panas():
    json = request.get_json()
    panas_scores = {
            "interested": int(json['interested']), 
            "alert": int(json['alert']), 
            "attentive": int(json['attentive']), 
            "excited": int(json['excited']), 
            "enthusiastic": int(json['enthusiastic']), 
            "inspired": int(json['inspired']), 
            "proud": int(json['proud']), 
            "strong": int(json['strong']), 
            "determined": int(json['determined']), 
            "active": int(json['active']), 
            "upset": int(json['upset']), 
            "jittery": int(json['jittery']), 
            "nervous": int(json['nervous']), 
            "distressed": int(json['distressed']), 
            "guilty": int(json['guilty']), 
            "ashamed": int(json['ashamed']), 
            "hostile": int(json['hostile']), 
            "irritable": int(json['irritable']), 
            "scared": int(json['scared']), 
            "afraid": int(json['afraid']), 
        }
    return {"result": get_affective_state_from_panas(panas_scores)}

@app.route("/newsarticle", methods=["POST"])
def newsarticle():
    result = clean_text(request.form['text'])
    return {"result": [result if result > 0 else 0, -result if result < 0 else 0]}

if __name__ == "__main__":
    app.run(debug=True)
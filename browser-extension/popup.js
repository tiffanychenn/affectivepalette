const _submitPanasForm = () => {
  const interested = document.querySelector('input[name="interested"]:checked').value;
  const distressed = document.querySelector('input[name="distressed"]:checked').value;
  const excited = document.querySelector('input[name="excited"]:checked').value;
  const upset = document.querySelector('input[name="upset"]:checked').value;
  const strong = document.querySelector('input[name="strong"]:checked').value;
  const guilty = document.querySelector('input[name="guilty"]:checked').value;
  const scared = document.querySelector('input[name="scared"]:checked').value;
  const hostile = document.querySelector('input[name="hostile"]:checked').value;
  const enthusiastic = document.querySelector('input[name="enthusiastic"]:checked').value;
  const proud = document.querySelector('input[name="proud"]:checked').value;
  const irritable = document.querySelector('input[name="irritable"]:checked').value;
  const alert = document.querySelector('input[name="alert"]:checked').value;
  const ashamed = document.querySelector('input[name="ashamed"]:checked').value;
  const inspired = document.querySelector('input[name="inspired"]:checked').value;
  const nervous = document.querySelector('input[name="nervous"]:checked').value;
  const determined = document.querySelector('input[name="determined"]:checked').value;
  const attentive = document.querySelector('input[name="attentive"]:checked').value;
  const jittery = document.querySelector('input[name="jittery"]:checked').value;
  const active = document.querySelector('input[name="active"]:checked').value;
  const afraid = document.querySelector('input[name="afraid"]:checked').value;

  const panasFormResults = {
    "interested": interested,
    "distressed": distressed,
    "excited": excited,
    "upset": upset,
    "strong": strong,
    "guilty": guilty,
    "scared": scared,
    "hostile": hostile,
    "enthusiastic": enthusiastic,
    "proud": proud,
    "irritable": irritable,
    "alert": alert,
    "ashamed": ashamed,
    "inspired": inspired,
    "nervous": nervous,
    "determined": determined,
    "attentive": attentive,
    "jittery": jittery,
    "active": active,
    "afraid": afraid
  }

  fetch('http://127.0.0.1:5000/panas', {
    method: "POST",
    body: JSON.stringify(panasFormResults),
    headers: {
      'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
      'Access-Control-Allow-Origin':'*',
      'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS',
      'Content-Type': 'application/json; charset=utf-8'
    },
  }).then(response => {
    return response.json();
  }).then(data =>{
      console.log(data["result"]);
  }).catch(error => {
    console.log(error);
  })  
}

const checkEmotionReaderType = () => {
  chrome.storage.local.get(["AffectivePaletteStatus"]).then((result) => {
    const t = result["AffectivePaletteStatus"];
    if (t === "questionnaire") {
      document.getElementById("questionnaire").setAttribute("checked", "true");
      document.getElementById("panas").setAttribute('style', 'visibility: visible');
    }
    else if (t === "article") {
      document.getElementById("article").setAttribute("checked", "true");
      document.getElementById("panas").setAttribute('style', 'visibility: hidden');
    }
    else {
      document.getElementById("off").setAttribute("checked", "true");
      document.getElementById("panas").setAttribute('style', 'visibility: hidden');
    }
  });
}

checkEmotionReaderType();

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("submit").onclick = _submitPanasForm;
});

document.querySelectorAll('input[name="type"]').forEach((el) => 
  el.addEventListener("change", function () {
    const v = document.querySelector('input[name="type"]:checked').value;
    chrome.storage.local.set({"AffectivePaletteStatus": v}).then(() => {
      console.log("set to " + v);
      if (v === "questionnaire") {
        document.getElementById("panas").setAttribute('style', 'visibility: visible');
      }
      else {
        document.getElementById("panas").setAttribute('style', 'visibility: hidden');
      }
    });
  })
);
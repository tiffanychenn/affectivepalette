const ping = () => {
    chrome.storage.local.get(["AffectivePaletteStatus"]).then((result) => {
        const t = result["AffectivePaletteStatus"];
        if (t === "article") {
            chrome.runtime.sendMessage(
                {
                    contentScriptQuery: "postData"
                    , text: document.body.innerText,
                    url: 'http://127.0.0.1:5000/newsarticle'
                }, function (response) {
                    if(chrome.runtime.lastError) {
                        setTimeout(ping, 1000);
                      }
                    else if (response != undefined && response != "") {
                        console.log(response);
                    }
                    else {
                        console.log(null);
                    }
                });
        }
    });
}

ping();
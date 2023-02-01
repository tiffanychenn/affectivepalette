// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {  
  if (request.contentScriptQuery == "postData") {
      fetch(request.url, {
          method: 'POST',
          headers: {
            'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
            // 'Access-Control-Allow-Origin':'*',
            // 'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
          },
          body: "text=" + request.text,
      })
          .then(response => {return response.json()})
          .then(data => {     
                chrome.storage.local.set({"AffectivePaletteEmotionList": data["result"]}).then(() => {
                console.log(data["result"]);
            })
            })
          .catch(error => console.log('Error:', error));
      return true;
  }
});
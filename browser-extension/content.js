function getText(){
    return document.body.innerText
}
function getHTML(){
    return document.body.outerHTML
}

setInterval(() => {
    console.log(getText());             //Gives you all the text on the page
    console.log(getHTML());             //Gives you the whole HTML of the pages
}, 1000);

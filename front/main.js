document.getElementById("filepicker").addEventListener("change", (event) => {

    var jsonfile = require('jsonfile');


    for (const file of event.target.files) {
        let item = document.createElement("li");
        item.textContent = file.webkitRelativePath;
        console.log(item);

    };
    jsonfile.writeFile('loop.json', item);



}, false);
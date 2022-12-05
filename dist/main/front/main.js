const output = document.getElementById('output');
const filepicker = document.getElementById('filepicker');



filepicker.addEventListener('change', (event) => {
    location.reload();
    const files = event.target.files;

    for (const file of files) {
        output.textContent += "C:/" + `${file.webkitRelativePath}\n`;

    }

    var userInput = output.textContent;
    start(userInput);

});

async function start(userInput) {

    output.textContent = ""
    document.getElementById('text_change').innerHTML = 'Работаю';
    await eel.get_txt(userInput)();
    userInput = "";

}
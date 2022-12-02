const output = document.getElementById('output');
const filepicker = document.getElementById('filepicker');



filepicker.addEventListener('change', (event) => {
    const files = event.target.files;

    for (const file of files) {
        output.textContent += "C:/" + `${file.webkitRelativePath}\n`;

    }

    var userInput = output.textContent;
    run_txt(userInput);
});

async function run_txt(userInput) {
    await eel.run_txt(userInput)();
}
console.log("testes");


function changeColor(){

    let colors = [
        "lightpink",
        "lightblue",
        "lightgreen",
        "lightyellow",
        "lavender",
        "mistyrose"
    ];

    let randomColor =
        colors[Math.floor(Math.random() * colors.length)];

    document.body.style.backgroundColor = randomColor;
}

document.addEventListener("DOMContentLoaded", () => {

    console.log("JS Loaded");

    let button = document.getElementById("btn");

    button.addEventListener("click", () => {
        alert("Added to cart");
       
        document.body.style.backgroundColor = "lightpink"
    });

});

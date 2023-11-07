let x = 10; // Declaring a variable using let

function exampleFunction() {
    let y = 20; // Declaring a block-scoped variable using let

    console.log(this); // 'this' has context-specific meaning within a function

    console.log(x); // Accessing the variable 'x' declared with let
    console.log(y); // Accessing the variable 'y' declared with let
}

exampleFunction();

function generateEmptyMatrix(noOfRows, noOfColumns) {
    let matrix = [];
    for (let i = 0; i < noOfRows; i++) {
        let row = [];
        for (let j = 0; j < noOfColumns; j++) {
            row.push("#");
        }
        matrix.push(row);
    }
    return matrix;
}

function senderSide() {
    console.log("\n\nAt the sender side : \nEnter Plain Text (Note : The plain text cannot be more than 16 characters long):");
    let plainText = "meetmeatthepark"; // Replace with suitable input method in your JavaScript environment

    if (plainText.length > 16) {
        console.log("The message is too long !!!");
        return;
    }

    let noOfRows = 4;
    let noOfColumns = 4;
    let counter = 0;
    let matrix = generateEmptyMatrix(noOfRows, noOfColumns);

    for (let i = 0; i < noOfRows; i++) {
        for (let j = 0; j < noOfColumns; j++) {
            if (counter >= plainText.length) {
                break;
            }
            matrix[i][j] = plainText[counter];
            counter++;
        }
    }

    console.log("The matrix formed at the sender side is : ", matrix);

    let cipherText = "";

    for (let i = 0; i < noOfColumns; i++) {
        for (let j = 0; j < noOfRows; j++) {
            cipherText += matrix[j][i];
        }
    }

    console.log("The cipher text enciphered at sender side is : ", cipherText);
    return cipherText;
}

function receiverSide(cipherText) {
    console.log("\n\nAt the receiver side : ");
    console.log("The cipher text obtained is : ", cipherText);

    let noOfRows = 4;
    let noOfColumns = 4;
    let counter = 0;

    let matrix = generateEmptyMatrix(noOfRows, noOfColumns);

    for (let i = 0; i < noOfColumns; i++) {
        for (let j = 0; j < noOfRows; j++) {
            matrix[j][i] = cipherText[counter];
            counter++;
        }
    }

    console.log("The matrix formed at the receiver side : ", matrix);

    let decipheredPlainText = "";

    for (let i = 0; i < noOfRows; i++) {
        for (let j = 0; j < noOfColumns; j++) {
            decipheredPlainText += matrix[i][j];
        }
    }

    console.log("Deciphered Plain Text with bogus characters : ");
    console.log(decipheredPlainText);

    decipheredPlainText = decipheredPlainText.replace(/#/g, "");

    console.log("Deciphered Plain Text : ");
    console.log(decipheredPlainText);
}

function main() {
    let cipherText = senderSide();
    receiverSide(cipherText);
}

main();

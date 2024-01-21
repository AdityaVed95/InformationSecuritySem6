// playfair_cipher.js

const prompt = require('prompt-sync')();

const plain_text = prompt('Enter Plain Text : ');
console.log(`Entered plain text is : ${plain_text}`);

// const plain_text = "meetmeatthepark";

const no_of_columns = 4;

let matrix = Array.from({ length: 4 }, () => new Array(4).fill("_"));

let counter = 0;

for(let i=0;i<4;i++)
{
    for(let j=0;j<4;j++)
    {
        if(plain_text[counter])
        {
            matrix[i][j] = plain_text[counter];
            counter += 1;
        }
        
    }
}

console.log(matrix);

let cipher_text = "";


for(let i = 0;i<4;i++)
{
    for(let j=0; j<4; j++)
    {
        cipher_text = cipher_text + matrix[j][i];
    }
}

console.log("Ciphter Text for your input is : "+cipher_text);
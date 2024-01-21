// let matrix = Array(4).fill().map(() => Array(4).fill('_'));

let matrix = Array(4).fill("_").map(() => Array(4).fill('#'));
console.log(matrix);

let arr1 = [1,2,3,4];

let arr2 = arr1.map( (element) => {
    return element+1
}

)

console.log(arr2);

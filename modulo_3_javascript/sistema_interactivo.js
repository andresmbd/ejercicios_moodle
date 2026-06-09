/* WEEK 1*/
// prompts para el usuario

// const nombre = prompt('Ingrese su nombre');
// const edad = parseInt(prompt('Ingrese la edad'));
// // si la edad es un numero entero y no es un NaN lo deja pasar, si no muestra error
// if(typeof edad === 'number' && !isNaN(edad)){
//     if(edad < 18){
//         console.log(`Hola ${nombre}, eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!`); 
//     }else{
//         console.log(`Hola ${nombre}, eres mayor de edad. ¡Prepárate para grandes oportunidades en el mundo de la programación!`);
//     }
// }else{
//     console.error('Error: Por favor, ingresa una edad válida en números.');
// }


/*WEEK 2*/
const productos = [
    {
        id: 1,
        name: "banana",
        price: 2100
    }
]

let numeros = new Set([1, 2, 2, 3, 3]);

numeros.add(7);
numeros.delete(4);

let myProducts = new Map([
    ["electrodomestico", {
        id: 1,
        nombre: "laptop",
        precio: 1200
    }]
]);

// for(const clave in productos){
//     console.log(clave, productos[clave]);

// }

// for(const numero of numeros){
//     console.log(numero);
// }

// myProducts.forEach((product, category) => {
//     console.log(category, product);

// });

function validateProducts(array, object, map, category) {

    if (typeof object.id === "number" && object.id > 0) {
        const lastElement = array[array.length - 1];
        let newId = null;
        if (!lastElement) {
            newId = 1;
        } else {
            newId = lastElement.id + 1;
        }
        object.id = newId;
    }else{
        console.error('Invalid Product Id');
        return;
    }

    if(typeof object.name === "string" && object.name.length > 0){
        object.name = object.name.trim();

    }else {
        console.error('Invalid Product name');
        return;
    }
    if (typeof object.price !== "number" || object.price <= 0) {
        console.error('Invalid Product Price');
        return;
    }
    return map.set(category, object)
}

console.log(productos);
console.log(numeros);


console.log(validateProducts(productos, productos[0], myProducts, 'fruit'));

/* WEEK 3 */
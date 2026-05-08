// 
const nombre = prompt('Ingrese su nombre');
const edad = parseInt(prompt('Ingrese la edad'));

if(typeof edad === 'number' && !isNaN(edad)){
    if(edad < 18){
        console.log(`Hola ${nombre}, eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!`); 
    }else{
        console.log(`Hola ${nombre}, eres mayor de edad. ¡Prepárate para grandes oportunidades en el mundo de la programación!`);
    }
}else{
    console.error('Error: Por favor, ingresa una edad válida en números.');
}
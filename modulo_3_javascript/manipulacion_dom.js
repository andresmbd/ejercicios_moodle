let inputNotas = document.getElementById('inputNotas');
const botonNotas = document.getElementById('botonNotas');
const listaNotas = document.getElementById('listaNotas');
let notas = [];



botonNotas.addEventListener('click', () => {
    if (inputNotas.value.trim() === "") {
        alert('vacio');
    } else {
        const li = document.createElement('li');
        const deleteButton = document.createElement('button');

        li.textContent = inputNotas.value;
        deleteButton.textContent = "Eliminar";
        listaNotas.appendChild(li);
        listaNotas.appendChild(deleteButton);
        inputNotas.value = "";
        console.log('Lista agregada', li);
        
        notas = [...listaNotas.querySelectorAll('li')];
        const notes = notas.map(li => li.textContent);
        console.log(notes);

        localStorage.setItem('notas', JSON.stringify(notes)) // al agregarse otra se muestran las anteriores notas no eliminadas

        deleteButton.addEventListener('click', () => {
            li.remove();
            deleteButton.remove()
            console.log(notes);
            console.log('removido', li);
            localStorage.removeItem('notas')// Se ve que se elimina todo pero se mantienen las anteriores
        });
    }
});

window.addEventListener('DOMContentLoaded', ()=>{
    listaNotas.innerHTML = localStorage.getItem('notas')
    // Al agregarse con la pag recargada se sobrescribe lo que ya estaba en el localStorage
});
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
        localStorage.setItem('notas', JSON.stringify(notes))
        console.log('Lista agregada', li);

        updateUl();
        deleteButton.addEventListener('click', () => {
            li.remove();
            deleteButton.remove()
            console.log('removido', li);
            localStorage.removeItem('nota')
            updateUl();
        });
    }
});

function updateUl() {
    notas = [...listaNotas.querySelectorAll('li')];
    // console.log(notas);
    const notes = notas.map(li => li.textContent);
    console.log(notes);
}




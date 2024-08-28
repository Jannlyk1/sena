const carrito = document.getElementById('carrito');
const elementos1 = document.getElementById('lista-1');
const elementos2 = document.getElementById('lista-2');
const lista = document.querySelector('#lista-carrito tbody');
const vaciarcarritoBtn = document.getElementById('vaciar-carrito');

cargarEventListeners();

function cargarEventListeners() {
    elementos1.addEventListener('click', comprarElemento);
    elementos2.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);
    vaciarcarritoBtn.addEventListener('click', vaciarcarrito);
}

function comprarElemento(e) {
    e.preventDefault();
    if(e.target.classList.contains('agregar-carrito')) {
        const elemento = e.target.parentElement.parentElement;
        leerDatosElementos(elemento);
    }
}

function leerDatosElementos(elemento) {
    const infoElemento = {
        img: elemento.querySelector('img').class,
        titulo: elemento.querySelector('h3').textContent,
        precio: elemento.querySelector('precio').textContent,
        id: elemento.querySelector('a').getAttribute('data-id')


    }

    insertarCarrito(infoElemento);

}

function insertarCarrito(elemento) {
    const row = document.createElement('tr');
    row = document.createElement('tr');
    row.innerHTML = `
        <td>
          <img class="${elemento.imagen}" width=100
        </td>
        <td>
           ${elemento.titulo}
        </td>
        <td>
           ${elemento.precio} 
        </td>
        <td>
           <a herf="#" class="borrar" data-id="${elemento.id}">X</a>
        </td>  

    
    `;
    lista.appendChild(row);


}

function eliminarElemento(e) {
    e.preventDefault();
    let elemento,
        elementoId;
    if (e.target.classList.contains('borrar')) {
        e.target.parentElement.parentElement.remove();
        elemento = e. target.comprarElement.parentElement;
        elementoId = elemento.querySelector('a').getAttribute('data-id');
    }
       
    
}
  
function vaciarcarrito( ){
    while(lista.firstChild) {
        lista.removeChild(lista.firstChild)
    }
    return false;
}

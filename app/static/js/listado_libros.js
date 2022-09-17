(function () {
    const btnsComprarLibro = document.querySelectorAll('btnComprarLibro');
    let isbnLibroSeleccionado = null;

    btnsComprarLibro.forEach((btn) => {
        btn.addEventListener('click', function () {
            isbnLibroSeleccionado = this.id;
            confirmarComprar();
        })
    })

    const confirmarComprar = async () => {
        await fetch('http://127.0.0.1:5000/comprarlibro', {
            method: 'POST',
            mode: 'same-origin',
            credentials: 'same-origin',
            headers: {
                'content-type': 'application/json',
                'X-CSRF-Token': ''
            },
            body: JSON.stringify({
                'isbn': isbnLibroSeleccionado
            })

        }).then(response => {
            if(!response.ok){
                console.error("Error en la recepción!");
            }
            return response.json();
        }).then(data=>{
            console.log("Libro comprado!")
        }).catch(error=>{
            console.error('Error: ${error}')
        });
    };

})();

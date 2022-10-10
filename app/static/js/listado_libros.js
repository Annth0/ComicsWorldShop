(function () {
    const btnsComprarLibro = document.querySelectorAll('.btnComprarLibro');
    let isbnLibroSeleccionado = null;
    const csrf_token = document.querySelector("[name='csrf_token']").value;

    btnsComprarLibro.forEach((btn) => {
        btn.addEventListener('click', function () {
            isbnLibroSeleccionado = this.id;
            confirmarComprar();
        });
    });

    const confirmarComprar = () => {
        Swal.fire({
            title: '|-  Confirma la compra para tu selección:  -|',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'Comprar Comic',
            showLoaderOnConfirm: true, 
            preConfirm: async () => {
                //console.log(window.origin);
                return await fetch('http://127.0.0.1:5000/comprarLibro', {
                    method: 'POST',
                    mode: 'same-origin',
                    credentials: 'same-origin',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrf_token
                    },
                    body: JSON.stringify({
                        'isbn': isbnLibroSeleccionado
                    })

                }).then(response => {
                    if (!response.ok) {
                        notificacionSwal('Error', response.statusText, 'error', 'Cerrar');
                    }
                    return response.json();
                }).then(data => {
                    notificacionSwal('¡Exito!', 'Libro comprado!', 'success', 'OK');
                }).catch(error => {
                    notificacionSwal('Error', error, 'error', 'Cerrar');
                });
            },
            allowOutsideClick: () => false,
            allowEscapeKey: () => false
        });
    };
})();

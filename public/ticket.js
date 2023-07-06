async function main() {
    const id = new URLSearchParams(location.search).get('id');
    if (!id) {
        return;
    }
    const doc = await db.collection('tickets').doc(id).get();
    document.querySelector('.ticket-id').textContent = doc.id;
    document.querySelector('.ticket-data').textContent = JSON.stringify(
        doc.data(),
        null,
        2
    );
    JsBarcode('#barcode', doc.id, {
        height: 300,
        width: 3,
    });
}

// detect when keyboard keys are pressed
let scanned = '';
document.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        document
            .querySelector('#barcode')
            .insertAdjacentHTML(
                'afterend',
                `<div style="font-size:1rem;">SCANNED: ${scanned}</div>`
            );
        scanned = '';
    } else if (/^[a-zA-Z0-9]$/.test(event.key)) {
        scanned += event.key;
    }
});

main();

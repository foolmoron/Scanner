async function onSubmit(event) {
    event.preventDefault();

    const name = event.target.name.value;
    const doc = await db.collection('tickets').add({
        name,
    });
    location.href = `ticket.html?id=${doc.id}`;
}

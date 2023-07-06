async function onSubmit(event) {
    event.preventDefault();

    const data = Object.fromEntries(new FormData(event.target).entries());
    const doc = await db.collection('tickets').add(data);
    location.href = `ticket.html?id=${doc.id}`;
}

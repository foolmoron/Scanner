async function onSubmit(event) {
    event.preventDefault();

    const data = {
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
        ...Object.fromEntries(new FormData(event.target).entries()),
    };
    const id =
        Date.now().toString().substring(3) + Math.floor(Math.random() * 1000);
    await db.collection('tickets').doc(id).set(data);
    location.href = `ticket.html?id=${id}`;
}

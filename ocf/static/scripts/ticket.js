const statusText = document.getElementById('status-info');


function updateStatus(message, statusName) {
    statusName = statusName || 'light';
    statusText.className = '';
    statusText.classList.add('text-' + statusName);
    statusText.innerHTML = message;
}


document.getElementById('ticket-form').addEventListener('submit', e => {
    e.preventDefault();

    const formData = new FormData(e.target);

    fetch('#', {
        method: 'POST',
        body: formData,
    })
    .then(data => data.json())
    .then(json => {
        if (json.code !== 0) {
            updateStatus(json.message, 'danger');
            return;
        }
        updateStatus('');

        fileName = json.data.name;

        const parentContainer = document.getElementById('body-container');
        const img = document.createElement('img');
        img.setAttribute('src', `/static/tickets/${fileName}`);
        // parentContainer.innerHTML = '';
        parentContainer.appendChild(img);

        document.getElementById('ticket-form').remove();
    });
});

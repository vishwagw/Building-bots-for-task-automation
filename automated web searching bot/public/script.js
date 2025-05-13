document.getElementById('start-record-btn').addEventListener('click', startVoiceRecognition);

function startVoiceRecognition() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('result-text').innerText = `You said: ${transcript}`;
        fetchSearchResults(transcript);
    };

    recognition.onerror = function(event) {
        console.error(event.error);
        document.getElementById('result-text').innerText = 'Error occurred in recognition: ' + event.error;
    };
}

function fetchSearchResults(query) {
    fetch(`/search?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const searchResults = document.getElementById('search-results');
            searchResults.innerHTML = '';
            data.results.forEach(result => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = result.link;
                a.textContent = result.title;
                a.target = '_blank';
                li.appendChild(a);
                searchResults.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching search results:', error);
        });
}
const searchForm = document.getElementById('searchForm');
const searchInput = document.getElementById('searchInput');
const gridContainer = document.getElementById('shows-grid');

searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const query = searchInput.value.trim();
    if (query === '') return;

    const apiUrl = `https://api.jikan.moe/v4/anime?q=${encodeURIComponent(query)}&type=tv`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            displayAnimeResults(data.data);
        })
        .catch(error => {
            console.error('Error fetching anime data:', error);
            animeResults.innerHTML = '<p>Failed to fetch anime data. Please try again later.</p>';
        });
});

function displayAnimeResults(results) {
    gridContainer.innerHTML = '';

    if (results.length === 0) {
        gridContainer.innerHTML = '<p>No anime found.</p>';
        return;
    }

    results.forEach(show => {
        const gridItem = document.createElement('div');
        gridItem.className = 'grid-item';
        gridItem.innerHTML = `
            <img src="${show.images.jpg.image_url}" alt="${show.title_english}">
            <h3>${show.title_english}</h3>
        `;
        gridItem.addEventListener('click', function() {
            addToShowList(show.mal_id);
        });
        gridContainer.appendChild(gridItem);
    });
}

function addToShowList(malId) {
    // Assuming you want to redirect to /add_show with the mal_id as a query parameter
    window.location.href = `/add?mal_id=${malId}`;
}

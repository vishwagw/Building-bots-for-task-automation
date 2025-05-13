const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

// Replace 'YOUR_API_KEY' with your actual API key from a search engine (e.g., Google Custom Search API)
const API_KEY = 'YOUR_API_KEY';
const SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID';

app.use(express.static('public'));

app.get('/search', async (req, res) => {
    const query = req.query.query;
    try {
        const response = await axios.get('https://www.googleapis.com/customsearch/v1', {
            params: {
                key: API_KEY,
                cx: SEARCH_ENGINE_ID,
                q: query,
            }
        });
        const results = response.data.items.map(item => ({
            title: item.title,
            link: item.link
        }));
        res.json({ results });
    } catch (error) {
        console.error('Error fetching search results:', error);
        res.status(500).json({ error: 'Error fetching search results' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
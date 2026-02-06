# Web Scraper Application

A Flask-based web application that extracts HTML and CSS from any given website URL. The application features a modern web interface with login/signup pages and allows users to fetch and download website source code.

## Features

- 🌐 **Web Scraping**: Extract HTML and CSS files from any website
- 🔐 **Authentication Pages**: Login and signup interfaces
- ⚡ **Concurrent Downloads**: Uses ThreadPoolExecutor for fast parallel CSS file downloads
- 🎨 **Modern UI**: Clean and responsive user interface
- 📁 **Organized Output**: Downloads are saved in categorized folders

## Project Structure

```
web_page/
├── app.py                          # Flask application with routes
├── web_scrape.py                   # Web scraping logic
├── static/
│   ├── script.js                   # Frontend JavaScript
│   └── styles.css                  # Application styles
├── templates/
│   ├── index.html                  # Main page
│   ├── login.html                  # Login page
│   └── signup.html                 # Signup page
└── downloaded_{domain}/            # Downloaded website files (auto-created)
```

## Requirements

- Python 3.7+
- Flask
- BeautifulSoup4
- Requests

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd web_page
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask beautifulsoup4 requests
   ```

## Usage

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - The main page allows you to enter a website URL to scrape
   - Login page: `http://localhost:5000/login`
   - Signup page: `http://localhost:5000/signup`

3. **Scrape a website**
   - Enter the target website URL in the input field
   - Click submit to fetch the HTML and CSS files
   - Downloaded files will be saved in a folder named `downloaded_{domain}`

## API Endpoints

### `GET /`
Returns the main index page

### `GET /login`
Returns the login page

### `GET /signup`
Returns the signup page

### `POST /fetch-website-code`
Fetches HTML and CSS from the provided URL

**Request Body:**
```json
{
  "web_url": "https://example.com"
}
```

**Response:**
```json
{
  "recieved": "yes"
}
```

## How It Works

1. **HTML Fetching**: The application sends a GET request to the target URL and retrieves the HTML content
2. **CSS Extraction**: BeautifulSoup parses the HTML to find all linked CSS files
3. **Concurrent Downloads**: Multiple CSS files are downloaded in parallel using ThreadPoolExecutor
4. **File Storage**: All files are saved in a folder named after the domain

## Configuration

- **Debug Mode**: Currently enabled in `app.py`. Disable for production:
  ```python
  app.run(debug=False)
  ```

- **Timeout Settings**: Adjust connection and read timeouts in `web_scrape.py`:
  ```python
  timeout=(connect_timeout, read_timeout)
  ```

- **Max Workers**: Control concurrent downloads by adjusting `max_workers` parameter

## Future Enhancements

- [ ] Add user authentication backend
- [ ] Implement database storage for user accounts
- [ ] Add JavaScript file extraction
- [ ] Support for image downloads
- [ ] User dashboard to manage downloaded websites
- [ ] Export functionality (ZIP downloads)

## Security Notes

⚠️ **Important**: This application currently does not have backend authentication implemented. The login and signup pages are frontend-only templates.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or support, please open an issue in the repository.

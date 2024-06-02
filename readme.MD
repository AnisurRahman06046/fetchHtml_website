# fetchhtml

`fetchhtml` is a simple Python package to fetch HTML data from a website.

## Installation

You can install the package using pip:

```sh
pip install fetchhtml


Usage
Here's a quick example of how to use the fetchhtml package:

python
Copy code
from fetchhtml import fetchHtml

# Fetch and parse HTML data from a website
soup = fetchHtml('http://example.com', 'html.parser')

# Print the prettified HTML
print(soup.prettify())
Function Details
fetchHtml(website, parser)
Fetches and parses HTML data from the specified website.

Parameters:

website (str): The URL of the website to fetch HTML from.
parser (str): The parser to use with BeautifulSoup (e.g., 'html.parser', 'lxml').
Returns:

soup_data (BeautifulSoup object): Parsed HTML data.
Dependencies
This package requires the following libraries:

requests
beautifulsoup4
These dependencies will be installed automatically when you install the fetchhtml package.

Development
If you want to contribute to the development of this package, follow these steps:

Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/fetchhtml.git
Navigate to the project directory:

sh
Copy code
cd fetchhtml
Install the dependencies:

sh
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions, suggestions, or issues, feel free to open an issue on GitHub or contact me directly at your.email@example.com.

Example of a Real-World Usage
Suppose you want to fetch and parse the HTML content of the Python website:

python
Copy code
from fetchhtml import fetchHtml

# Fetch and parse HTML data from the Python website
soup = fetchHtml('https://www.python.org', 'html.parser')

# Print the title of the page
print(soup.title.string)
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
Changelog
v0.1.0
Initial release of fetchhtml.
Added the fetchHtml function to fetch and parse HTML content from a given URL.
Acknowledgements
This package uses the requests library to make HTTP requests.
It also uses BeautifulSoup for parsing HTML and XML documents.
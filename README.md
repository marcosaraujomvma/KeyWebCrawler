WebKeywordScanner
A simple Python script to scan a list of web pages and their subpages for specific keywords. If the keywords are found, the script saves the URLs and the matching keywords in a text file.

Features
Scans a list of web pages and their subpages.
Searches for user-defined keywords in the visible text of the pages.
Saves results (URLs and keywords found) to a .txt file.
Controls scan depth to avoid infinite loops.
Handles errors gracefully during the scanning process.
Prerequisites
Python 3.6 or higher.
Dependencies
The script uses the following Python libraries:

requests - For making HTTP requests.
beautifulsoup4 - For parsing HTML content.
re - For searching keywords using regular expressions.
urllib.parse - For handling URL manipulations.
Install the required libraries with:

bash
Copiar código
pip install requests beautifulsoup4
Usage
Clone the repository:

bash
Copiar código
git clone https://github.com/your-username/WebKeywordScanner.git
cd WebKeywordScanner
Edit the script:

Define the list of keywords to search for.
Add the start URLs to begin scanning.
Run the script:

bash
Copiar código
python WebKeywordScanner.py
View the results:

Results are saved in resultados.txt in the same directory as the script.
Example content of resultados.txt:
yaml
Copiar código
Scan Results:

URL: https://example.com
Keywords found: voip, calls

URL: https://example.com/subpage
Keywords found: telephony
Configuration
Keywords: Define the list of keywords to search in the keywords variable.
Start URLs: Provide the initial URLs in the start_urls variable.
Scan Depth: Adjust the maximum scan depth by modifying the max_depth parameter in the web_scraper function.
Example
Example configuration in the script:

python
Copiar código
keywords = ["voip", "telephony", "calls"]
start_urls = ["https://www.example.com", "https://another-example.com"]
Example output:

yaml
Copiar código
Scan Results:

URL: https://www.example.com
Keywords found: voip, telephony

URL: https://www.example.com/subpage
Keywords found: calls
Limitations
The script does not handle JavaScript-rendered pages.
Links outside the domain of the start URL are ignored.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Marcos Vinicius Monteiro Araujo
Email: marcosa@cos.ufrj.br
Version: 0.1 (January 7, 2025)


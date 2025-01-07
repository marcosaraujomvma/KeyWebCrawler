"""
WebKeywordScanner

Description:
    This script scans a list of web pages and their subpages for user-provided keywords.
    If keywords are found, the script saves the URLs of the pages and the keywords found to a text file.
    The script also controls the scan depth to avoid infinite loops.

Dependencies:
    - requests: To perform HTTP requests.
    - BeautifulSoup (bs4): To parse the HTML content of the pages.
    - re: To search for keywords using regular expressions.
    - urllib.parse: To handle URL manipulations.

Usage Instructions:
    1. Install the dependencies with `pip install requests beautifulsoup4`.
    2. Replace `keywords` with the list of keywords you want to search for.
    3. Replace `start_urls` with the initial URLs the script should scan.
    4. Run the script.
    5. Check the results in the `resultados.txt` file generated in the same directory as the script.

Settings:
    - `keywords`: List of keywords to search for.
    - `start_urls`: List of initial URLs.
    - `max_depth`: Maximum scan depth for subpages.

Output:
    - A `results.txt` file containing the URLs where keywords were found and the keywords found on each page.

Author:
    Marcos Vinicius Monteiro Araujo
    marcosa@cos.ufrj.br
    01/07/2025
    V 0.1
"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse

# List of keywords to search for
keywords = ["voip", "telefonia", "chamadas","pabx", "turret", "trading"]

# Initial list of URLs
start_urls = ["https://www.gov.br/compras/pt-br", "https://licitacoes-e2.bb.com.br/aop-inter-estatico/" , "https://bll.org.br/" , "https://bnc.org.br/", "https://licitar.digital/","https://licitacoes.caixa.gov.br/SitePages/pagina_inicial.aspx", "https://www.compras.rj.gov.br/"], 

# To avoid loops, keep track of visited URLs
visited_urls = set()

# File to save results
output_file = "results.txt"

# Function to search for keywords on a page
def search_keywords_in_page(url, keywords, output_file):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Search for keywords in the visible text of the page
        text = soup.get_text()
        found_keywords = [kw for kw in keywords if re.search(rf'\b{kw}\b', text, re.IGNORECASE)]
        
        if found_keywords:
            print(f"[Found] Keywords {found_keywords} on URL: {url}")
            # Save the result to the file
            with open(output_file, "a") as file:
                file.write(f"URL: {url}\nKeywords found: {', '.join(found_keywords)}\n\n")
        
        # Return the links found on the page
        return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    except Exception as e:
        print(f"Error accessing {url}: {e}")
        return []

# Main function to perform the scan
def web_scraper(start_urls, keywords, output_file, max_depth=2):
    queue = [(url, 0) for url in start_urls]  # URL and depth
    with open(output_file, "w") as file:
        file.write("Scan Results:\n\n")
    
    while queue:
        url, depth = queue.pop(0)
        
        # Ensure the URL is a string and not a list
        if isinstance(url, list):
            url = url[0]  # If it's a list, take only the first element (in case of queue errors)

        # Check if the URL has already been visited or exceeds the maximum depth
        if url in visited_urls or depth > max_depth:
            continue
        
        visited_urls.add(url)  # Add the URL to the set of visited URLs
        print(f"Visiting: {url} (Depth: {depth})")
        
        # Search for keywords and extract subpages
        subpages = search_keywords_in_page(url, keywords, output_file)
        
        # Add subpages to the queue with incremented depth
        for subpage in subpages:
            if subpage not in visited_urls and urlparse(subpage).netloc == urlparse(url).netloc:
                queue.append((subpage, depth + 1))

# Run the scraper
web_scraper(start_urls, keywords, output_file, max_depth=8)

# Wikipedia Top Articles Scraper

This Python script scrapes the top 10 articles from the [Wikipedia Pageviews Analysis page](https://pageviews.wmcloud.org/topviews/?project=en.wikipedia.org&platform=all-access&date=last-month&excludes=) and extracts the title and first paragraph of each article. The extracted data is then saved to a JSON file called "wikipedia_top_articles.json".

## Dependencies

- Python 3.7+
- BeautifulSoup4
- Requests
- Selenium WebDriver

## Installation

1. Clone the repository:

```bash
git clone https://github.com/munir2200963/WikipediaTopArticlesScraper.git

2. Change directory:

```bash
cd WikipediaTopArticlesScraper

3. Install the required packages in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

4. Download the appropriate Selenium WebDriver for your browser and add its location to your system's PATH variable.

## Usage

1. Run the script:
```bash
python main.py

2. The scraped data will be saved to a file called "wikipedia_top_articles.json".

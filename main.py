import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to get the URLs of the top articles
def get_top_articles_url():
    # URL to scrape the top articles
    url = "https://pageviews.wmcloud.org/topviews/?project=en.wikipedia.org&platform=all-access&date=last-month&excludes="

    # Set up the selenium webdriver
    driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
    driver.get(url)

    # Wait for the page to load and the first top article to be present
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#topview-entry-1 > td.topview-entry--label-wrapper > div > a")))

    top_articles = []

    # Iterate through the top 10 articles
    for i in range(1, 11):
        # CSS selector for each article
        article_selector = f"#topview-entry-{i} > td.topview-entry--label-wrapper > div > a"

        # Get the article URL and title using the CSS selector
        article_url = driver.find_element(By.CSS_SELECTOR, article_selector).get_attribute("href")
        article_title = driver.find_element(By.CSS_SELECTOR, article_selector).text

        # Append the article title and URL to the top_articles list
        top_articles.append({
            "title": article_title,
            "url": article_url
        })

    # Close the browser
    driver.quit()

    return top_articles


# Function to get the article title and first paragraph
def get_article_data(article_url):
    # Send an HTTP request to the article URL
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the article title and first paragraph
    title = soup.select_one("#firstHeading").text
    first_paragraph = soup.select_one("#mw-content-text .mw-parser-output p:not(.mw-empty-elt)").text.strip()

    return {
        "title": title,
        "first_paragraph": first_paragraph,
    }


# Get the URLs of the top articles
top_articles = get_top_articles_url()
articles_data = []

# Scrape the article data (title and first paragraph) for each top article
for article in top_articles:
    print(f"Scraping {article['title']}...")
    article_data = get_article_data(article["url"])
    articles_data.append(article_data)

# Save the scraped data to a JSON file
with open("wikipedia_top_articles.json", "w", encoding="utf-8") as outfile:
    json.dump(articles_data, outfile, ensure_ascii=False, indent=4)

print("Top Wikipedia article data has been saved to 'wikipedia_top_articles.json'")

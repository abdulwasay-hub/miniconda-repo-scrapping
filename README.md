# Miniconda Repository Version Scraper

## Project Overview
This project is a Python-based web scraper designed to extract available Miniconda version information from the Conda repository page. It creates a CSV file containing all available versions for download. The project uses the **Scrapy** library for web scraping and adheres to best practices by organizing the scraping logic within a structured Scrapy project.

## Key Features
- Scrapes the Miniconda repository page to extract version information.
- Stores the extracted data in a CSV file.
- Built using the powerful **Scrapy** framework.
- Organized with a structured project containing dedicated folders and files generated using terminal commands.

## Requirements
- Python 3.8 or above
- Miniconda (or any Python environment manager)
- Required Python packages:
  - **Scrapy**

Install the necessary packages using:
```bash
pip install scrapy
```

## Setup Instructions

### 1. Create the Scrapy Project
Run the following commands in the terminal to create and navigate the project:
```bash
scrapy startproject miniconda_scraper
cd miniconda_scraper
scrapy genspider conda_versions <repository_url>
```
Replace `<repository_url>` with the URL of the Miniconda repository page.

### 2. Implement the Spider Logic
Modify the `spider.py` file (located in the `spiders` folder) with the scraping logic. The spider will extract version information and save it in a structured format.

### 3. Run the Spider
Execute the spider to scrape the data and save it to a CSV file:
```bash
scrapy crawl conda_versions -o versions.csv
```
This command runs the spider and outputs the scraped data to `versions.csv` in the project's root directory.

### 4. View the Results
Open the `versions.csv` file to view the extracted Miniconda version information.

## File Structure
Below is an overview of the project's file structure:
```
miniconda_scraper/
    scrapy.cfg
    miniconda_scraper/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            conda_versions.py  # Contains the spider logic
```

## Usage
- Clone the repository or download the project files.
- Ensure you have the required environment and dependencies set up.
- Modify the spider file if you want to scrape additional information.
- Run the spider and access the output CSV for the scraped data.

## Additional Notes
- The project is designed for educational purposes to demonstrate the use of Scrapy for web scraping.
- Make sure to adhere to the website's terms of service while scraping.

## License
This project is open-source and available under the MIT License. Feel free to modify and share it.


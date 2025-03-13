# Web Scraping 

## Overview
This project is a web scraping script written in Python that extracts data from a specified website and exports the collected information into an Excel sheet.

## Features
- Extracts data from a target website
- Cleans and structures the scraped data
- Saves the data into an Excel (.xlsx) file
- Handles exceptions and errors gracefully

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Required Python libraries:
  ```bash
  pip install requests beautifulsoup4 pandas openpyxl
  ```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/webscraping-project.git
   cd webscraping-project
   ```

2. Run the script:
   ```bash
   python scraper.py
   ```

3. The scraped data will be saved as `output.xlsx` in the project directory.

## Configuration
- Modify `scraper.py` to change the target website, scraping logic, and exported data format.
- Customize the output file name and sheet name as needed.

## Error Handling
- The script includes error handling for common issues like missing data, invalid URLs, and connection timeouts.
- Log messages help track errors and debugging.

## Author
tamizhanban.n2022cse@sece.acx.in


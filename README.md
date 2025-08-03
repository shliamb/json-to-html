
# 📥 Python Script JSON to HTML
** supa-easy

Simple Python script for generating static HTML pages from JSON data. Built for personal use, potentially evolving into a basic CMS.

## Features

- Generates static HTML pages from JSON configuration
- Creates pricing tables with JSON-LD markup
- Fast, lightweight, and crash-resistant static output
- Easy FTP deployment

## Requirements

- Python 3.x
- Manual creation of directories specified in `config.py`
- `data.json` file with page data (see example format)

## Setup

1. Clone repository
2. Create directories as defined in `config.py`
3. Configure `data.json` with your page data
4. Modify HTML templates in `html.py` to match your design
5. Run: `python run.py`

## Usage

The script reads `data.json` and generates complete HTML pages by:
- Inserting data into predefined template fields
- Building pricing tables
- Generating JSON-LD structured data

## Future Plans

- AI integration for automated page generation
- AI-driven JSON data creation and page assembly
- Evolution into full CMS functionality

## Output

Static HTML files ready for FTP upload - maximum speed and reliability for simple websites.

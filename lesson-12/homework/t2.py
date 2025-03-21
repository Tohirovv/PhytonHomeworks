import sqlite3
import requests
import csv

from bs4 import BeautifulSoup
from datetime import datetime


def initialize_database():
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs(
Job_Title TEXT,
Company Name TEXT,
Location TEXT,
Job_Description TEXT,
Application Link TEXT
UNIQUE(job_title, company_name, location)
);
""")

    conn.commit()


def scrape_jobs(url):
    response = requests.get(url)
    soap = BeautifulSoup(response.text, 'html.parser')
    job_listing = []
    for job_item in soap.find_all('div', class_="card-content"):
        job_title = job_item.find('h2', class_='title is-5').text().strip()
        company_name = job_item.find('h3', class_='subtitle is-6 company').text().strip()
        location = job_item.find('p', class_='location').text().strip()

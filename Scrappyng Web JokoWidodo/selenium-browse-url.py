import argparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
full_text = []

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', default='', help='sample-url-for-browse')
    parser.add_argument('-o', '--outfile', default='', help='hasil-browse-2D')
    return parser.parse_args()

def main():
    args = parse_args()
    outfile = args.outfile
    infile = args.infile

    with open(infile) as f:
        urls = f.read().splitlines()

    filtered_text_2D = []

    for i, url in enumerate(urls):
        driver.get(url)
        elems = driver.find_element(By.TAG_NAME, 'body').text.split('\n')
        filtered_text = [f'["{line.strip()}"]' for line in elems if len(line.split()) >= 5]
        filtered_text_2D.extend(filtered_text)
        
        # Tambahkan baris kosong kecuali untuk URL terakhir
        if i < len(urls) - 1:
            filtered_text_2D.append('[" "]')

    # Format output dalam bentuk list 2 dimensi
    formatted_output = '['
    for line in filtered_text_2D:
        formatted_output += '\n\t' + str(line) + ','

    formatted_output = formatted_output.rstrip(',') + '\n]'

    # Tulis output ke file
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(formatted_output)

    driver.close()
main()
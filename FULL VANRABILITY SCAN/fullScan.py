 # The The following programe run, a full scan based on the following highligted comments.
import requests
from bs4 import BeautifulSoup

# Function to check for common security vulnerabilities on a web page
def check_vulnerabilities(url):
    vulnerabilities = []

    # Check for open redirect
    try:
        response = requests.get(url)
        if 'redirect' in response.url:
            vulnerabilities.append('Open Redirect')

        # Check for sensitive information in response
        if 'password' in response.text.lower() or 'secret' in response.text.lower():
            vulnerabilities.append('Sensitive Information Exposure')

        # Check for insecure HTTP methods
        headers = requests.head(url).headers
        methods = headers.get('Allow', '').split(',')
        insecure_methods = ['PUT', 'DELETE']
        if any(method in methods for method in insecure_methods):
            vulnerabilities.append('Insecure HTTP Methods')
    except requests.RequestException as e:
        print(f"Error checking vulnerabilities: {e}")

    return vulnerabilities

# Function to crawl and check a web mobile banking site
def crawl_site(url):
    print(f"Crawling {url} for vulnerabilities...")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for common issues
        vulnerabilities = check_vulnerabilities(url)
        print(f"Found vulnerabilities: {', '.join(vulnerabilities) if vulnerabilities else 'None'}")

        # Example: find all forms and check for CSRF tokens
        forms = soup.find_all('form')
        for form in forms:
            if not form.find('input', {'name': 'csrf_token'}):
                print("Possible missing CSRF token in form.")
    except requests.RequestException as e:
        print(f"Error crawling site: {e}")

# Main function to initiate scanning
def main():
    url = input("Enter the URL of the mobile banking site: ")

    # Crawl and check the web site
    crawl_site(url)

if __name__ == '__main__':
    main()

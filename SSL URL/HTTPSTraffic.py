from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Modify the request here
    pass

def response(flow: http.HTTPFlow) -> None:
    # Modify the response here
    pass
# ensure you have mitmproxy installed to run the proxy, run with this command, mitweb "pip install mitmproxy"
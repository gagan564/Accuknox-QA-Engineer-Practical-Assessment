import requests # type: ignore
import sys

def check_application_status(url):
    try:
        response = requests.get(url, timeout=10)  # Timeout after 10 seconds
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"
    except requests.exceptions.RequestException as e:
        return "DOWN"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_uptime.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    status = check_application_status(url)
    print(f"The application at {url} is {status}.")

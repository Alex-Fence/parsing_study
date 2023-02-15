from fake_headers import Headers
from requests import get
from fake_useragent import UserAgent

if __name__ == "__main__":
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()

    # for i in range(10):
    #     print(header.generate())
    ua = UserAgent()
    r = get(url='http://httpbin.org/user-agent', headers={'user_agent': ua.random})
    print(r.text)

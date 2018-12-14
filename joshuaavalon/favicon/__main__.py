from argparse import ArgumentParser
from io import BytesIO
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from PIL import Image
from bs4 import BeautifulSoup


def main():
    parser = ArgumentParser(description="Download favicon from urls")
    parser.add_argument("urls", nargs="+", type=str,
                        help="Urls to be downloaded")
    parser.add_argument("-s", "--size", type=int, default=16,
                        help="Icon maximum size")
    args = parser.parse_args()
    size = args.size, args.size
    for url in args.urls:
        if not url.startswith("http"):
            url = f"http://{url}"
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        icon = find_icon(soup)
        if icon is None:
            icon = urljoin(url, "favicon.ico")
        r = requests.get(icon, stream=True)

        domain = urlparse(url).netloc
        if r.status_code == 200:
            try:
                image = Image.open(BytesIO(r.content))
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(f"{domain}.png", "png")
            except IOError as e:
                print(f"Failed {url}: {e}")
        else:
            print(f"Failed {url}: {r.status_code}")


def find_icon(soup: BeautifulSoup) -> Optional[str]:
    shortcut = soup.select_one("link[rel*='shortcut icon']")
    if shortcut is not None:
        return shortcut["href"]
    apple = soup.select_one("link[rel*='apple-touch-icon']")
    if apple is not None:
        return apple["href"]
    return None


if __name__ == "__main__":
    main()

__version__ = "0.0.1a"

from seleniumbase import SB, BaseCase
import threading
import time

def give_traffic(url: str, out_link:str, loops: int = 1) -> None:
    with SB(uc=True) as driver:
        driver: BaseCase = driver
        driver.generate_traffic(url, out_link, loops=loops)

def generate_views_shorts(code: str, n_threads: int = 1):
    def run_time():
        with SB(uc=True) as driver:
            driver: BaseCase = driver
            driver.get("https://www.youtube.com/shorts/" + code)
            while True:
                time.sleep(1)
    for _ in range(n_threads):
        threading.Thread(target=run_time).start()

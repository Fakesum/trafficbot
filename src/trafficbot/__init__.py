__version__ = "0.0.1a"

from seleniumbase import SB, BaseCase

def give_traffic(url: str, out_link:str, loops: int = 1):
    with SB(uc=True) as driver:
        driver: BaseCase = driver
        driver.generate_traffic(url, out_link, loops=loops)

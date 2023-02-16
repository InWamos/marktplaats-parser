from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class LastOffer:
    name: str
    link: str

    def __str__(self) -> str:
        return f"Новый автомобиль!\n🚘 Название: {self.name}\n🔗 Ссылка: {self.link}"

def find_last_offer(page_code: str) -> None:
    
    soup = BeautifulSoup(page_code, 'html.parser')
    soup.find("div", )

    # hz-Page-element hz-Page-element--main with-exp-cars-filters <-- Div with offers

ListOfParsedPages = list
def parse_new_offers(parsed_pages: ListOfParsedPages):

    ...

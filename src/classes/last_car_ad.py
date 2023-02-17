from dataclasses import dataclass

@dataclass
class LastCarAdvertisement:
    """Dataclass. Consists of 3 variables, used to provide a return of
    get_last_advertisement()

    Returns:
        LastOffer: consists of
            link to the page with advertisements(link_to_page),
            link to certain advertisement(link_to_advertisement),
            name of the advertisement(name);
    """
    link_to_page: str
    link_to_advertisement: str
    name: str

    def __str__(self) -> str:
        return f"Новый автомобиль!\n🚘 Название: {self.name}\n🔗 Ссылка: {self.link_to_advertisement}"
  
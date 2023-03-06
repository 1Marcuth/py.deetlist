from pydantic import validate_arguments
from datetime import datetime
from parsel import Selector
import calendar

from ...settings import DRAGON_ELEMENTS
from ...utils.time_parser import (
    parse_attack_training_time,
    parse_summon_time,
    parse_breed_time,
    parse_hatch_time
)

MONTHS = { month: index for index, month in enumerate(calendar.month_abbr) if month }

class DragonPageParser:
    @validate_arguments
    def __init__(self, html: str) -> None:
        self.__selector = Selector(html)

    @property
    def name(self) -> str:
        name = self.__selector.css("h1::text").get()
        return name
    
    @property
    def rarity(self) -> str:
        rarity_classes = self.__selector.css("div.img_rar::attr(class)").get()
        rarity = rarity_classes.split()[0].split("_")[2].upper()
        return rarity

    @property
    def elements(self) -> list[str]:
        elements = []

        elements_classes = self.__selector.css("#typ_hull .typ_i::attr(class)").getall()

        for element_classes in elements_classes:
            abbreviated_element_name = element_classes.split()[1].split("_")[1]
            elements.append(DRAGON_ELEMENTS[abbreviated_element_name])

        return elements

    @property
    def image_url(self) -> str:
        image_url = (self.__selector
            .css("img.drg_img::attr(src)")
            .get()
            .replace("../", "https://deetlist.com/dragoncity/"))

        return image_url

    @property
    def description(self) -> str:
        description = self.__selector.css("div#self_bio::text").getall()[-1].strip()
        return description

    @property
    def __basic_attacks(self) -> list[dict]:
        attacks_selector = self.__selector.css(".b_split .att_hold")[0:4]

        attacks = []

        for attack_selector in attacks_selector:
            attack_selector_texts = attack_selector.css("::text").getall()

            name = attack_selector_texts[3].strip()

            element = (attack_selector_texts[5]
                .split("|")[1]
                .strip())

            damage = (attack_selector_texts[5]
                .split("|")[0]
                .removeprefix("Damage:")
                .strip())

            if damage.isnumeric():
                damage = int(damage)

            else:
                damage = None

            attacks.append(dict(
                name = name,
                element = element,
                damage = damage
            ))

        return attacks

    @property
    def __trainable_attacks(self) -> list[dict]:
        attacks_selector = self.__selector.css("div.b_split+ div.b_split div.att_hold")

        attacks = []

        for attack_selector in attacks_selector:
            attack_selector_texts = attack_selector.css("::text").getall()

            name = attack_selector_texts[3].strip()

            element = (attack_selector_texts[5]
                .split("|")[1]
                .strip())

            damage = (attack_selector_texts[5]
                .split("|")[0]
                .removeprefix("Damage:")
                .strip())

            training_time = parse_attack_training_time(
                attack_selector_texts[5]
                    .split("|")[2]
                    .strip()
            )

            if damage.isnumeric():
                damage = int(damage)

            else:
                damage = None

            attacks.append(dict(
                name = name,
                element = element,
                damage = damage,
                training_time = training_time
            ))

        return attacks

    @property
    def attacks(self) -> dict:
        return dict(
            basics = self.__basic_attacks,
            trainables = self.__trainable_attacks
        )

    @property
    def strengths(self) -> list[str]:
        strengths_selector = self.__selector.css(".spc2+ .b_split .typ_i")
        strengths = []

        for strength_selector in strengths_selector:
            strength = (strength_selector
                .css("::attr(class)")
                .get()
                .split()[1]
                .removeprefix("tb_"))

            if strength in DRAGON_ELEMENTS:
                strength = DRAGON_ELEMENTS[strength]

            strengths.append(strength)

        return strengths

    @property
    def weaknesses(self) -> list[str]:
        weaknesses_selector = self.__selector.css(".b_split+ .b_split .typ_i")
        weaknesses = []

        for weakness_selector in weaknesses_selector:
            weakness = (weakness_selector
                .css("::attr(class)")
                .get()
                .split()[1]
                .removeprefix("tb_"))

            if weakness in DRAGON_ELEMENTS:
                weakness = DRAGON_ELEMENTS[weakness]

            weaknesses.append(weakness)

        return weaknesses

    @property
    def book_index(self) -> int | None:
        book_index = self.__selector.css("#did .dt::text").get()

        if book_index:
            return int(book_index)

    @property
    def category(self) -> int:
        category = int(self.__selector.css("#dc .dt::text").get())
        return category

    @property
    def is_breedable(self) -> bool:
        is_breedable = self.__selector.css("#br .dt::text").get() == "Yes"
        return is_breedable

    @property
    def summmon_time(self) -> int:
        summmon_time = parse_summon_time(self.__selector.css("#bt::text").get())
        return summmon_time

    @property
    def breed_time(self) -> int:
        breed_time = parse_breed_time(self.__selector.css("#bt::text").get())
        return breed_time

    @property
    def hatch_time(self) -> int:
        hatch_time = parse_hatch_time(self.__selector.css("#ht .dt::text").get())
        return hatch_time

    @property
    def xp_on_hatch(self) -> int:
        xp_on_hatch = int(self.__selector.css("#hx .dt::text").get())
        return xp_on_hatch

    @property
    def release_timestamp(self) -> int | None:
        release_date = self.__selector.css("#dc::text").get().strip()

        if release_date:
            day, month, year = release_date.split("-")

            day = int(day)
            month = MONTHS[month]
            year = int(year)

            release_timestamp = int(datetime(
                day=day,
                month=month,
                year=year
            ).timestamp())

            return release_timestamp

    @property
    def sell_price(self) -> dict:
        price, type = (self.__selector
            .css("#sp .dt::text")
            .get()
            .split(" "))

        price = int(price)
        type = type.lower()

        return dict(
            price = price,
            type = type
        )

    @property
    def production(self) -> dict:
        starting_income, level_up_increase = [
            int(string.split(":")[1])
            for string in self.__selector.css(".spc2~ .norm_h+ p::text").getall()
        ]

        return dict(
            starting_income = starting_income,
            level_up_increase = level_up_increase
        )

    def get(self) -> dict:
        return dict(
            name = self.name,
            rarity = self.rarity,
            elements = self.elements,
            image_url = self.image_url,
            description = self.description,
            attacks = self.attacks,
            strengths = self.strengths,
            weaknesses = self.weaknesses,
            book_index = self.book_index,
            category = self.category,
            is_breedable = self.is_breedable,
            summon_time = self.summmon_time,
            breed_time = self.breed_time,
            hatch_time = self.hatch_time,
            xp_on_hatch = self.xp_on_hatch,
            release_timestamp = self.release_timestamp,
            sell_price = self.sell_price,
            production = self.production
        )

__all__ = [ DragonPageParser ]
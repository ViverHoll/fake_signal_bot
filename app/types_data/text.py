from dataclasses import dataclass


@dataclass
class Text:
    id_: int
    not_sub: str
    manual: str
    main_menu: str

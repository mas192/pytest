from dataclasses import dataclass, field
from laxleague.src.laxleague.guardian import Guardian
from typing import List

@dataclass()
class Player():
    """ A lacrosse player in the league """
    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)
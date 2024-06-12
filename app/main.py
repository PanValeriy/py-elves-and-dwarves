from __future__ import annotations

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> str:
    return "\n".join(elf.play_elf_song() for elf in elves)


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> str:
    return "\n".join(dwarf.eat_favourite_dish() for dwarf in dwarves)

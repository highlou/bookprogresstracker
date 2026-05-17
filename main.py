# Created 2026-05-17

from __future__ import annotations

'''
Schedule and keep track of your books!

UI
- terminal, command based
- Commands:
  - ls: list all books
  - add: add a book
    - Successive prompts ask about the scheduling, etc.
      - probably should give the option for days off
        - days per week, days per month, every X days, etc.
      - option A: by given DATE it should be finished
        > calculates the number of chapters per day
      - option B: given NO. of chapters per day
  - del/rem: delete/remove a book
  - help: list all commands
  - update: update a book (progress, etc.)
  - book: show information progress on book
> When the user opens the program, it should say hello, the date, and what ought
  be done today
'''

from dataclasses import dataclass
from datetime import datetime

ST_CHAPTERED = "chaptered"
ST_PAGED = "paged"

TT_GIVEN_DATE = "given date"
TT_GIVE_NO_PER_DAY = "given no. of sections per day"

@dataclass
class Book:
    title: str
    subtitle: str
    volume: int
    edition: int
    author: str|list[str]
    sections: int # either chapters or pages
    section_type: str # either ST_CHAPTERED or ST_PAGED

@dataclass
class Task:
    book: Book
    progress: int
    task_type: str # only the TT_* constants
    end_date: datetime.date # last date where there is reading
    no_per_day: int
    rest_days_of_week: int # ISO day of the week number
    rest_days_of_month: list[int]
    rest_days_of_year: list[datetime.date]
    rest_days_periodic: list[int]

    @staticmethod
    def create_from_given_date() -> Task:
        pass
    
    @staticmethod
    def create_from_no_per_day() -> Task:
        pass
    
    def calculate_end_date(self) -> int|list[int|datetime.date]:
        pass

if __name__ == '__main__':
    print('hello')

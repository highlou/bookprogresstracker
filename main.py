# Created 2026-05-17

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

if __name__ == '__main__':
    print('hello')

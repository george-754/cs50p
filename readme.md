# cs50p from edx

### indoor.py
`python3 indoor.py` - converts a user inputed string to all lowercase.

### playback.py
`python3 playback.py`- replaces spaces between words with "..." on a user inputed string.

### faces.py
`python3 faces.py` - converts any emoticons to emoji's from a user inputed string. i.e. :)

### einstein.py
`python3 einstein.py` - prompts user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.

### tip.py
`python3 tip.py` - tip calculator. Enter the meal amout and what percentage you would like to leave.

### deep.py
`python3 deep.py` - prompts user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise outputs `No`.

### bank.py
`python3 bank.py` - promts the user for a greeting. If the greeting starts with "hello", output `$0`. If the greeting starts with an "h" (but not "hello"), output `$20`. Otherwise, output `$100`.

### extensions.py
`python3 extensions.py` - prompts the user for the name of a file and then outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:
- `.gif`
- `.jpg`
- `.jpeg`
- `.png`
- `.pdf`
- `.txt`
- `.zip`

### interpreter.py
`python3 interpreter.py` - prompts user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Format `x y z`.
- `x` is an integer
- `y` is `+`,`-`,`*`,or `/`
- `z` is an integer

### meal.py
`python3 meal.py` - prompts user for a time and outputs whether it's `breakfast time`, `lunch time`, or `dinner time`. If it's not time for a meal, then nothing is output to screen. User's input is formatted in 24-hour time as `#:##` or `##:##`, or 12-hour time as `#:## a.m.`, `##:## a.m.`, `#:## p.m.` or `##:## p.m.`

### camel.py
`python3 camel.py` - prompts user for the name of a variable in camel (`firstName`) case and outputs the corresponding name in snake case (`first_name`).

### coke.py
`python3 coke.py` - prompt user to insert a coin (`25`, `10`, `5`), one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, then output how many cents in change the user is owed.

### twttr.py
`python3 twttr.py` - prompt user for a `str` of text and then outputs that same text but with all vowels (A, E, I, O and U) omitted.

### plates.py
`python3 plates.py` - prompt the user for a vanity plate and then output `Valid` if meets all of the requirements or `Invalid` if it does not. Any letters in the input should be uppercase. Format:
- All vanity plates must start with at least two letters.
- Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate. They must come at the end. The first number used cannot be a `0`.
- No periods, spaces, or punctuation marks are allowed.

### nutrition.py
`python3 nutrition.py` - prompt user to input a fruit and then outputs the number of calories in one portion of that fruit, per the FDA's poster for fruits.

### fuel.py
`python3 fuel.py` prompt user for a fraction, formatted as `X/Y`, where `X` and `Y` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.

### taqueria.py
`python3 taqueria.py` - place an order entering one item at a time, when done press `control-d`. After each item is entered the total cost will be displayed of all the items entered. Menu:
```
Baja Taco
Burrito
Bowl
Nachos
Quesadilla
Super Burrito
Super Quesadilla
Taco
Tortilla Salad
```

### grocery.py
`python3 grocery.py` - prompt user for items, one per line, until the user inputs `control-d`. Then ouputs the user's grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.

### outdated.py
`python3 outdated.py` - prompt user for a date formatted like `9/1/2022` or `September 1, 2022`. Then outputs the date in `YYYY-MM-DD` format.

### emojize.py
`python3 emojize.py` -prompt user for a `str` in English and then outputs the "emojized" version of that `str` to the corresponding emoji. [Emoji List](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias)
Uses `emoji` library

### figlet.py
- `python3 figlet.py` - outputs user inputted text with a random font.
- `python3 figlet.py -f *font*` or `python3 figlet.py --font *font*` - outputs text with the applied font.
Uses library `pyfiglet`

### adieu.py
`python3 adieu.py` - prompt user for names, one per line, until user inputs `control-d`. Outputs adieu to those names. Uses library [inflect](https://pypi.org/project/inflect)

### game.py
`python3 game.py` - guessing game that gets user input for a level which is the maximum number for the range of numbers to guess from. Then prompts user to guess that number outputting `Too small!`, `Too large!`, or `Just right!` until the number is guessed. Uses library [random](https://docs.python.org/3/library/random.html).

### professor.py
`python3 professor.py` - prompt user for a level `1`, `2`, or `3`. Then randomly generates 10 math problems formatted as `X + Y =`. Then prompts user to solve each of those problems. If an answer is not correct up to three times then the program will output the correct answer. The program will output the user's score, a number out of 10. Uses [random](https://docs.python.org/3/library/random.html) module

### bitcoin.py
`python3 bitcoin.py *shares*` - Outputs the current cost of shares of bitcoin in USD to four decimal places, using `,` as a thousands separator. Uses `sys` module and [requests](https://requests.readthedocs.io/en/latest/) module

### test_*app*.py
Uses `pytest` to test these apps.

### lines.py
`python3 lines.py *file.py*` - outputs the number of lines of code in a file, excluding comments and blank lines. 

### pizza.py
`python3 pizza.py *file.csv*` - outputs a table formatted as ASCII art using [tabulate](https://pypi.org/project/tabulate), a package on PyPI.

### scourgify.py
`python3 scourgify.py *existing.csv* *output.csv*` - converts the existing.csv to the output.csv, splitting each name into a first name and a last name. Uses [csv](https://docs.python.org/3/library/csv.html) module.

### shirt.py
`python3 shirt.py *input.jpeg or .png* *output.jpeg or .png*` - program that overlays shirt.png on the input after resizing and cropping the input to be the same size and saves the result as its output. Uses [Pillow](https://pypi.org/project/Pillow/) package.

### numb3rs.py
`python3 numb3rs.py` - gets an IPv4 address as input as a `str` and then returns `True` or `False`, respectively, if that input is a valid IPv4 address or not. Uses `re` module. [Regular Expressions](https://docs.python.org/3/library/re.html)

### watch.py
`python3 watch.py` - gets a `str` input of HTML, extracts any YouTube URL that's the value of a `src` attribute of an `iframe` element therein, and returns its shorter, shareable `youtu.be` equivalent as a `str`. Expected input formats:
```
- http://youtube.com/embed/xvFZjo5PgG0
- https://youtube.com/embed/xvFZjo5PgG0
- https://www.youtube.com/embed/xvFZjo5PgG0
```

### working.py
`python3 working.py` - gets input as a `str` in either of the 12-hour formats `9:00 AM to 5:00 PM` or `9 AM to 5 PM` and outputs a `str` in 24-hour format `9:00 to 17:00`. `AM` and `PM` must be capitalized with no periods therein and a space before each. Uses [re](https://docs.python.org/3/library/re.html) module.

### um.py
`python3 um.py` - get input as a `str` and returns, as an `int`, the number of times that "um" appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. uses [re](https://docs.python.org/3/library/re.html) module.

### response.py
`python3 response.py` - prompts user for an email address and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address. Makes use of eiter or `validator-collection` or `validators` packages.

### seasons.py
`python3 seasons.py` - prompts user for their date of birth in `YYYY-MM-DD` format and then prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from *Rent*, without any `and` between words. Uses the `date` class and [inflect](https://pypi.org/project/inflect/) module.

### jar.py
`jar.py` is a custom python class file. And `test_jar.py` is used to test the `jar.py` class file. 
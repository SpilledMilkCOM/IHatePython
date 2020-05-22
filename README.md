# I Hate Python :rage:

## :scroll: Backstory

I remember way back in the day (2002) I was laid off, got 6 months of severance, and started to look for my "dream job".
I networked and interviewed like crazy, submitting my resume to the likes of Pixar, ILM, and Digital Domain.
I **finally** got a phone screen/interview with Dreamworks.  Things were going amazingly well until that fatal question "Do you know Python?".
I said no. Right then and there the interview was pretty much over. It's as if someone said "My socks are pink" *(inside joke)* and the interview wrapped up.

After the interview I hopped on the internet and found that Python was just another scripting language.  **SERIOUSLY?**  Like I couldn't learn another scripting language in about a week?  I took a look at it and was **not** impressed.  Since when does **white space** matter?  Is this the FORTRAN of scripting languages?  I'll stick with my `.bat` files and C++ thank you very much.

Cut to 18 years later (5/18/2020) and I'm trying to see what all the damn hype is about Python.  I **LOVE** Monty Python 🥥🥥🦜, so I figured I'd give it another go.  And this is my story as it unfolds...

## :dvd: Install the Latest Version of Python

* [Download Python](https://www.python.org/downloads/)
* Version 3.8.3 (as of 5/19/2020)

## :computer: Setup [Visual Studio Code](https://code.visualstudio.com/)

* Select the Python interpreter (probably if you have multiple versions of Python).
* Visual Studio Code prompts (recommends) `pylint`

I installed Python in the default directory, which I'm guessing is `~\AppData\Local\Programs\Python` since I wasn't paying much attention.
I have not cluttered up my `path` variable with all of the Python stuff, so I've been doing everything "brute force". *(You should also be able to use the `py` alias if everything is installed correctly.)*

    ~\AppData\Local\Programs\Python\Python38-32\Scripts\pip.exe install pylint

I installed the linter, but it will also nag at you saying that your version of `pip` is out of date and to run the following command.

    ~\AppData\Local\Programs\Python\Python38-32\python.exe -m pip install --upgrade pip

Once you've created your "Hello World" file, then you'll want to set up the debugger tell it what version of Python you want to use and the location of the `python.exe` file which is stored in the `settings.json` file.  You will also need a `launch.json` file which describes how the debugger will launch.  VS Code has a template for this where you can use the current active file or attach to a process.

## :thought_balloon: Thoughts (COULD be more of a rant)

When I first looked at Python quite a few years ago I immediately hated it *"What do you mean **whitespace** matters? Are we back in the FORTRAN days?"*

And I'm almost **POSITIVE** that there are people out there that insist on using spaces, and probably only **TWO**.

Right now, I don't **hate** it, but after using it a bit...  It **really** feels like BASIC *(I'm assuming **without** the GOTOs)*

### Syntax

The choice to exclude `++`?  I don't get it.  If you have the `+=` operator, then why not include `++`?  Did C++ patent the use of `++`?  I don't think so.

`except` vs `catch`?  Maybe I'm just so used to the "try/catch" syntax that "except" seems so foreign to me. "Handle your exceptions in the `except` block." Hmmmm...  Maybe that **does** sound better than "Handle your exceptions in the `catch` block".

So basically a colon ":" says that there is **"more"** to come, and as long as it's indented then **that's** the block of code which is "more".

### :book: Documention

"Type Hinting" wasn't added until 3.5, but I would definitely recommend this for more readable and structured code.

`docstrings` allow you to document your code as explained down in the **References** section below.

I'm **STILL** struggling to see **why** people are so gaga over Python.  Maybe I'll get it one day.  And then again...

### Things I Need to Try

* Inheritance / Interfaces / Polymorphism
* Public / Private?
* IoC Container
* Website
* Threading
* Unit Tests
* [Blender](https://www.blender.org/) (Application Scripting)

## :books: References

* [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
* [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)
* [Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)
* [django - web development](https://docs.djangoproject.com/)
* [Markdown Emojis](https://www.webfx.com/tools/emoji-cheat-sheet)
* [Copy+Paste Emojis Into Markdown File](https://emojis.wiki/)

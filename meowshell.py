import random
import os
import pathlib
import click
from rich.console import Console

console = Console()

# 🔹 Unique themed cats per command
CAT_ART = {
    "sniff": r"""
     /\_/\ sniff sniff...
    ( - . - )
     > ^ <
    """,

    "slink": r"""
     |\___/|    
    (=^‥^=)    
     )   (     
    (     )    
    (___(__)
    Entering your new lair...
    """,

    "nest": r"""
     |\_._/|        
    /       \      
   (  ◕   ◕  )      
   >         <      
  /           \     
 (             )    
(__(__)___(__)__)
  Built a cozy little box.
    """,

    "nap": r"""
    z Z Z Z
     |\      _,,,---,,_
     /,`.-'`'    -.  ;-;;,_
    |,4-  ) )-,_. ,\ (  `'-'
   '---''(_/--'  `-'\_)
     snoozing...
    """,

    "chaos": r"""
    /\___/\
   ( o   o )
   (  =^=  )
   (        )
   (         )
   (          )))))))))))
   TOO MANY CATS
    """,

    "yowl": r"""
     ╭∩╮(ಠ_ಠ)╭∩╮
    (╯°□°）╯︵ ┻━┻
     *SCREEEAAAMMMM*
    """,

    "judge": r"""
     😼 Judgement Cat
     /\_/\  
    ( o.o ) 
     > ^ <  
     I'll allow it... maybe.
    """,

    "summon": r"""
     /\_/\     /\_/\     /\_/\
    ( o.o )   ( o.o )   ( o.o )
     > ^ <     > ^ <     > ^ <
     MULTICAT SUMMONED
    """,

    "pawpoke": r"""
     ┏(=^･^)=┛
     *poke poke*
     Touched the file.
    """
}

# 🔸 Default random cats (fallback/random)
CATS = [
    r"""
        |\---/|
        | o_o |
         \_^_/
    """,
    r"""
     /\     /\
    {  `---'  }
    {  O   O  }
~~>  V__^Y^__V
     /     \
    (  )-(  )
    ""     ""
    (       )
    (        )
    (         )
    (          )))))))))))
    """,
    r"""
     |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
    |,4-  ) )-,_. ,\ (  `'-'
   '---''(_/--'  `-'\_)
    """,
    r"""
      |\_._/|        
     /       \      
    (  ◕   ◕  )      
    >         <      
   /           \     
  (             )    
 ( (  )     (  ) )   
(__(__)___(__)__)
    """,
    r"""
        /\_/\     
       ( o.o )    
        > ^ <     
      CAT HACKER
    """
]

# 🔹 Helper: Print themed or random cat
def show_cat(message=None, mood=None):
    if mood and mood in CAT_ART:
        cat = CAT_ART[mood]
    else:
        cat = random.choice(CATS)
    console.print(f"[bold cyan]{cat}[/bold cyan]")
    if message:
        console.print(f"[italic yellow]{message}[/italic yellow]")

# 🐾 CLI Group
@click.group()
def cli():
    pass

# --------------------
# 🐱 Basic Commands
# --------------------

@cli.command()
def sniff():
    """Sniff around (like ls)."""
    files = os.listdir()
    show_cat("I sniffed these files:", mood="sniff")
    for f in files:
        console.print(f"🐾 {f}")

@cli.command()
@click.argument('folder')
def slink(folder):
    """Slink into a folder (like cd)."""
    try:
        os.chdir(folder)
        show_cat(f"Slinked into {folder} 🐈", mood="slink")
    except FileNotFoundError:
        show_cat(f"[red]That path smells wrong...[/red]")

@cli.command()
@click.argument('name')
def nest(name):
    """Build a new nest (like mkdir)."""
    try:
        os.mkdir(name)
        show_cat(f"Built a cozy nest: {name} 🧶", mood="nest")
    except FileExistsError:
        show_cat(f"[red]That nest already exists![/red]")

@cli.command()
def nap():
    """Take a catnap (exit)."""
    show_cat("Time for a nap... 💤", mood="nap")
    exit()

@cli.command()
def chaos():
    """Enter chaos mode (experimental)."""
    show_cat("CATS EVERYWHERE!!!", mood="chaos")
    for _ in range(10):
        console.print(random.choice(CATS), style=random.choice(["red", "blue", "green", "yellow"]))

@cli.command()
@click.argument('message', required=False)
def yowl(message="I HAVE OPINIONS!"):
    """Yell like an angry cat (like echo)."""
    show_cat(mood="yowl")
    console.print(f"😾 YOWL: [bold red]{message.upper()}!!![/bold red]")

@cli.command()
@click.argument('filename')
def judge(filename):
    """Judge a file based on its name. Emotionally."""
    sass = [
        "Ugh. Boring filename.",
        "Meh, seen better.",
        "This smells suspicious...",
        "Delicious name. I’d sleep on it.",
        "Too many underscores. Ew.",
        "Purrfection. Absolute masterpiece."
    ]
    show_cat(mood="judge")
    console.print(f"📂 {filename}: [bold magenta]{random.choice(sass)}[/bold magenta]")

@cli.command()
def summon():
    """Summon a flood of cats."""
    for _ in range(5):
        show_cat("You summoned a feline force!", mood="summon")

@cli.command()
@click.argument("file")
def pawpoke(file):
    """Touches a file, but in a cute way."""
    pathlib.Path(file).touch()
    show_cat(f"Pawpoked {file} 🐾", mood="pawpoke")

# 🔹 Entry Point
if __name__ == "__main__":
    cli()

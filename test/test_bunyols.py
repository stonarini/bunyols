import pytest
from src.bunyols import bunyols

items = [
    (
        "https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/",
        (None, ["IT"]),
    ),
    (
        "https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882",
        ("Robert C Martin Series", ["IT"]),
    ),
    (
        "https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052/",
        (None, ["IT"]),
    ),
    (
        "https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164",
        ("Robert C Martin Series", ["IT"]),
    ),
    (
        "https://www.amazon.com/Clean-Coder-Conduct-Professional-Programmers/dp/0137081073/",
        ("Robert C Martin Series", ["IT"]),
    ),
    (
        "https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/",
        (None, ["IT"]),
    ),
    (
        "https://www.amazon.com/SSH-Mastery-OpenSSH-PuTTY-Tunnels/dp/1642350028/",
        (None, ["IT", "Comedy"]),
    ),
    (
        "https://www.amazon.com/Mushroom-Botanical-Art-Toshimitsu-Fukiharu/dp/4756254756/",
        (None, ["Art"]),
    ),
    (
        "https://www.amazon.com/Art-That-Changed-World-Transformative/dp/1465414355/",
        (None, ["Art", "History"]),
    ),
    (
        "https://www.amazon.com/Daily-Drawing-Prompts-Sketchbook-Inspiration/dp/1648764843/",
        (None, ["Drawing"]),
    ),
    (
        "https://www.amazon.com/Complete-Book-Drawing-Essential-Skills/dp/1848375360/",
        (None, ["Drawing"]),
    ),
    (
        "https://www.amazon.com/Library-Fragile-History-Andrew-Pettegree/dp/1541600770/",
        (None, ["History"]),
    ),
    (
        "https://www.amazon.com/Season-Storms-Witcher-Andrzej-Sapkowski/dp/0316441635/",
        ("The Witcher", ["Sci-Fi", "Fantasy"]),
    ),
    (
        "https://www.amazon.com/Sword-Destiny-Witcher-Andrzej-Sapkowski/dp/0316389706/",
        ("The Witcher", ["Sci-Fi", "Fantasy"]),
    ),
    (
        "https://www.amazon.com/Harry-Potter-Sorcerers-Stone-Rowling/dp/0590353403/",
        ("Harry Potter", ["Fantasy"]),
    ),
    (
        "https://www.amazon.com/Harry-Potter-Chamber-Secrets-Rowling/dp/0439064864/",
        ("Harry Potter", ["Fantasy"]),
    ),
    (
        "https://www.amazon.com/Harry-Potter-Goblet-Fire-Book/dp/0439139597/",
        ("Harry Potter", ["Fantasy"]),
    ),
    (
        "https://www.amazon.com/Maigret-Gehängte-von-Saint-Pholien/dp/3257208162/",
        (None, ["Crime"]),
    ),
    (
        "https://www.amazon.com/Tucci-Table-Cooking-Family-Friends/dp/1476738564/",
        (None, ["Cooking"]),
    ),
    (
        "https://www.amazon.com/Hollywood-Genres-Post-war-America-Masculinity/dp/1850438153/",
        (None, ["Noir", "History"]),
    ),
    (
        "https://www.amazon.com/Street-No-Name-History-American/dp/0813122430/",
        (None, ["Noir"]),
    ),
    (
        "https://www.amazon.com/Chronicles-Narnia-C-S-Lewis/dp/0060765453",
        ("Narnia", ["Fantasy"]),
    ),
    (
        "https://www.amazon.com/Introducing-Python-Modern-Computing-Packages/dp/1492051365/",
        ("O'Reilly", ["Python"]),
    ),
    (
        "https://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730/",
        ("O'Reilly", ["Python"]),
    ),
    (
        "https://www.amazon.com/Book-about-Monty-Python-Grail-dp-1538134438/dp/1538134438/",
        (None, ["Python"]),
    ),
    (
        "https://www.amazon.com/Learning-Vim-Editors-Processing-Maximum/dp/059652983X/",
        ("O'Reilly", ["IT"]),
    ),
    (
        "https://www.amazon.com/Version-Control-Git-collaborative-development/dp/1449316387/",
        ("O'Reilly", ["IT"]),
    ),
    (
        "https://www.amazon.com/Classical-Music-World-Crystal-Kirgiss/dp/1583400192/",
        (None, ["Music"]),
    ),
    (
        "https://www.amazon.com/Monks-Music-Thelonious-History-Making/dp/0520252012/",
        (None, ["Music"]),
    ),
    (
        "https://www.amazon.com/Chestnut-Cook-Book-Practical-Information/dp/1587361671/",
        (None, ["Cooking"]),
    ),
    (
        "https://www.amazon.com/Pumpkin-Cookbook-2nd-Celebrating-Versatility/dp/1612128335/",
        (None, ["Cooking"]),
    ),
    ("https://www.amazon.com/The-Beatles-Get-Back/dp/0935112960/", (None, ["Music"])),
    (
        "https://www.amazon.com/Music-History-Questlove/dp/1419751433/",
        (None, ["Music"]),
    ),
    ("https://www.amazon.com/-/Aldous-Huxley/dp/0060850523/", (None, ["Fantasy"])),
]

more_items = []


def test_bunyols():
    for item in more_items:
        bunyols(item)

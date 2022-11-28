# """Same as the table_movie.py but uses Live to update"""
# import time
# from contextlib import contextmanager
#
# from rich import box
# from rich.align import Align
# from rich.columns import Columns
# from rich.console import Console
# from rich.live import Live
# from rich.panel import Panel
# from rich.table import Table
# from rich.text import Text
# from rich.tree import Tree
#
# console = Console(record=True)
#
# BEAT_TIME = 0.04
#
#
# @contextmanager
# def beat(length: int = 1) -> None:
#     yield
#     time.sleep(length * BEAT_TIME)
#
#
# table = Table(show_footer=False)
# table_centered = Align.center(table)
#
# console.clear()
#
# with Live(table_centered, console=console, screen=False, refresh_per_second=20):
#     # pass
#     with beat(10):
#         title = Text.from_markup(
#             "[b blue]Sundara Nataraja  \n [b white]Lead Backend Developer",
#             justify="center",
#         )
#         description = Text.from_markup(
#             """\n\nI am a strong believer of "I Can is greater than IQ". I have architected and developed multiple python
# based web tools and standalone tools. Always being first to initiate and innovate is my strongest
# strength. Having strong critical and analytical thinking along with strong technical skills enabled me to be
# top at what I do.""",
#             justify="center",
#         )
#         table.add_column(title + description)
#         table.width = console.width
#     with beat(10):
#         contacts = Table(show_footer=False)
#         table.add_row(contacts)
#         contacts.width = console.measure(table).maximum - 10
#         contacts.box = None
#         contacts.add_column(" ")
#         contacts.add_column(" ")
#         contacts.add_column(" ")
#         contacts.add_column("linkedin.com/in/sundara-nataraja-amancharla-15b85965")
#         contacts.add_column(":link: ")
#         contacts.box = box.SIMPLE_HEAD
#     with beat(10):
#         skills = Table(show_footer=False)
#         table.add_row(skills)
#         skills.box = box.SIMPLE_HEAD
#         skills.width = console.measure(table).maximum - 10
#         skills.add_column("Programming Skills")
#         skill = "[black on white] + ".join(["Python", "FastAPI", "SqlAlchemy"])
#         skills.add_row(skill)
#         skills.add_row(skill)
#
#     with beat(10):
#         expereinces = Table(show_footer=False)
#         expereinces.box = box.SIMPLE_HEAD
#         expereinces.add_column("Experiences")
#         expereince = Tree("[b]Aspaara AG")
#         expereince.add("foo")
#         expereince.add("bar")
#         expereinces.add_row(expereince)
#         expereince = Tree(
#             "[b]Technical Architect & Product Owner \t\t 01/2018 - Present,"
#         )
#         expereince.add("Continental Automotive")
#         expereince.add(
#             "Technologies : Python, Django, Django Restframework, Tensorflow, Angular, Jenkins, MongoDB, "
#             "MySql, Docker,AWS,Oracle"
#         )
#         expereince.add(
#             "Create and Design Web Tools from scratch and create a technical stack for the project. Translate design "
#             "into the requirements."
#         )
#         expereince.add(
#             "Product Owner for Multiple projects from creating vision and translating same to work-packages and bring "
#             "the project to closure."
#         )
#         expereince.add(
#             "Leading and Managing 10+ colleagues last 3 years that involves recruiting, training ,provide constant feedback and appraisal of thecolleagues."
#         )
#         expereince.add(
#             "Being SPOC for the tools developed and talking to German Counterparts and understand the business requirement, Communicating the status, Demonstrating the tool and collecting feedback."
#         )
#         expereince.add(
#             "Responsible for talking to various counterparts, understand requirements and propose a solution that fits the vision and goals of the organization"
#         )
#         expereince.add("")
#         expereince.add("")
#         expereince.add("")
#         expereince.add("")
#         expereince.add("")
#
#         expereinces.add_row(expereince)
#
#     with beat(10):
#         most_proud_of = Table(show_footer=False)
#         most_proud_of.add_column("Most Proud of")
#         most_proud_of.box = box.SIMPLE_HEAD
#         most_proud_of.add_row()
#         user_renderables = [
#             Panel(
#                 user,
#                 expand=True,
#                 width=int((console.measure(table).maximum - 10) / 2),
#                 box=box.SIMPLE_HEAD,
#             )
#             for user in [expereinces, most_proud_of]
#         ]
#         col = Columns(user_renderables)
#         table.add_row(col)
#     with beat(10):
#         skills = Table(show_footer=False)
#         table.add_row(skills)
#         skills.box = box.SIMPLE_HEAD
#         skills.width = console.measure(table).maximum - 10
#         skills.add_column("Education")
#         skill = "[black on white] + ".join(["Python", "FastAPI", "SqlAlchemy"])
#         skills.add_row(skill)
#         skills.add_row(skill)
#     with beat(10):
#         skills = Table(show_footer=False)
#         table.add_row(skills)
#         skills.box = box.SIMPLE_HEAD
#         skills.width = console.measure(table).maximum - 10
#         skills.add_column("Interests")
#         skill = "[black on white] + ".join(["Python", "FastAPI", "SqlAlchemy"])
#         skills.add_row(skill)
#         skills.add_row(skill)
#
#     #
#     # with beat(10):
#     #     table.add_column("Title", Text.from_markup("[b]Total", justify="right"))
#     #
#     # with beat(10):
#     #     table.add_column("Budget", "[u]$412,000,000", no_wrap=True)
#     #
#     # with beat(10):
#     #     table.add_column("Opening Weekend", "[u]$577,703,455", no_wrap=True)
#     #
#     # with beat(10):
#     #     table.add_column("Box Office", "[u]$4,331,212,357", no_wrap=True)
#     #
#     # with beat(10):
#     #     table.title = "Sundara Nataraja Amancharla"
#     #
#     # with beat(10):
#     #     table.title = (
#     #         "[not italic]:snake:[/] [bold]Sundara Nataraja [b magenta not dim] Amancharla[/][/] [not italic]:snake:[/]"
#     #     )
#     #
#     #
#     with beat(10):
#     #
#     # for row in TABLE_DATA:
#     #     with beat(10):
#     #         table.add_row(*row)
#     #
#     # with beat(10):
#     #     table.show_footer = True
#     #
#     # table_width = console.measure(table).maximum
#     #
#     # with beat(10):
#     #     table.columns[2].justify = "right"
#     #
#     # with beat(10):
#     #     table.columns[3].justify = "right"
#     #
#     # with beat(10):
#     #     table.columns[4].justify = "right"
#     #
#     # with beat(10):
#     #     table.columns[2].header_style = "bold red"
#     #
#     # with beat(10):
#     #     table.columns[3].header_style = "bold green"
#     #
#     # with beat(10):
#     #     table.columns[4].header_style = "bold blue"
#     #
#     # with beat(10):
#     #     table.columns[2].style = "red"
#     #
#     # with beat(10):
#     #     table.columns[3].style = "green"
#     #
#     # with beat(10):
#     #     table.columns[4].style = "blue"
#     #
#     # with beat(10):
#     #     table.columns[0].style = "cyan"
#     #     table.columns[0].header_style = "bold cyan"
#     #
#     # with beat(10):
#     #     table.columns[1].style = "magenta"
#     #     table.columns[1].header_style = "bold magenta"
#     #
#     # with beat(10):
#     #     table.columns[2].footer_style = "bright_red"
#     #
#     # with beat(10):
#     #     table.columns[3].footer_style = "bright_green"
#     #
#     # with beat(10):
#     #     table.columns[4].footer_style = "bright_blue"
#     #
#     # with beat(10):
#     #     table.row_styles = ["none", "dim"]
#     #
#     # with beat(10):
#     #     table.border_style = "bright_yellow"
#     #
#     # for box_style in [
#     #     box.SQUARE,
#     #     box.MINIMAL,
#     #     box.SIMPLE,
#     #     box.SIMPLE_HEAD,
#     # ]:
#     #     with beat(10):
#     #         table.box = box_style
#     #
#     # with beat(10):
#     #     table.pad_edge = False
#     #
#     # original_width = console.measure(table).maximum
#     #
#     # for width in range(original_width, console.width, 2):
#     #     with beat(1):
#     #         table.width = width
#     #
#     # for width in range(console.width, original_width, -2):
#     #     with beat(1):
#     #         table.width = width
#     #
#     # for width in range(original_width, 90, -2):
#     #     with beat(1):
#     #         table.width = width
#     #
#     # for width in range(90, original_width + 1, 2):
#     #     with beat(1):
#     #         table.width = width
#     #
#     # with beat(2):
#     #     table.width = None
#
# CONSOLE_HTML_FORMAT = """\
# <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
# """
#
# console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
#
# """
#
#
#
# Design and Architect for Project "Versatile" which is automation of Validation and testing process of ADAS Sensors and has saved
# around 7 man year of Effort helped organization to manage workload from various customers during the pandamic
# Created and developed a Data management system for the organization that includes Managing 100+PB of Data and various workflows
# inside it.
# Architected and developed a Labeling Management system, that is the amalgamation of multiple tools and process using the concept
# of Microservices that could manage intense data from labelling activities and data transfers.
# """

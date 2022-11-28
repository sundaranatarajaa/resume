import json
import os
import typing
from typing import Dict

from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

from .schema import Details
from .schema import Education
from .schema import Experience
from .schema import ProgrammingStack

NAME_MAP_EMOJI = {
    "email": ":mailbox_with_no_mail: ",
    "location": ":earth_asia: ",
    "phone_num": ":mobile_phone: ",
    "link": ":link: ",
    "nationality": ":flag_for_india: ",
}


class ResumeBuilder:
    def __init__(self, console: Console):
        self.table = Table(show_footer=False)
        self.console = console
        self.table.width = self.console.width

    def __generate_table(self):
        table = Table(show_footer=False)
        table.box = box.SIMPLE_HEAD
        table.width = self.console.measure(self.table).maximum - 10
        return table

    def create_resume(
            self,
            details: typing.Dict,
    ):
        details = Details(**details)
        self._create_title(details.title, details.role)
        self._create_about(details.about)
        self._create_info(details.info)
        self._create_programming_stack(details.programming_stacks)
        self._create_work_experience(details.experiences)
        self._create_education(details.education)
        self._create_interests(details.interests)
        self._create_footer()

        self.console.print(self.table)
        CONSOLE_HTML_FORMAT = """\
        # <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
        # """
        from rich.terminal_theme import DEFAULT_TERMINAL_THEME

        # self.console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
        self.console.save_svg("resume.svg", title="sundara_nataraja.py", theme=DEFAULT_TERMINAL_THEME)

    def _create_title(self, title, role):
        title = Text.from_markup(
            f"[b blue]{title} \n [b black]{role}",
            justify="center",
        )
        self.table.add_column(title)

    def _create_about(self, about):
        description = Text.from_markup(
            f"{about}",
            justify="center",
        )
        self.table.add_row(description)

    def _create_programming_stack(self, prog_stack: ProgrammingStack):

        skills = self.__generate_table()
        self.table.add_row(skills)
        skills.add_column("Programming Skills")
        current_stack = "Current stack : "
        for skill in prog_stack.current_stack:
            current_stack += f"[black on white] {skill} [/] "
        skills.add_row(current_stack)
        skills.add_row("")

        for inx, prev_stack in enumerate(prog_stack.previous_stacks):
            previous_stack = f"Previous stack {inx + 1}: "
            for skill in prev_stack:
                previous_stack += f"[black on white] {skill} [/] "
            skills.add_row(previous_stack)
            skills.add_row()

    def _create_education(self, education: typing.List[Education]):
        interest_table = self.__generate_table()
        interest_table.add_column("Education")
        interest_str = ''
        for university in education:
            interest_str += f"[black on white] {university.degree:50s}[/] " \
                            f"[b black] {university.university:50s} [/]" \
                            f"[b black] {university.serving_period.end_date} - {university.serving_period.start_date} [/]  "

        interest_table.add_row(interest_str)
        self.table.add_row(interest_table)

    def _create_interests(self, interests: typing.List):
        interest_table = self.__generate_table()
        interest_table.add_column("Interests")
        interest_str = ''
        for interest in interests:
            interest_str += f"[black on white] {interest} [/] "

        interest_table.add_row(interest_str)
        self.table.add_row(interest_table)

    def _create_work_experience(self, experiences: typing.List[Experience]):
        experiences_table = self.__generate_table()
        experiences_table.add_column("Experiences")
        for expereince in experiences:
            end_date = expereince.serving_period.end_date
            expereince_title = f"[b black on white] {expereince.company:100s}[/]\t " \
                               f"[b black]{end_date if end_date else 'Present'} -" \
                               f" {expereince.serving_period.start_date} "
            exp_tree = Tree(expereince_title)
            role_title = ' <- '.join(expereince.roles)
            exp_tree.add(role_title)
            tasks_title = Tree("Main Responsibilities")
            exp_tree.add(tasks_title)
            for task in expereince.tasks:
                tasks_title.add(task)
            if len(expereince.most_proud_of) > 0:
                mpo_title = Tree("Most Proud Of")
                exp_tree.add(mpo_title)
                for mpo in expereince.most_proud_of:
                    mpo_title.add(mpo)
            experiences_table.add_row(exp_tree)
            experiences_table.add_row()

        self.table.add_row(experiences_table)

    def _create_footer(self):
        self.table.caption = Text.from_markup(
            f"[b black] Made programmatically using [magenta]rich[/]."
            " To know more please visit:"
            "[blue]github.com/sundaranatarajaa/resume ",
            justify="center",
        )

    def _create_info(self, info: dict):
        contacts = self.__generate_table()
        for detail in info:
            if detail == "links":
                for link in info[detail]:
                    contacts.add_column(f"{NAME_MAP_EMOJI['link']}{info[detail][link]}")
            else:
                contacts.add_column(
                    f"{NAME_MAP_EMOJI.setdefault(detail, '')} {info[detail]}"
                )

        self.table.add_row(contacts)

import typing
from datetime import date

from pydantic import BaseModel


class Period(BaseModel):
    start_date: date
    end_date: typing.Optional[date]

class Education(BaseModel):
    degree: str
    university: str
    serving_period: Period



class Experience(BaseModel):
    company: str
    roles: typing.List
    serving_period: Period
    tasks: typing.List
    most_proud_of: typing.List


class ProgrammingStack(BaseModel):
    current_stack: typing.List
    previous_stacks: typing.Optional[typing.List[typing.List]]


class Details(BaseModel):
    title: str
    role: str
    about: str
    motto: str
    info: typing.Dict
    programming_stacks: ProgrammingStack
    experiences: typing.List[Experience]
    education: typing.List[Education]
    certificates: typing.List
    interests: typing.List

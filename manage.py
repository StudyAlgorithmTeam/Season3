from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from functools import cache
from typing import List

# external modules (pip install pyyaml requests)
from yaml import load, FullLoader
import requests



@cache
def request_json(url: str) -> dict:
    return requests.get(url).json()


class Color(Enum):
    SOLVED = '#a1e4ac'
    UNSOLVED = '#dddfe0'
    TEXT = '#8a8f95'


@dataclass
class Activity:
    name: str
    problem_id_list: List[int]


@dataclass
class Problem:
    problem_id: int
    title: str = ''
    level: int = 0
    is_solved: bool = False

    @classmethod
    def from_json(self, data: dict):
        return Problem(
            problem_id=int(data.get('problemId')),
            title=data.get('titleKo'),
            level=int(data.get('level')),
            is_solved=True
        )


@dataclass
class User:
    handle: str
    problems: List[Problem] = field(default_factory=list)

    def add_problems(self, *problem_id: int):
        query = '+%7C+'.join(f'id:{id}' for id in problem_id)
        query += f'+%40{self.handle}'
        data = request_json(f' https://solved.ac/api/v3/search/problem?query={query}')
        self.problems = [Problem.from_json(item) for item in data['items']]

    def did_solve(self, problem_id: int) -> bool:
        for problem in self.problems:
            if problem.problem_id == problem_id:
                return problem.is_solved
        return False


@dataclass
class Study:
    users: List[User]
    activities: List[Activity]

    def create_svg(self) -> str:
        problem_id_list = self._problem_id_list()

        HANDLE_WIDTH = 160

        CELL_WIDTH = 20
        CELL_HEIGHT = 20

        SVG_WIDTH = HANDLE_WIDTH + (len(problem_id_list)+len(self.activities)) * CELL_WIDTH
        SVG_HEIGHT = 192

        for user in self.users:
            user.add_problems(*problem_id_list)

        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" style="direction: ltr; height: {SVG_HEIGHT}px; width: {SVG_WIDTH}px; display: block; margin: 0px auto;">'
        for y, user in enumerate(self.users):
            text_x = 8
            text_y = CELL_HEIGHT*y + 10
            text_hex_color = Color.TEXT.value
            svg += f'<text font-size="13" text-anchor="left" x="{text_x}" y="{text_y}" dy="0.3em" fill="{text_hex_color}">{user.handle}</text>'
        x = 0
        for activity in self.activities:
            for problem_id in activity.problem_id_list:
                for y, user in enumerate(self.users):
                    cell_x = CELL_WIDTH * x + HANDLE_WIDTH
                    cell_y = CELL_HEIGHT * y
                    cell_hex_color = Color.UNSOLVED.value
                    if user.did_solve(problem_id):
                        cell_hex_color = Color.SOLVED.value
                    svg += f'<rect width="{CELL_WIDTH-2}" height="{CELL_HEIGHT-2}" x="{cell_x}" y="{cell_y}" rx="5" fill="{cell_hex_color}" stroke-width="2.5"/>'
                text_x = CELL_WIDTH * x + HANDLE_WIDTH + 8
                text_y = CELL_HEIGHT * len(self.users) + 8
                text_rotate = 45
                text_hex_color = Color.TEXT.value
                svg += f'<text font-size="13" text-anchor="left" dy="0.3em" fill="{text_hex_color}" transform="translate({text_x}, {text_y}) rotate({text_rotate})">{problem_id}</text>'
                x += 1
            x += 1
        svg += '</svg>'
        return svg

    def _create_element(tag_name: str, attrs: dict = {}, *children: str) -> str:
        return f'<{tag_name} '+' '.join(f'{key}="{val}"' for key, val in attrs.items())+'>'+''.join(children)+f'</{tag_name}>'

    def _problem_id_list(self) -> List[int]:
        problem_id_list = []
        for activity in self.activities:
            problem_id_list.extend(activity.problem_id_list)
        return problem_id_list


if __name__ == '__main__':
    users = []
    activities = []

    with open("info.yml", "r") as f:
        data = load(f, FullLoader)
        for name, problem_id_list in data['activities'].items():
            activities.append(Activity(name, problem_id_list))
        for handle in data['handles']:
            users.append(User(handle))

    study = Study(users, activities)

    with open('streak.svg', 'w') as f:
        f.write(study.create_svg())

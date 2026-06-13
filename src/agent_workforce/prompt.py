from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def load_prompt(path: Path, **variables) -> str:
    env = Environment(loader=FileSystemLoader(str(path.parent)))
    template = env.get_template(path.name)
    return template.render(**variables)

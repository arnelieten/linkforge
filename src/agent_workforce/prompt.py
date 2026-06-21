import random

from jinja2 import Environment, PackageLoader


class PromptLoader:
    def __init__(self, agent: str):
        self._agent = agent

    @staticmethod
    def _load_prompt_plugins(plugin_name: str) -> str:
        plugin_env = Environment(
            loader=PackageLoader("agent_workforce", "prompt_plugins")
        )
        return plugin_env.get_template(f"{plugin_name}.jinja2").render()

    @staticmethod
    def _sample_example(example_count: int):
        numbers = random.sample(range(1, 11), example_count)
        return [f"example_{number}" for number in numbers]

    def _load_prompt(
        self, plugins: list[str] | None = None, example_count: int = 0
    ) -> str:
        prompt_env = Environment(loader=PackageLoader("agent_workforce", self._agent))
        template = prompt_env.get_template("prompt.jinja2")
        if plugins is None:
            plugins = []

        agent_plugins = {
            plugin: self._load_prompt_plugins(plugin) for plugin in plugins
        }

        agent_examples = {
            example: self._load_prompt_plugins(example)
            for example in self._sample_example(example_count=example_count)
        }
        return template.render(**agent_plugins, **agent_examples)

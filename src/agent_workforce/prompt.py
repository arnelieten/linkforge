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

    def _load_prompt(self, plugins: list[str]) -> str:
        prompt_env = Environment(loader=PackageLoader("agent_workforce", self._agent))
        template = prompt_env.get_template("prompt.jinja2")
        agent_plugins = {
            plugin: self._load_prompt_plugins(plugin) for plugin in plugins
        }
        return template.render(**agent_plugins)

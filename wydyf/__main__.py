import click

from .feedback import main as feedback
from .hours import main as hours


@click.group(name="wydyf", context_settings={"show_default": True})
def main() -> None:
    pass


main.add_command(cmd=feedback)
main.add_command(cmd=hours)


if __name__ == "__main__":
    main()

"""
    python example_dynaconf_2.py --env=prd
"""

import argparse

from dynaconf import Dynaconf


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="ver")
    known_args, _ = parser.parse_known_args()
    print(known_args.env)

    config_path = f"config/{known_args.env}"
    settings = Dynaconf(
        envvar_prefix="DYNACONF",
        settings_files=[
            f"{config_path}/settings.toml",
            f"{config_path}/.secrets.toml",
        ],
    )

    print(settings.database.name)
    print(settings.PORT)
    print(settings.port)

    print(settings.port)

    print(settings.servers.beta)
    print(settings.servers.alpha)

    print(settings.password)


if __name__ == "__main__":
    main()

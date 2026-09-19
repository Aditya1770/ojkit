from pathlib import Path
from platformdirs import user_config_dir

CONFIG_DIR = Path(user_config_dir("ojkit"))
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_FOLDER = "~/codeforces/"


def getFolder():
    if not CONFIG_FILE.exists():
        return Path(DEFAULT_FOLDER).expanduser()
    
    for line in CONFIG_FILE.read_text().splitlines():
        if line.startswith("problem_folder"):
            folder = line.split("=", 1)[1].strip().strip('"')
            return Path(folder).expanduser()

    return Path(DEFAULT_FOLDER).expanduser()

def setFolder(folder):
    folder = Path(folder).expanduser()

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    CONFIG_FILE.write_text(f'problem_folder="{folder}"\n')

    return folder

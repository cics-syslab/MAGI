import shutil

from functions.session import update_pages
from magi.utils import file_utils


def reset_pages():
    from magi.managers import InfoManager
    pages_dir = InfoManager.Directories.SRC_PATH / "webui" / "pages"
    # remove all files in pages directory
    file_utils.reset_dir(pages_dir)
    template_dir = InfoManager.Directories.SRC_PATH / "webui" / "templates"
    for file in template_dir.iterdir():
        if file.is_file() and file.suffix == ".py":
            shutil.copy(file, pages_dir)
    update_pages(use_session_state=False)


if __name__ == "__main__":
    reset_pages()

"""Auto update all albert extensions"""
import os

from albert import *

__iid__ = "PythonInterface/v0.4"
__title__ = "Autoupdate"
__prettyname__ = "Autoupdate"
__version__ = "0.4.1"
__triggers__ = "up "
__authors__ = "Bharat Kalluri"
__dependencies__ = []


def auto_update():
    os.system(
        """cd ~/.local/share/albert/org.albert.extension.python/modules && 
    find . -maxdepth 1 -type d \\( ! -name . \\) -exec bash -c "cd '{}' && pwd && git pull --all" \\;"""
    )


def handleQuery(query):
    if query.isTriggered:
        return Item(
            id=__prettyname__,
            text="All extensions will be updated on enter",
            subtext="It will take some time, wait till albert disappears. Check the logs for info.",
            actions=[FuncAction(text="Save token", callable=lambda: auto_update())],
        )

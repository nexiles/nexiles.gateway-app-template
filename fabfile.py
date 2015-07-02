import os

import webbrowser

from fabric.api import task
from fabric.api import execute
from fabric.api import local, lcd
from fabric.context_managers import settings
from fabric.context_managers import hide

from fabric.colors import red, green, yellow


os.environ["SENCHA_VERSION"] = "6.0.0.202"

APP_NAME = "AppTemplate"

project_root    = os.path.dirname(__file__)

docs_dir        = os.path.join(project_root, "docs")
build_dir       = os.path.join(project_root, "build")
static_dir      = os.path.join(project_root, "static")
src_dir         = os.path.join(project_root, "src")

######################################################################
# Package Maintainer Tasks
######################################################################


@task
def release_docs():
    "builds the documentation and pushes it to GitHub"
    execute(build_docs)
    print(green("Pushing to GitHub ..."))
    with settings(hide("stdout", "running")):
        with lcd(docs_dir):
            local("make gh_pages")
            local("make gh_pages_sync")


######################################################################
# Developer Tasks
######################################################################


@task
def init():
    "Initialize freshly checked-out repo"
    print(green("Initializing repo"))
    with settings(hide("stdout", "running")):
        with lcd(project_root):
            print(green("    Installing node modules ..."))
            local("npm install")

            print(green("    Compiling coffee scripts ..."))
            local("grunt coffee")

            print(green("    Initializing sencha framework ..."))
            local("sencha generate app -ext {} static".format(APP_NAME))

        with lcd(static_dir):
            print(green("    Building application ..."))
            local("sencha app build".format(APP_NAME))

@task(default=True)
def full_monty():
    "Do a full rebuild-package cycle"
    execute(build)
    execute(package)
    execute(build_docs)


@task
def build(which="production"):
    "builds the app"
    print(green("Building for {}".format(which)))
    with settings(hide("stdout", "running")):
        with lcd(project_root):
            print(green("   installing node modules ..."))
            local("npm install")
            print(green("   compiling CoffeScript ..."))
            local("grunt coffee")
        with lcd(static_dir):
            print(green("   building app ..."))
            local("sencha app build {}".format(which))


@task
def package(which="production"):
    "package the app"
    print(green("Packaging app ({})".format(which)))

    app_package = "{}/{}-{}.zip .".format(build_dir, APP_NAME, which)

    with settings(hide("stdout", "running")):
        local("mkdir -p {}".format(build_dir))
        with lcd(os.path.join(static_dir, "build", which, APP_NAME)):
            local("zip -r {} .".format(app_package))

    print(green("Built package: ") + yellow(app_package))


@task
def build_docs():
    "builds the documentation"
    print(green("Building documentation"))
    with settings(hide("stdout", "running")):
        with lcd(docs_dir):
            local("make html")


@task
def docs():
    "Show docs"
    execute(build_docs)
    url = "file://{}".format(
        os.path.abspath(
            os.path.join(docs_dir, "_build", "html", "index.html")))

    webbrowser.open(url)

# EOF

import os
import json

import webbrowser
# import socketserver
# import SimpleHTTPServer

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

ext_sdk_dir     = os.path.expanduser("~/develop/js/Sencha/ext-6.0.0")
if not os.path.exists(ext_sdk_dir):
    # Will use trial version.
    ext_sdk_dir = None


APP_VERSION = json.loads(open(
    os.path.join(static_dir, "resources", "version.json"), "r").read())


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
# Windchill App Template Building
######################################################################

@task
def build_app_template():
    "build the windchill app template package"

    # So the production build ran through, and we need to manually
    # assemble the app template build because sencha command does not
    # support non-microloader builds.

    dest_dir = os.path.join(static_dir, "build", "windchill", APP_NAME, "static")
    local("mkdir -p {}".format(dest_dir))

    with lcd(dest_dir):
        # copy built app sources (actually this is done by grunt also)
        local("cp -r {}/* .".format(static_dir))

        app_meta = {
            "version":      "{version}".format(**APP_VERSION),
            "thumbnail":    "resources/img/ilogo.png",
            "app-url":      "index.html",
            "name":         APP_NAME,
            "description":  APP_NAME
        }
        with open(os.path.join(dest_dir, "app-meta.json"), "w") as appmeta:
            appmeta.write(json.dumps(app_meta, indent=4))


@task
def iterate_template_app():
    execute(build_app_template)
    app_dir = os.path.join(static_dir, "build", "windchill", APP_NAME)
    with lcd(app_dir):
        local("nxtools app-pack   --name template")
        local("nxtools app-upload --name template")

@task
def full_monty_template():
    execute(build, which="windchill")
    execute(iterate_template_app)

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
            if ext_sdk_dir:
                local("sencha -sdk {} generate app -ext -classic {} static".format(
                    ext_sdk_dir, APP_NAME))
            else:
                print(yellow("    SDK directory not configured, "
                             "using TRIAL VERSION of ExtJS"))
                local("sencha generate app -ext -classic {} static".format(APP_NAME))

        with lcd(static_dir):
            print(green("    Building application ..."))
            local("sencha app build".format(APP_NAME))


# @task
# def serve(port=8000, production=False):
#     "Serves the app locally for testing"
#     Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#     httpd = SocketServer.TCPServer(("", port), Handler)
#     webbrowser.open("http://localhost:{}".format(port))
#     if not production:
#         print(green("Serving DEVELOPMENT on http://localhost:{}".format(port)))
#         os.chdir(static_dir)
#     else:
#         print(green("Serving PRODUCTION on http://localhost:{}".format(port)))
#         os.chdir(os.path.join(static_dir, "build", "production", APP_NAME))
#     httpd.serve_forever()


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
            local("grunt copy")

        # if the build type is "windchill", we do a production build and
        # delegate to a special windchill build task
        windchill_build = False
        if which == "windchill":
            which = "production"
            windchill_build = True

        with lcd(static_dir):
            print(green("   building app ..."))
            local("sencha app build {}".format(which))

        if windchill_build:
            execute(build_app_template)

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

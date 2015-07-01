# node requirements
path = require "path"
fs   = require "fs"
cp   = require "child_process"
async = require "async"

# meta informations
application_name = "AppTemplate"

# ExtJS location, Ext.Router location, sencha CMD version
sencha_base = path.resolve "../../js/Sencha"
process.env.SENCHA_VERSION="5.1.3.61"


module.exports = (grunt) ->
    # Do grunt-related things in here

    grunt.initConfig
        pkg: grunt.file.readJSON("package.json")

        # config
        cfg:
            version_file: "static/resources/version.json"

        # watch files
        watch:
            options:
                livereload: yes
            app:
                files: [
                    "src/#{application_name}/app.coffee",
                    "src/#{application_name}/app/**/*"
                    "static/index.html"
                ]
                tasks: [
                    "coffee"
                    "bump_version"
                ]

        # coffee compile task
        coffee:
            app:
                options:           # coffee compile options
                    sourceMap: yes
                expand: yes        # use dynamic glob patterns when expanding src
                cwd:  "src/#{application_name}"  # all src paths are relative to here
                src:  [ "*.coffee","**/*.coffee" ]
                dest: "static"
                ext: ".js"


    grunt.loadNpmTasks "grunt-node-webkit-builder"
    grunt.loadNpmTasks "grunt-contrib-coffee"
    grunt.loadNpmTasks "grunt-contrib-watch"
    grunt.loadNpmTasks "grunt-contrib-uglify"
    grunt.loadNpmTasks "grunt-contrib-copy"
    grunt.loadNpmTasks "grunt-notify"

    grunt.registerTask "default", ["watch"]
    grunt.registerTask "build",   ["coffee", "sencha"]

    grunt.registerTask "version", "show the web app version", ->
        version_file = grunt.config.get "cfg.version_file"
        version = JSON.parse fs.readFileSync version_file
        grunt.log.write "#{version.name} v#{version.version} - build #{version.build} - date #{version.date}"

    grunt.registerTask "bump_version", "bump the web app version", ->
        grunt.log.write "bumping version ...."
        version_file = grunt.config.get "cfg.version_file"
        version = JSON.parse fs.readFileSync version_file
        version.build += 1
        d = new Date()
        version.date = "#{d.getFullYear()}-#{d.getMonth()+1}-#{d.getDate()}"
        fs.writeFileSync version_file, JSON.stringify version
        grunt.log.write "#{version.name} v#{version.version} - build #{version.build} - date #{version.date}"

    grunt.registerTask "sencha", "build the application with 'sencha cmd'", ->
        done = @async()
        cmd = cp.exec "sencha app build", {cwd: "static"}
        cmd.stdout.on "data", (data) ->
            grunt.log.write "stdout: " + data
        cmd.stderr.on "data", (data) ->
            grunt.log.write "stderr: " + data
        cmd.on 'close', (code) ->
            grunt.log.write 'child process exited with code ' + code
            done(code)

# vim: set nolist ts=4 sw=4 expandtab :

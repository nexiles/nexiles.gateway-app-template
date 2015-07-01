Ext.define "AppTemplate.widgets.StatusBar",
    extend: "Ext.ux.statusbar.StatusBar"

    xtype: "nexiles-statusbar"
    alias: "widget.nexiles-statusbar"

    version_loaders: [
        url: "resources/version.json"
        tpl: "{name} v{version} - build {build} - date {date}"
    ]

    make_item: (options) ->
        xtype: "component"
        tpl: options?.tpl or "{name} v{version} - build {build} date {date}"
        cls: "x-toolbar-text x-box-item x-toolbar-item x-toolbar-text-default"
        data:
            name: "?"
            version: "?"
            build: "?"
            date: "?"
        loader:
            url: options?.url or "resources/version.json"
            renderer: "data"
            autoLoad: yes

    make_items: (configs)->
        items = [ "->" ]

        for option in configs
            items.push @make_item option
            items.push "-"

        items.push "copyright &copy; #{new Date().getFullYear()} - <a href='http://www.nexiles.de' target='_blank'>nexiles GmbH</a>"
        return items

    initComponent: ->
        Ext.applyIf @,
            items: @make_items @version_loaders

        @callParent arguments

# vim: set ft=coffee ts=4 sw=4 expandtab :


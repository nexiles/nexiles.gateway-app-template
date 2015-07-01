###*
# This class is the main view for the application. It is specified in app.js as the
# "autoCreateViewport" property. That setting automatically applies the "viewport"
# plugin to promote that instance of this class to the body element.
#
# TODO - Replace this content of this view to suite the needs of your application.
###

Ext.define 'AppTemplate.view.main.MainController',
  extend: 'Ext.app.ViewController'
  requires: [
  ]
  alias: 'controller.main'

  init: ->
    console.log "#{@$className}.init"

  ############################################################################
  # Business Logic
  ############################################################################

  ############################################################################
  # EVENT HANDLERS
  ############################################################################

  onClick: (button, e) ->
    console.debug "#{@$className}.onClick:"
    Ext.Msg.alert "Hello!", "You clicked the button!"

  onSubmit: (form) ->
    values = @lookupReference("form").getValues()
    win = Ext.create "Ext.Window",
      title: "Form Values"
      width: 300
      height: 200
      closable: yes
      items: [
        xtype: "propertygrid"
        source: values
      ]

    win.items.getAt(0).findPlugin('cellediting').disable();
    win.show()


###*
# The main application class. An instance of this class is created by app.js when it calls
# Ext.application(). This is the ideal place to handle application launch and initialization
# details.
###

if window.template
  console.debug "**** TEMPLATE MODE ****"
  Ext.Loader.setConfig
    disableCaching: no
    paths:
      AppTemplate: "app"
      "Ext.ux": "ext/ux"

Ext.define 'AppTemplate.Application',
  extend: 'Ext.app.Application'
  requires: [
    "Ext.app.*"
    "Ext.layout.*"
    "Ext.panel.*"
    "Ext.tree.*"
    "Ext.grid.*"
    "Ext.data.*"
    "Ext.state.*"
    "AppTemplate.*"
  ]
  name: 'AppTemplate'

  models: [
  ]

  stores: [
  ]

  launch: ->
    # Configure LocalStorage for stateful UI
    # provider = new Ext.state.LocalStorageProvider
    #     prefix: "uistate-"
    # Ext.state.Manager.setProvider provider

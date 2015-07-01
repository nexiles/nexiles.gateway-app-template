###*
# This class is the main view for the application. It is specified in app.js as the
# "autoCreateViewport" property. That setting automatically applies the "viewport"
# plugin to promote that instance of this class to the body element.
#
# TODO - Replace this content of this view to suite the needs of your application.
###

Ext.define 'AppTemplate.view.main.Main',
  extend: 'Ext.panel.Panel'
  requires: [
    'AppTemplate.view.main.MainController'
    'AppTemplate.view.main.MainModel'
    'AppTemplate.widgets.StatusBar'
  ]

  xtype: 'app-main'
  controller: 'main'
  viewModel: type: 'main'
  plugins: "viewport"

  bind:
    title: "{name}"
  layout: "border"

  items: [
    region: "west"
    width: "20%"
    title: "Navigation"
    collapsible: yes
    collapsed: yes
    html: """Some navigation here"""
  ,
    region: "center"
    xtype: "form"
    reference: "form"
    title: "Main Content"
    bodyPadding: 10
    items: [
      xtype: "textfield"
      fieldLabel: "A text field"
      name: "text"
    ,
      xtype: "textfield"
      fieldLabel: "Another text field"
      name: "name"
      allowBlank: no
    ,
      xtype: 'datefield',
      fieldLabel: 'From'
      name: 'from_date'
      maxValue: new Date()
    ,
      xtype: 'datefield'
      fieldLabel: 'To'
      name: 'to_date'
      value: new Date()
    ,
      xtype: "button"
      text: "Click me!"
      listeners:
        click: "onClick"
    ]
    buttons: [
      text: "Cancel"
    ,
      text: "Submit"
      formBind: yes
      listeners:
        click: "onSubmit"
    ]
  ]
  bbar: [
    xtype: "nexiles-statusbar"
    text: "Ready"
  ]

# EOF

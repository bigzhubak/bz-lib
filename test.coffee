Vue = require './vue_local.coffee'
error = require 'lib/functions/error.coffee'
v_test = new Vue
  created:->
    error.setOnErrorVm(@)
  data:->
    items: [
      1
      2
      3
      4
      5
    ]
    oauths:[
      {
        'name':'twitter'
        'show_name':'Twitter'
      }
      {
        'name':'github'
        'show_name':'GitHub'
      }
      {
        'name':'douban'
        'show_name':'豆瓣'
      }
    ]
    simditor_content:'simditor content'

    navbar_header:
      name:'Test'
      href:'/'
    nav_links:[
      {
        name:'Changelog'
        href:'/Changelog'
        target:''
      },
      {
        name:'云南程序员'
        href:'http://yncoder.github.io/'
        target:'_blank'
      }
    ]

  el:'#v_test'
  components:
    'main-login': require('lib/components/main-login'),
    'simditor': require('lib/components/simditor'),
    'vnav': require('lib/components/nav-bz'),
    'bz-str': require('lib/components/bz-str'),


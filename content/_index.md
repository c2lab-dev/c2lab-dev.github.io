---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: slider
    content:
      slides:
      - title: C2Lab
        content: Cryogenic Computing Laboratory at Kyushu University
        align: center
        background:
          gradient_start: '#1a1a2e'
          gradient_end: '#16213e'
          text_color_light: true
      - title: Cryogenic AI Acceleration
        content: 'Advancing AI computing with superconducting circuits at cryogenic temperatures for unprecedented energy efficiency.'
        align: left
        background:
          gradient_start: '#16213e'
          gradient_end: '#0f3460'
          text_color_light: true
      - title: Superconducting EDA Development
        content: 'Building full-stack EDA workflows for designing and simulating superconducting digital systems.'
        align: center
        background:
          gradient_start: '#0f3460'
          gradient_end: '#16213e'
          text_color_light: true
      - title: Cryogenic Measurement System
        content: 'Developing advanced measurement infrastructure for characterizing devices at ultra-low temperatures.'
        align: right
        background:
          gradient_start: '#16213e'
          gradient_end: '#1a1a2e'
          text_color_light: true
        link:
          icon: users
          icon_pack: fas
          text: Join Our Team
          url: './contact/'
    design:
      slide_height: ''
      is_fullscreen: true
      loop: false
      interval: 2000
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---

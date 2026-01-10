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
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.6
          position: center
          color: '#1a1a1a'
        link:
          icon: arrow-down
          icon_pack: fas
          text: Learn More
          url: '#about'
      - title: Cryogenic AI Acceleration
        content: 'Advancing AI computing with superconducting circuits at cryogenic temperatures for unprecedented energy efficiency.'
        align: left
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#2c3e50'
      - title: Superconducting EDA Development
        content: 'Building full-stack EDA workflows for designing and simulating superconducting digital systems.'
        align: center
        background:
          image:
            filename: contact.jpg
            filters:
              brightness: 0.6
          position: right
          color: '#34495e'
      - title: Cryogenic Measurement System
        content: 'Developing advanced measurement infrastructure for characterizing devices at ultra-low temperatures.'
        align: right
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#2c3e50'
        link:
          icon: users
          icon_pack: fas
          text: Join Our Team
          url: './contact/'
    design:
      slide_height: ''
      is_fullscreen: true
      loop: true
      interval: 4000
  
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

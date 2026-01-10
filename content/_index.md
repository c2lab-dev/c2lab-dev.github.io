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
        link:
          icon: users
          icon_pack: fas
          text: Join Our Team
          url: './contact/'
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
    design:
      slide_height: ''
      is_fullscreen: true
      loop: false
      interval: 2000
  
  - block: about.biography
    id: about
    content:
      title: Biography
      username: admin
  
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: card
  
  - block: collection
    id: recent
    content:
      title: Recent Publications
      text: |-
        <p style="text-align: center; color: #666; font-size: 0.9em; margin-bottom: 1em;">
        <em>Filter by Type: 1 = Conference paper, 2 = Journal article</em>
        </p>
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - event
    design:
      columns: '2'
      view: compact
  
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        For prospective students, collaborations, or general inquiries, please reach out.
      email: olivia@c2lab.org
      address:
        street: 744 Motooka, Nishi-ku
        city: Fukuoka
        postcode: '819-0395'
        country: Japan
        country_code: JP
      directions: Graduate School of Information Science and Electrical Engineering, Kyushu University
      contact_links:
        - icon: twitter
          icon_pack: fab
          name: DM Me
          link: 'https://twitter.com/OliviaChenC2Lab'
    design:
      columns: '2'
---

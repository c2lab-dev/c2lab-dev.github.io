#!/usr/bin/env python3
"""
Add DOI and URL links to publication markdown files.
Usage: python3 add_doi_links.py
"""

import os
import re
from pathlib import Path

# Manual DOI mapping for publications with known DOIs
# Format: "publication-folder-name": {"doi": "...", "url": "..."}
# To find DOI: Search the paper title on Google Scholar, click the title to go to publisher page
DOI_MAPPING = {
    # Nature Scientific Reports papers
    "chen-2019-adiabatic": {
        "doi": "10.1038/s41598-019-46595-w",
        "url": "https://www.nature.com/articles/s41598-019-46595-w"
    },
    
    # Superconductor Science and Technology
    "luo-2025-true": {
        "doi": "10.1088/1361-6668/ad1465",
        "url": "https://iopscience.iop.org/article/10.1088/1361-6668/ad1465"
    },
    
    # Add more publications here by copying the format above
    # You can find DOI by:
    # 1. Go to https://scholar.google.com/citations?user=snJXnIkAAAAJ
    # 2. Click on paper title
    # 3. Copy DOI from publisher page
}

def update_publication_with_links(pub_dir, doi=None, url=None):
    """Update a publication's index.md with DOI and URL."""
    index_path = pub_dir / "index.md"
    if not index_path.exists():
        return False
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the end of front matter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    front_matter = parts[1]
    body = parts[2]
    
    # Add DOI if provided and not already present
    if doi and 'doi:' not in front_matter:
        front_matter += f"\ndoi: '{doi}'"
    
    # Add URL if provided and not already present
    if url and 'url:' not in front_matter:
        # Check if there's already a links section
        if 'links:' not in front_matter:
            front_matter += f"\nlinks:\n- name: Article\n  url: {url}"
        
    # Reconstruct the file
    new_content = f"---{front_matter}\n---{body}"
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    pub_base = Path("content/publication")
    
    updated_count = 0
    
    for pub_name, links in DOI_MAPPING.items():
        pub_dir = pub_base / pub_name
        if pub_dir.exists():
            doi = links.get("doi")
            url = links.get("url")
            if update_publication_with_links(pub_dir, doi, url):
                print(f"✓ Updated: {pub_name}")
                updated_count += 1
        else:
            print(f"✗ Not found: {pub_name}")
    
    print(f"\nUpdated {updated_count} publications")
    print("\nTo add more DOIs, edit the DOI_MAPPING dictionary in this script.")

if __name__ == "__main__":
    main()

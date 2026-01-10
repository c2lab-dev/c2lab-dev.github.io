#!/usr/bin/env python3
"""
Add publication links to all papers based on their citation info.
Generates search URLs based on journal/conference information.
"""

import os
import re
from pathlib import Path
import bibtexparser

def get_publisher_url(bib_entry):
    """Generate publisher URL based on journal/conference name."""
    
    # Extract publication venue
    venue = ""
    if 'journal' in bib_entry:
        venue = bib_entry['journal'].lower()
    elif 'booktitle' in bib_entry:
        venue = bib_entry['booktitle'].lower()
    
    title = bib_entry.get('title', '').replace('{', '').replace('}', '')
    
    # IEEE publications
    if any(x in venue for x in ['ieee', 'transactions', 'conference', 'international conference']):
        return f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={title.replace(' ', '%20')}"
    
    # Nature journals
    if 'nature' in venue or 'scientific reports' in venue:
        return f"https://www.nature.com/search?q={title.replace(' ', '+')}"
    
    # IOP Publishing
    if 'superconductor science' in venue or 'iop' in venue:
        return f"https://iopscience.iop.org/search?q={title.replace(' ', '+')}"
    
    # ACM
    if 'acm' in venue:
        return f"https://dl.acm.org/action/doSearch?AllField={title.replace(' ', '+')}"
    
    # Springer
    if 'springer' in venue:
        return f"https://link.springer.com/search?query={title.replace(' ', '+')}"
    
    # IEICE
    if 'ieice' in venue:
        return f"https://search.ieice.org/bin/search.php?search_type=simple&search_mode=normal&lang=E&q={title.replace(' ', '+')}"
    
    # Elsevier/ScienceDirect
    if any(x in venue for x in ['elsevier', 'microelectronics', 'vlsi']):
        return f"https://www.sciencedirect.com/search?qs={title.replace(' ', '%20')}"
    
    # Default: Google Scholar
    return f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"

def update_publication(pub_dir):
    """Update a publication with its link."""
    index_path = pub_dir / "index.md"
    cite_path = pub_dir / "cite.bib"
    
    if not index_path.exists() or not cite_path.exists():
        return None
    
    # Parse BibTeX
    with open(cite_path, 'r', encoding='utf-8') as f:
        bib_database = bibtexparser.load(f)
    
    if not bib_database.entries:
        return None
    
    entry = bib_database.entries[0]
    
    # Read current index.md
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has links
    if 'links:' in content or 'url:' in content:
        return "skipped"
    
    # Split front matter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    front_matter = parts[1]
    body = parts[2]
    
    # Generate URL
    url = get_publisher_url(entry)
    
    # Add link
    front_matter += f"\nlinks:\n- name: Article\n  url: {url}\n  icon: link\n  icon_pack: fas"
    
    # Write back
    new_content = f"---{front_matter}---{body}"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return "updated"

def main():
    pub_base = Path("content/publication")
    
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    
    for pub_dir in sorted(pub_base.iterdir()):
        if pub_dir.is_dir():
            result = update_publication(pub_dir)
            if result == "updated":
                stats["updated"] += 1
                print(f"✓ {pub_dir.name}")
            elif result == "skipped":
                stats["skipped"] += 1
            elif result is None:
                stats["failed"] += 1
    
    print(f"\n{'='*50}")
    print(f"Updated: {stats['updated']}")
    print(f"Skipped (already has links): {stats['skipped']}")
    print(f"Failed: {stats['failed']}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

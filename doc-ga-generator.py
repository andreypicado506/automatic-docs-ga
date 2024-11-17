#!/usr/bin/env python3
import re

def extract_tags(md_file_path):
    # Regular expression to match the tags
    tag_pattern = r'<!--\s*doc-ga-generator\s+id=(\d+)\s+type=(\w+)\s+target_action="([^"]+)"\s*-->'
    
    with open(md_file_path, 'r', encoding='utf-8') as file:
      content = file.read()
    
    # Find all matches and preserve their order
    matches = re.findall(tag_pattern, content)
    
    # Format the matches as dictionaries for better readability
    tags = [
      {'id': match[0], 'type': match[1], 'target_action': match[2]}
      for match in matches
    ]
    
    return tags

def main():
    md_file_path = './README.md'
    tags = extract_tags(md_file_path)
    print(tags)

if __name__ == '__main__':
    main()
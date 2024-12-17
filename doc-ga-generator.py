#!/usr/bin/env python3
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Extract tags from a markdown file')
parser.add_argument('--md_file_path', type=str, default="README.md", help='Path to the markdown file')
parser.add_argument('--generate-md-file', type=str, help='Generate a markdown file with the tags')
args = parser.parse_args()

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

def group_tags_by_id(tags):
    tags_by_id = {}
    for tag in tags:
        tag_id = tag['id']
        if tag_id not in tags_by_id:
            tags_by_id[tag_id] = []
        tags_by_id[tag_id].append(tag)
    return tags_by_id

def validate_tags(tags_by_id):
    # Check for validation errors
    grouped_tags = tags_by_id
    seen_ids = set()
    for tag_id, tag_group in grouped_tags.items():
        # Check that each group contains exactly 2 tags
        if len(tag_group) != 2:
            print(f"[Error] Tags with id={tag_id} are not exactly 2 tags (start and end).")
            return False
        
        # Check the first tag is of type "start"
        if tag_group[0]['type'] != 'start':
            print(f"[Error] The first tag in group with id={tag_id} is not of type 'start'.")
            return False
        
        # Check the second tag is of type "end"
        if tag_group[1]['type'] != 'end':
            print(f"[Error] The second tag in group with id={tag_id} is not of type 'end'.")
            return False
        
        # Check for duplicate group IDs
        if tag_id in seen_ids:
            print(f"[Error] Duplicate group found with id={tag_id}.")
            return False
        
        # Mark this ID as seen
        seen_ids.add(tag_id)
    
    # If all checks pass, validation is successful
    print("[INFO] All tags are valid.")
    return True


def main():
    md_file_path = args.md_file_path
    if not os.path.isfile(md_file_path):
        print(f"{md_file_path} file not found in the current directory")
        exit(1)
    tags = extract_tags(md_file_path)
    if not tags:
        print('No tags found in the README.md file')
        return
    print(">> Grouping tags by ID...")
    tags_by_id = group_tags_by_id(tags)

    print(">> Validating tags...")
    tags_are_valid = validate_tags(tags_by_id)


if __name__ == '__main__':
    main()
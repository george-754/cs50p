# Convert an embeded youtube URL to a shorter, shareable youtu.be URL

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    validate = re.search(r"src=\"\w+:+/+(\w+\.)?youtube\.\w+/\w+/\w+\"", s.strip())

    if validate:
        # Clean up the validate link
        link = validate.group(0).lstrip("src=\"")
        link = link.rstrip("\"")
        
        # Extract the last part of the link after the last "/"
        extract = re.search(r"/\w+$", link)
        extract = extract.group(0).lstrip("/")
        
        # Create the new link from the extracted extract
        new_link = f"https://youtu.be/{extract}"
        
        # Output the new link
        return new_link

    # Ouput none if validate couldn't find a match
    return validate



if __name__ == "__main__":
    main()
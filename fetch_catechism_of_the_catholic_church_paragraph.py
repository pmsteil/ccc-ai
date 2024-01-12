# filename: fetch_catechism_of_the_catholic_church_paragraph.py
# Author: Patrick M. Steil
# Date: 2024-01-12
# Description: Fetches a paragraph from the Catechism of the Catholic Church (CCC)
# Usage:
#   cli: python3 fetch_catechism_of_the_catholic_church_paragraph.py 1111
#   import: from fetch_catechism_of_the_catholic_church_paragraph import fetch_ccc_paragraph
#           fetch_ccc_paragraph(1111)

import sys
import requests
import re

# URL to the raw CCC text
CCC_URL = "https://raw.githubusercontent.com/pmsteil/ccc-cleanup/master/ccc.md"

def fetch_ccc_paragraph( ccc_paragraph_number: int):
    """
    Fetches a paragraph from the Catechism of the Catholic Church (CCC)
    using my GitHub markdown repository of the CCC.
    :param ccc_paragraph_number: The paragraph number to fetch
    """

    # throw an error if ccc_paragraph_number is not an integer
    if not isinstance(ccc_paragraph_number, int):
        raise TypeError("Paragraph number must be an integer.")
    # fetches a random paragraph from the Catechism of the Catholic Church
    try:

        response = requests.get( CCC_URL, timeout=1500)
        if response.status_code == 200:
            content = response.text
            # Use regular expression to find ccc_paragraph_number
            match = re.search(r'CCC {ccc_paragraph_number}\s*(.*?)\n'.format(ccc_paragraph_number=ccc_paragraph_number), content, re.DOTALL)
            if match:
                return match.group(1).strip()
            else:
                return f"Paragraph {ccc_paragraph_number} not found."
        else:
            return "Failed to retrieve the content."
    except requests.RequestException as e:
        return str(e)



if __name__ == "__main__":
    # Fetch and print the content of paragraph 1111
    # get first arg passed
    arg = int(sys.argv[1])
    print( f"CCC {arg}")
    content = fetch_ccc_paragraph(arg )
    print(content)

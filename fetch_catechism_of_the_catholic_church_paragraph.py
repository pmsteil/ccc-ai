# Description: Fetch one or more paragraphs from the Catechism of the Catholic Church (CCC)
# Author: Patrick M. Steil
# Date: 2024-01-12
# Version: 1.0.1
# Usage:
#   import: from fetch_catechism_of_the_catholic_church_paragraph import fetch_ccc_paragraph
#           fetch_ccc_paragraph( [1, 1111, 2222, 2865] )
#   returns: a list of paragraph contents

import sys
import requests
import re

# URL to the raw CCC text
CCC_URL = "https://raw.githubusercontent.com/pmsteil/ccc-cleanup/master/ccc.md"
CCC_CATECHISM = "" # cache the catechism



def getCatechisim():
    """
    Fetches the Catechism of the Catholic Church (CCC) from my GitHub markdown repository of the CCC.
    Caches it and returns the cached content if already downloaded.
    """
    if CCC_CATECHISM is "":
        result = requests.get(CCC_URL)
        if result.status_code == 200:
            globals()['CCC_CATECHISM'] = result
        else:
            raise requests.RequestException("Failed to retrieve the content.")
    return CCC_CATECHISM




def fetch_ccc_paragraph( ccc_paragraph_numbers: list):
    """
    Fetches a paragraph from the Catechism of the Catholic Church (CCC)
    using my GitHub markdown repository of the CCC.
    :param ccc_paragraph_number: A list of the paragraph numbers to fetch
    """

    results = []

    # loop through the list of paragraph numbers
    # and determnine if the paragraph number is valid
    for ccc_paragraph_number in ccc_paragraph_numbers:
        # throw an error if ccc_paragraph_number is not an integer
        if not isinstance(ccc_paragraph_number, int):
            raise TypeError("Paragraph number must be an integer.")
        # fetches a random paragraph from the Catechism of the Catholic Church
        try:
            response = getCatechisim()

            if response.status_code == 200:
                content = response.text
                # Use regular expression to find ccc_paragraph_number
                match = re.search(r'CCC {ccc_paragraph_number}\s*(.*?)\n'.format(ccc_paragraph_number=ccc_paragraph_number), content, re.DOTALL)
                if match:
                    # return match.group(1).strip()
                    results += [match.group(1).strip()]
                else:
                    results += [f"Paragraph {ccc_paragraph_number} not found."]
                    # return f"Paragraph {ccc_paragraph_number} not found."
            else:
                results += ["Failed to retrieve the content."]
                # return "Failed to retrieve the content."
        except requests.RequestException as e:
            results += [str(e)]
            # return str(e)

    return results


if __name__ == "__main__":
    # Fetch and print the content of paragraph 1111
    # get first arg passed
    arg = int(sys.argv[1])
    print( f"CCC {arg}")
    content = fetch_ccc_paragraph( [arg] )
    print(content)

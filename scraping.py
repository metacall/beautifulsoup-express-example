#!/usr/bin/env python3

#
#	MetaCall BeautifulSoup NodeJS Example by Parra Studios
#	Example of using Python BeautifulSoup in NodeJS with MetaCall.
#
#	Copyright (C) 2016 - 2020 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#

import urllib.request
import certifi
from bs4 import BeautifulSoup

def links(url):
    try:
        # Open URL for reading the HTML (allowing SSL certificates with certifi)
        fp = urllib.request.urlopen(url, cafile=certifi.where())

        # Read data as a bytearray
        data = fp.read()

        # Convert into a utf8 string
        string = data.decode("utf8")

        # Close URL
        fp.close()

        # Initialize beautiful soup in order to scrape the web
        soup = BeautifulSoup(string, features='html.parser')

        # Obtain all href for each link
        links = map(lambda a: a.get('href'), soup.find_all('a'))

        # Filter the ones that begin with http
        result = filter(lambda link: link.startswith('http'), links)

        # Return it as a list
        return list(result)
    except:
        return []

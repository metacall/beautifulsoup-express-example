/*
 *	MetaCall BeautifulSoup NodeJS Example by Parra Studios
 *	Example of using Python BeautifulSoup in NodeJS with MetaCall.
 *
 *	Copyright (C) 2016 - 2020 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
 *
 *	Licensed under the Apache License, Version 2.0 (the "License");
 *	you may not use this file except in compliance with the License.
 *	You may obtain a copy of the License at
 *
 *		http://www.apache.org/licenses/LICENSE-2.0
 *
 *	Unless required by applicable law or agreed to in writing, software
 *	distributed under the License is distributed on an "AS IS" BASIS,
 *	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *	See the License for the specific language governing permissions and
 *	limitations under the License.
 *
 */

'use strict';

// MetaCall imports
const { metacall, metacall_load_from_file } = require('metacall');

// Load Python script scraping.py
metacall_load_from_file('py', [ 'scraping.py' ]);

// Express imports
const express = require('express');
const app = express();
const port = 3000;

// Configure server routes
app.get('/', (req, res) => res.send(req.query.url ?
    metacall('links', req.query.url) :
    'Invalid URL parameter');

// Create Express server (TODO: stdout does not work properly on node loader)
app.listen(port, () => console.log(`Listening on port ${port}!`));

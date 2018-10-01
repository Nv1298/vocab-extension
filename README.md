# vocab-extension

## Files
- background.js
- manifest.json
- voc.html
- insert.js: insert code into html file
- slide.js: sliders

### Populate Data
The extension uses the wrapper.py file to update the data, which can also be found in ox-dictionary repository
Can populate the data for synonym.js, antonym.js, sent.js, words.js,text.js ... with the suites
- aSuite.py - populate antonym.js with antonyms
- eSuite.py - populate sent.js with sentences
- sSuite.py - populate synonym.js with synonyms
- testSuite.py - populate words.js and text.js with words and definitions respectively
- suite.py - populate prons.js with pronunciations

Otherwise the javascript files are already pre-populated

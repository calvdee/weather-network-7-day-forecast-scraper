# Weather Network 7-Day Precipitation Forecast Scraper

## Overview
A Python application that scrapes 7-day precipitation forecasts from the Weather Network website with a url similar to www.theweathernetwork.com/ca/14-day-weather-trend/{PROVINCE}/{CITY}', using OCR (Optical Character Recognition). This application is part of a larger application that compares the performance of precipitation forecasting models that attempt to directly forecast the number of rainy days in a week.

## Dependencies
See requirements.txt.

## Project Structure

### src
Application source code.

### tests
Unit tests. Requires a file called `creds.txt` in this folder that contains the Azure Cognitive Services key.

## TODO
* Handle errors in OCR service.
* Extract the Azure Cognitive Services url.

## License
The MIT License (MIT)

Copyright (c) 2019 Calvin De Lima

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
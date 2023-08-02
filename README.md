# google_image_download

# Google Image Downloader

Google Image Downloader is a Python program that allows you to download images from Google using the Google Images Search API.

## Getting Started

These instructions will help you set up and run the Google Image Downloader program on your local machine.

### Prerequisites

- Python 3.x
- `google_images_search` library

You can install the required library using pip:

pip install google_images_search


### API Key and Custom Search Engine ID

Before running the program, you need to obtain a Google API key and create a custom search engine. Follow these steps:

1. Sign up for the Google Custom Search JSON API: https://developers.google.com/custom-search/docs/tutorial/introduction

2. Create a custom search engine and get the custom search engine ID: https://developers.google.com/custom-search/docs/tutorial/creatingcse

3. Replace `<YOUR_GOOGLE_API_KEY>` and `<YOUR_GOOGLE_CX>` in the `download_images()` function with your actual Google API key and custom search engine ID.

### Usage

1. Clone this repository or download the `google_image_downloader.py` file.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the `google_image_downloader.py` file.

4. Run the program by executing the following command:

   python google_image_downloader.py

5. Enter the image you want to download when prompted.

6. Enter the number of images you want to download.

7. The program will download the specified number of images related to your query and save them in a folder named 'downloads'.



To create a Python program for downloading images from Google, we can utilize the google_images_search library. 
Before proceeding, ensure that you have the library installed. If not, you can install it using pip:

pip install google_images_search

from google_images_search import GoogleImagesSearch

def download_images(query, num_images=10):
    # Replace the following with your Google Images Search API credentials
    gis = GoogleImagesSearch('<YOUR_GOOGLE_API_KEY>', '<YOUR_GOOGLE_CX>')

    search_params = {
        'q': query,
        'num': num_images,
        'safe': 'high',
        'fileType': 'jpg|png',  # You can specify other file types here
        'imgType': 'photo',     # Change this to 'clipart', 'face', etc., if needed
    }

    gis.search(search_params=search_params)

    # Download each image
    for image in gis.results():
        image.download('downloads/')  # Save the images in a folder named 'downloads'
        print(f"Downloaded {image.filename}")

if __name__ == "__main__":
    search_query = input("Enter the image you want to download: ")
    num_images_to_download = int(input("Enter the number of images to download: "))

    download_images(search_query, num_images_to_download)


import requests  # lets us download stuff from the internet
import os        # lets us work with folders and files

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for the image link
    url = input("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Nokota_Horses_cropped.jpg/500px-Nokota_Horses_cropped.jpg: ")

    # Make a folder called Fetched_Images (if it doesn’t exist already)
    os.makedirs("Fetched_Images", exist_ok=True)
    

    try:
        # Try to download the image
        response = requests.get(url, timeout=10)

        # If the website gave an error, stop
        response.raise_for_status()

        # Get the name of the file from the URL
        filename = url.split("/")[-1]

        # If no filename found, give it a default name
        if filename == "":
            filename = "downloaded_image.jpg"

        # Full path where we will save the image
        filepath = os.path.join("Fetched_Images", filename)

        # Save the image to the computer
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except Exception as e:
        print(f"✗ An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()


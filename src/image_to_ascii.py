#!/usr/bin/python3

from PIL import Image

ASCII_CHARS = ["@", "#", "%", "?", "*", "+", ";", ":", ",", ".", " "]
ASCII_CHARS_LEN = len(ASCII_CHARS)

def convert_image_to_ascii(image_file):
    # open the image
    image = Image.open(image_file)
    # convert image to grayscale
    image = image.convert("L")
    # resize image with (# cols , # rows) for chars
    image = image.resize((50, 50))

    # initialize output string
    ascii_art = ""
    # loop through pixels
    for y in range(image.height):
        for x in range(image.width):
            # get the pixel value
            pixel_value = image.getpixel((x, y))
            # calculate the ASCII char
            ascii_char_index = pixel_value * ASCII_CHARS_LEN // 256
            # add char to output
            ascii_art += ASCII_CHARS[ascii_char_index] + " "
        # new line at the end of row
        ascii_art += "\n"
    return ascii_art

def main():
  ascii_art = convert_image_to_ascii("image.png")
  print(ascii_art)

  # write the ASCII art to a text file
  try: 
    with open("output.txt", "w") as file:
        file.write(ascii_art)

    print("ASCII art saved to output.txt")
  except:
    print("Wasn't able to print ASCII art to output.txt")

if __name__ == "__main__":
  main()
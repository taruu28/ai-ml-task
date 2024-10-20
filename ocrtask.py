!pip install easyocr
import easyocr

# Create an instance of the Reader class
reader = easyocr.Reader(['en'])  # Replace 'en' with desired languages if needed

results = reader.readtext('/content/sample.jpeg', detail=0)  # performing ocr on the image
hormones_dict = {}  # dict to hold the result

# Process lines to organize them into a dictionary
current_heading = ""
for line in results:
    line = line.strip()
    # Check for headings (assumed to be capitalized)
    if line.isupper():
        current_heading = line
        hormones_dict[current_heading] = []
    else:
        # Add hormone types under the current heading
        if current_heading:
            hormones_dict[current_heading].append(line)

print(hormones_dict)  # output
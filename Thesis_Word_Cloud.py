from wordcloud import WordCloud
import matplotlib.pyplot as plt

input_file = "yourfile.txt" #Save thesis as a text file

# Read text file
with open(input_file, "r", encoding="latin-1") as f:
    text = f.read()

output_image = "wordcloud_inlet_v0.pdf" #different versions to see various combinations 

# High-resolution dimensions (2550x3300 px ≈ 8.5"×11" at 300 dpi)
WIDTH_PX = 2550   # corresponds to 8.5 inches
HEIGHT_PX = 3300  # corresponds to 11 inches

# Generate word cloud
wc = WordCloud(
    width=WIDTH_PX,
    height=HEIGHT_PX,
    background_color="white",
    collocations= True,
    max_words=2000,
    min_font_size=6
).generate(text)

# Display the word cloud
plt.figure(figsize=(8.5, 11), dpi=300)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()

# Save at full print quality
plt.savefig(output_image, dpi=300, bbox_inches="tight", pad_inches=0.1)

print(f"High-resolution word cloud saved to: {output_image}")

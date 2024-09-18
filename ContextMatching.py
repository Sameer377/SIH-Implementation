def keyword_matching(paragraph, keywords):
    # Convert paragraph to lowercase for case-insensitive matching
    paragraph = paragraph.lower()
    
    # Check if each keyword is present in the paragraph
    for keyword in keywords:
        if keyword.lower() in paragraph:
            return True
    return False

# Example usage
paragraph = "Artificial Intelligence is a branch of computer science that focuses on developing smart machines."
keywords = ["intelligent machines", "artificial intelligence"]

if keyword_matching(paragraph, keywords):
    print("At least one keyword is present in the paragraph.")
else:
    print("No keywords are present in the paragraph.")
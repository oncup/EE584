# preprocessing/aspect_extraction.py

def extract_aspect_sentences(review_text, aspect_labels):
    """
    Extract sentences related to given aspects from a review text.
    
    Args:
        review_text (str): Full review text.
        aspect_labels (dict): Dictionary with aspect presence indicators (1 or 0).
        
    Returns:
        str: Concatenated aspect-related sentences.
    """
    sentences = review_text.split('.')
    extracted = []
    
    if aspect_labels.get('Contribution', 0) and len(sentences) > 0:
        extracted.append(sentences[0].strip())
    if aspect_labels.get('Motivation', 0) and len(sentences) > 1:
        extracted.append(sentences[1].strip())
    if aspect_labels.get('Claims', 0) and len(sentences) > 2:
        extracted.append(sentences[2].strip())
    if aspect_labels.get('Support', 0) and len(sentences) > 3:
        extracted.append(sentences[3].strip())
    
    return " ".join(extracted)

# Example usage
if __name__ == "__main__":
    example_review = "This paper proposes a novel method. It is motivated by previous failures. The main claim is strong. Experiments support the claim."
    example_aspects = {'Contribution': 1, 'Motivation': 1, 'Claims': 1, 'Support': 1}
    
    result = extract_aspect_sentences(example_review, example_aspects)
    print("Extracted aspect sentences:")
    print(result)

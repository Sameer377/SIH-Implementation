from sentence_transformers import SentenceTransformer, util

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')



def isContextMatched(paragraph, context,threshold):
    # Get embeddings for both the context and the paragraph 
    embedding_context = model.encode(context, convert_to_tensor=True)
    embedding_paragraph = model.encode(paragraph, convert_to_tensor=True)

    # Compute the cosine similarity
    similarity = util.pytorch_cos_sim(embedding_context, embedding_paragraph)

    # Convert to scalar value
    similarity_score = similarity.item()

    # Threshold to decide whether the context is present in the paragraph
    if similarity_score > threshold:  # Adjust the threshold as needed
        return True
    else:
        return False

# Example usage
""" if isContextMatched(paragraph, context):
    print("The context is present in the paragraph.")
else:
    print("The context is not present in the paragraph.")
 """
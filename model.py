from sentence_transformers import SentenceTransformer, util

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def encode_text(text: str):
    try:
        return MODEL.encode(text, batch_size=8)
    except Exception as e:
        print(f"Error during encoding: {e}")
        return None

def calculate_cosine_similarity(embedding1, embedding2) -> float:
    return util.cos_sim(embedding1, embedding2).item()

def get_cosine_similarity(text1: str, text2: str) -> float:
    embedding1 = encode_text(text1)
    embedding2 = encode_text(text2)

    if embedding1 is None or embedding2 is None:
        return None

    return calculate_cosine_similarity(embedding1, embedding2)

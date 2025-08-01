from sentence_transformers import SentenceTransformer, util
import torch

def load_similarity_model():
    """
    Loads the SentenceTransformer model for comparing job descriptions and resumes.
    """
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    model = model.to(torch.device('cpu'))  # or use 'cuda' if available
    return model

def encode(model, text_list):
    """
    Encodes a list of text strings using the SentenceTransformer model.
    """
    if isinstance(text_list, str):
        text_list = [text_list]
    return model.encode(text_list, convert_to_tensor=True)

def calculate_similarity(jd_lines, cv_lines, jd_embeds, cv_embeds, threshold=0.5):
    """
    Compares each job description line to the resume and prints match results.
    """
    results = []

    for i, jd_line in enumerate(jd_lines):
        sims = util.cos_sim(jd_embeds[i], cv_embeds)[0]
        best_score = float(sims.max())
        best_match = cv_lines[sims.argmax()]

        result = {
            "jd": jd_line,
            "match": best_match,
            "score": best_score,
            "matched": best_score > threshold
        }
        results.append(result)

    return results

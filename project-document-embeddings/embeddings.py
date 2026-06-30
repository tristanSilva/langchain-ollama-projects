from langchain_ollama import OllamaEmbeddings
import numpy as np

embedder = OllamaEmbeddings(model="nomic-embed-text")

text = "The dog is happy"
vector = embedder.embed_query(text)

print("Vector length (dimensions): ")
print(len(vector))
print("First 10 numbers of thev vector: ")
print(vector[:10])


def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


sentence_a = "The dog is happy."
sentence_b = "The canine is joyful."
sentence_c = "The stock market crashed today."

vec_a = embedder.embed_query(sentence_a)
vec_b = embedder.embed_query(sentence_b)
vec_c = embedder.embed_query(sentence_c)

similarity_ab = cosine_similarity(vec_a, vec_b)
similarity_ac = cosine_similarity(vec_a, vec_c)

print("Similarity A - B")
print(f"{sentence_a}")
print(f"{sentence_b}")
print(f"Similarity: {similarity_ab:.4f}")
print("Similarity A - c")
print(f"{sentence_a}")
print(f"{sentence_c}")
print(f"Similarity: {similarity_ac:.4f}")

print("NAGA CITY SIMILARITY TEST")
print()

query = "Who runs the local government?"
candidate_1 = "The local government is led by a city mayor and a city council."
candidate_2 = "The Peñafrancia Festival is the most important cultural event."
candidate_3 = "Naga City is part of the Bicol Region, Region V."

vec_query = embedder.embed_query(query)
vec_1 = embedder.embed_query(candidate_1)
vec_2 = embedder.embed_query(candidate_2)
vec_3 = embedder.embed_query(candidate_3)

print("QUERY")
candidate_vec_1 = f"{cosine_similarity(vec_query, vec_1):.4f}"
candidate_vec_2 = f"{cosine_similarity(vec_query, vec_2):.4f}"
candidate_vec_3 = f"{cosine_similarity(vec_query, vec_3):.4f}"

print()
print(f"vs Candidate 1 : {candidate_vec_1}")
print(f"vs Candidate 2 : {candidate_vec_2}")
print(f"vs Candidate 3 : {candidate_vec_3}")

import os
import json
import chromadb
from chromadb.utils import embedding_functions


def get_chroma_client():
    return chromadb.PersistentClient(path="./chroma_db")


def setup_and_populate_db(json_file_path="./data/sports_facts.json"):
    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    if collection.count() > 0:
        return collection

    if not os.path.exists(json_file_path):
        print("Sports facts file not found!")
        return collection

    with open(json_file_path, "r", encoding="utf-8") as f:
        facts = json.load(f)

    documents = []
    metadatas = []
    ids = []

    for i, item in enumerate(facts):
        documents.append(item["fact"])
        metadatas.append({"sport": item["sport"]})
        ids.append(f"fact_{i}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    return collection


def query_historic_facts(sport, query_text, n_results=2):
    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        where={"sport": sport}
    )

    if results["documents"]:
        return results["documents"][0]

    return []
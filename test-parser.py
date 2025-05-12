from parser import extract_articles

for artigo in extract_articles('simplewiki.xml', limit=3):
    print("\n--- ARTIGO ---")
    print("Título:", artigo['title'])
    print("Texto:", artigo['text'][:200])

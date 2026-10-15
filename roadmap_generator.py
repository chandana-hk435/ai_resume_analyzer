
def generate_roadmap(missing):
    return [f"Week {i}: Learn {s}" for i,s in enumerate(missing[:4],1)]
def identify_gaps(found, required_str):
    req=[s.strip() for s in required_str.lower().split(',')]
    return [r for r in req if r not in [f.lower() for f in found]]

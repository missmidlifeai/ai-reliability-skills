#!/usr/bin/env python3
"""Deterministic publish gate. Usage: python sourcecheck.py items.json
items.json: [{"claim": "...", "quote": "...", "source": "<full source text>"}]
Exit 0 if all pass, 1 if any fail. One line per failure. Never override; reword or drop."""
import json, re, sys

STOP = set("a an the of and or to in on at for by with is are was were be been it its this that as from not no but if than then has have had will would".split())

def norm(s):
    s = s.lower()
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2013", "-"), ("\u2014", "-")):
        s = s.replace(a, b)
    s = re.sub(r"(?<=\d),(?=\d{3}\b)", "", s)      # 1,000 -> 1000
    s = re.sub(r"\bpercent\b", "%", s)
    s = re.sub(r"\s*%", "%", s)
    s = re.sub(r"\b(minutes?|mins?)\b", "min", s)
    s = s.replace("$", "")
    return re.sub(r"\s+", " ", s).strip()

def nums(s):
    return set(re.findall(r"\d+(?:\.\d+)?", norm(s)))

def words(s):
    return {w for w in re.findall(r"[a-z0-9%']+", norm(s)) if w not in STOP and len(w) > 2}

def names(claim):
    toks = re.findall(r"[A-Za-z][A-Za-z'\-]*", claim)
    return {t.lower() for i, t in enumerate(toks) if i > 0 and t[0].isupper()}

def check(it):
    claim, quote, source = it["claim"], it["quote"], it["source"]
    if norm(quote) not in norm(source):
        return "STAGE1 quote not found in source (after normalizing case/space/number format)"
    miss = nums(claim) - nums(quote)
    if miss:
        return f"STAGE2 numbers in claim not in quote: {sorted(miss)}"
    qw = words(quote)
    miss = names(claim) - qw
    if miss:
        return f"STAGE2 names in claim not in quote: {sorted(miss)}"
    cw = words(claim)
    if cw and len(cw & qw) / len(cw) < 0.6:
        return "STAGE2 under 60% of claim's content words appear in quote"
    return None

if __name__ == "__main__":
    items = json.load(open(sys.argv[1]))
    bad = 0
    for i, it in enumerate(items):
        err = check(it)
        if err:
            bad += 1
            print(f"FAIL #{i}: {err} | claim: {it['claim'][:80]}")
    print(f"{len(items) - bad}/{len(items)} passed")
    sys.exit(1 if bad else 0)

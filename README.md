# Operation Gate: GATE DA 2027 (Data Science & AI)

Preparation material for the **GATE 2027 Data Science & AI (DA)** paper (February 2027), plus an
out-of-syllabus set for learning after the exam.

Every topic is told through two friends: **Ramu** asks "why?" and **Somu** explains with everyday examples.
Each topic comes as a LaTeX-built PDF and as a narrated, animated film whose Python code was run, so the
output on screen is the real output.

## What is here

| Part | What | Where |
|------|------|-------|
| Syllabus PDFs | 7 sections (probability and statistics, linear algebra, calculus and optimisation, programming and DSA, DBMS and warehousing, machine learning, AI) with past GATE DA questions 2024-2026 solved | [da-2027](da-2027/README.md) |
| Syllabus films | 13 core films in watch order, covering every syllabus section | [da-2027](da-2027/README.md) |
| Study plan | Video watch-order spreadsheet and the missing-topics addendum PDF | [da-2027/study-plan](da-2027/study-plan/) |
| Later Learning | 37 films and a 77-page handbook PDF beyond the syllabus | [da-2027/later-learning](da-2027/later-learning/README.md) |
| Film tooling | Drawing helpers, line tracer, build driver, commented lab code | [da-2027/shared-film-tools](da-2027/shared-film-tools/) |

## Later Learning topics (beyond GATE)

Advanced DSA (range queries, balanced trees, graphs, flow, advanced DP, strings, number theory), deep learning,
transformers and LLMs, NLP and retrieval, reinforcement learning, generative models, geometric deep learning,
optimisation, Bayesian methods, causality and game theory, state space models, boosting and kernels,
advanced linear algebra, probability, statistics, calculus optimisation, MLOps, data engineering, system design,
ML security, neuromorphic computing, and LeetCode patterns (hashing, windows, trees, graphs, DP, backtracking).

## How to use it

1. Watch the 13 core films in the order of the watch-order spreadsheet.
2. Read the matching section PDF and solve its past questions.
3. After the exam, work through the Later Learning films, then use the handbook to practise the code.

## Rebuilding

PDFs: `latexmk -pdf file.tex` in each folder. Handbook: `xelatex` on
[the handbook source](da-2027/later-learning/handbook/Operation_Gate_OutOfSyllabus_Handbook.tex).
Films are built from the scripts in each film's `source` folder with the shared tooling.

---

Older notes from the first GATE 2026 plan are kept in [operationgate.md](operationgate.md).

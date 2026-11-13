# Later Learning (out-of-syllabus) films

37 narrated Python films that go beyond the GATE DA 2027 syllabus: advanced DSA, deep learning,
generative models, linear algebra, probability, statistics, calculus optimisation and LeetCode patterns.

- `film/` - the 37 films (mp4), numbered in watch order
- `handbook/` - LaTeX source and PDF: one chapter per film, every code block run, real outputs shown
- `source/` - narration scripts, scene definitions and the verified code blocks (`codes_L.py`) used to build the films; `genpdf.py` rebuilds the handbook (`xelatex` on the generated `.tex`)

Every code block was executed, and the output shown on screen is the real output.
The build scripts expect the film toolkit from `../shared-film-tools` and use absolute paths from the author's workspace (`/home/claude/films`), so adjust those first when rebuilding.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Conversor simples de README.ipynb para README.md e README.py

- Concatena células Markdown do notebook para gerar o Markdown.
- Gera um README.py com o conteúdo markdown comentado (estilo já usado neste projeto).

Uso:
    python convert_ipynb_to_md_and_py.py
"""

import json
from pathlib import Path

NB_PATH = Path("README.ipynb")
MD_PATH = Path("README.md")
PY_PATH = Path("README.py")


def load_nb(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_md(cells, path: Path):
    parts = []
    for cell in cells:
        if cell.get("cell_type") == "markdown":
            parts.append("".join(cell.get("source", [])))
    text = "\n".join(parts).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")


def write_py(cells, path: Path):
    lines = []
    for cell in cells:
        if cell.get("cell_type") == "markdown":
            src = "".join(cell.get("source", [])).splitlines()
            for line in src:
                lines.append(f"# {line}" if line else "#")
        # células de código não são esperadas neste README, mas se houver, comentamos também
        elif cell.get("cell_type") == "code":
            src = cell.get("source", [])
            if src:
                lines.append("# ```python")
                for line in src:
                    for sub in line.splitlines():
                        lines.append(f"# {sub}")
                lines.append("# ```")
        # separador visual entre células
        lines.append("# ")
    text = "\n".join(lines).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")


def main():
    if not NB_PATH.exists():
        raise SystemExit("README.ipynb não encontrado.")
    nb = load_nb(NB_PATH)
    cells = nb.get("cells", [])
    write_md(cells, MD_PATH)
    write_py(cells, PY_PATH)
    print("Conversão concluída: README.md e README.py atualizados.")


if __name__ == "__main__":
    main()


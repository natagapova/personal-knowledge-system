"""
Generate a portfolio diagram for Personal Knowledge System.

Run:
    pip install matplotlib
    python scripts/generate_portfolio_image.py

Output:
    assets/pks_portfolio.png  (16:10)
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUTPUT = Path(__file__).resolve().parent.parent / "assets" / "pks_portfolio.png"

BG = "#0f1419"
BOX = "#1a2332"
BORDER = "#3d8bfd"
TEXT = "#e6edf3"
SUBTEXT = "#8b949e"
ACCENT = "#58a6ff"

ASPECT_W, ASPECT_H = 16, 10


def draw_box(ax, x, y, w, h, title, subtitle=None):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        facecolor=BOX,
        edgecolor=BORDER,
        linewidth=1.5,
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2,
        y + h * 0.62,
        title,
        ha="center",
        va="center",
        fontsize=11,
        color=TEXT,
        fontweight="bold",
    )
    if subtitle:
        ax.text(
            x + w / 2,
            y + h * 0.28,
            subtitle,
            ha="center",
            va="center",
            fontsize=8,
            color=SUBTEXT,
        )


def draw_arrow(ax, x1, y1, x2, y2):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=12,
            color=ACCENT,
            linewidth=1.5,
        )
    )


def main():
    fig, ax = plt.subplots(figsize=(ASPECT_W, ASPECT_H), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, ASPECT_W)
    ax.set_ylim(0, ASPECT_H)
    ax.axis("off")

    ax.text(
        ASPECT_W / 2,
        9.1,
        "Personal Knowledge System",
        ha="center",
        fontsize=24,
        color=TEXT,
        fontweight="bold",
    )
    ax.text(
        ASPECT_W / 2,
        8.45,
        "RAG pipeline over personal PDFs  ·  Python · ChromaDB · Ollama",
        ha="center",
        fontsize=11,
        color=SUBTEXT,
    )

    box_w, box_h = 1.85, 1.25
    pipeline_y = 5.0
    pipeline = [
        (0.5, "PDF files", "data/"),
        (2.75, "Load & chunk", "pdf_loader · text_chunker"),
        (5.0, "Embeddings", "sentence-transformers"),
        (7.25, "Vector DB", "ChromaDB + metadata"),
        (9.5, "Search", "semantic retrieval"),
        (11.75, "LLM", "Ollama llama3.2"),
        (14.0, "Answer", "summary + sources"),
    ]

    for x, title, subtitle in pipeline:
        draw_box(ax, x, pipeline_y, box_w, box_h, title, subtitle)

    for i in range(len(pipeline) - 1):
        x1 = pipeline[i][0] + box_w
        x2 = pipeline[i + 1][0]
        mid_y = pipeline_y + box_h / 2
        draw_arrow(ax, x1 + 0.06, mid_y, x2 - 0.06, mid_y)

    draw_box(ax, 5.4, 2.6, 5.2, 1.05, "User scope", "1 · one file  |  2 · whole folder")
    draw_arrow(ax, ASPECT_W / 2, 3.65, ASPECT_W / 2, pipeline_y - 0.05)
    ax.text(ASPECT_W / 2 + 0.35, 4.35, "where filter", fontsize=8, color=ACCENT)

    ax.text(
        ASPECT_W / 2,
        1.35,
        "citations (filename + page)   ·   multi-PDF index   ·   built without LangChain",
        ha="center",
        fontsize=10,
        color=SUBTEXT,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT, dpi=150, facecolor=BG, bbox_inches="tight")
    plt.close()
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()

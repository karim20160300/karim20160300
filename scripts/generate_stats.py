"""Generate themed GitHub stats SVGs for the profile README.
Runs inside GitHub Actions using the built-in GITHUB_TOKEN. Standard library only."""
import json, os, sys, urllib.request
from html import escape

USER = os.environ.get("GH_USER", "karim20160300")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT_DIR", "assets/generated")

BG1, BG2, TEXT, MUTED = "#0b0f1a", "#160f26", "#e6edf3", "#8b9bb4"
ACCENTS = ["#ff2d55", "#ff7a59", "#ffd166", "#42d392", "#4cc9f0", "#a78bfa"]
FONT = "Segoe UI,Helvetica,Arial,sans-serif"

QUERY = """
query($login: String!) {
  user(login: $login) {
    name
    followers { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar { totalContributions }
    }
    repositories(ownerAffiliations: OWNER, isFork: false, first: 100, privacy: PUBLIC) {
      totalCount
      nodes {
        stargazerCount
        forkCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}"""


def fetch():
    if not TOKEN:
        sys.exit("GITHUB_TOKEN is not set")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    u = data["data"]["user"]
    repos = u["repositories"]["nodes"]
    langs = {}
    for repo in repos:
        for e in repo["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    c = u["contributionsCollection"]
    return {
        "stats": [
            ("Public repos", u["repositories"]["totalCount"]),
            ("Contributions (1y)", c["contributionCalendar"]["totalContributions"]),
            ("Commits (1y)", c["totalCommitContributions"]),
            ("Pull requests (1y)", c["totalPullRequestContributions"]),
            ("Stars earned", sum(r["stargazerCount"] for r in repos)),
            ("Followers", u["followers"]["totalCount"]),
        ],
        "langs": sorted(langs.items(), key=lambda x: -x[1])[:6],
    }


def frame(w, h, title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient></defs>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="url(#bg)" stroke="#ff2d55" stroke-opacity=".45" stroke-width="2"/>
<text x="28" y="42" font-family="{FONT}" font-size="20" font-weight="700" fill="{ACCENTS[0]}">{escape(title)}</text>
{body}
</svg>"""


def stats_svg(stats):
    rows = []
    for i, (label, value) in enumerate(stats):
        col, row = i % 2, i // 2
        x, y = 28 + col * 210, 90 + row * 62
        c = ACCENTS[i % len(ACCENTS)]
        start = round(i / 8, 2)
        rows.append(
            f'<g><animate attributeName="opacity" values="0;0;1" keyTimes="0;{start};1" dur="1.2s" fill="freeze"/>'
            f'<rect x="{x}" y="{y-26}" width="4" height="44" rx="2" fill="{c}"/>'
            f'<text x="{x+16}" y="{y}" font-family="{FONT}" font-size="24" font-weight="800" fill="{TEXT}">{value:,}</text>'
            f'<text x="{x+16}" y="{y+18}" font-family="{FONT}" font-size="13" fill="{MUTED}">{escape(label)}</text></g>'
        )
    return frame(460, 290, "GitHub stats", "".join(rows))


def langs_svg(langs):
    total = sum(s for _, s in langs) or 1
    bar, x = [], 28
    for i, (_, size) in enumerate(langs):
        w = max(size / total * 404, 2)
        bar.append(f'<rect x="{x:.1f}" y="66" width="{w:.1f}" height="12" fill="{ACCENTS[i]}"/>')
        x += w
    items = []
    for i, (name, size) in enumerate(langs):
        col, row = i % 2, i // 2
        ix, iy = 28 + col * 210, 120 + row * 50
        pct = size / total * 100
        items.append(
            f'<circle cx="{ix+6}" cy="{iy-5}" r="6" fill="{ACCENTS[i]}"/>'
            f'<text x="{ix+20}" y="{iy}" font-family="{FONT}" font-size="15" font-weight="600" fill="{TEXT}">{escape(name)}</text>'
            f'<text x="{ix+20}" y="{iy+18}" font-family="{FONT}" font-size="13" fill="{MUTED}">{pct:.1f}%</text>'
        )
    body = (
        '<clipPath id="r"><rect x="28" y="66" width="404" height="12" rx="6"/></clipPath>'
        f'<g clip-path="url(#r)">{"".join(bar)}</g>' + "".join(items)
    )
    return frame(460, 290, "Top languages", body)


def main():
    data = fetch()
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/stats.svg", "w") as f:
        f.write(stats_svg(data["stats"]))
    with open(f"{OUT}/languages.svg", "w") as f:
        f.write(langs_svg(data["langs"]))
    print("Generated", OUT)


if __name__ == "__main__":
    main()

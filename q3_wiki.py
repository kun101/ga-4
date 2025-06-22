from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

# Enable CORS for all origins and GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"

def extract_headings(html: str) -> str:
    """
    Extract H1-H6 headings from HTML and generate Markdown outline.
    """
    soup = BeautifulSoup(html, "lxml")

    # Extract the main title (usually H1)
    title_tag = soup.find("h1", id="firstHeading")
    title = title_tag.text.strip() if title_tag else "Country"

    # Find all headings H1 to H6 in order in the content text
    content_div = soup.find("div", id="mw-content-text")
    if not content_div:
        return f"# {title}\n\n*No content found*"

    headings = content_div.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    # Start building markdown outline
    md_lines = ["## Contents\n", f"# {title}\n"]

    for h in headings:
        # Extract heading level from tag name
        level = int(h.name[1])
        # Create markdown heading with same level (# = 1, ## = 2, etc)
        # Adjust levels so top-level heading is #
        # Wikipedia H1 is usually page title, so here H2 maps to ##
        # We'll just map heading level directly to '#' repeated level

        # To make sure # is at least one, and max 6
        hashes = "#" * level
        text = h.get_text(strip=True)

        # Sometimes headings may be empty or too short; skip if so
        if not text or len(text) < 2:
            continue

        md_lines.append(f"{hashes} {text}\n")

    return "\n".join(md_lines)

@app.get("/api/outline")
async def get_country_outline(country: str = Query(..., description="Country name to fetch outline for")):
    # Construct Wikipedia URL (replace spaces with underscores)
    country_url = WIKI_BASE_URL + country.replace(" ", "_")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(country_url, timeout=10.0)
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=404, detail=f"Wikipedia page for '{country}' not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching Wikipedia page: {e}")

    markdown_outline = extract_headings(response.text)

    return {"country": country, "outline": markdown_outline}

# Install dependencies:
# pip install fastapi uvicorn httpx beautifulsoup4 lxml
# Run the FastAPI app with: uvicorn q3_wiki:app --reload
# Submit : http://localhost:8000/api/outline

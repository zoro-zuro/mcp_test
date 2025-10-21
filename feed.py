import feedparser
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "Feed Capturer")

@mcp.tool()
def capture_feed(query: str, max_entries:int =3) -> list:
  """ Capture Rss feed entries from freecodecamp.org based on a search query."""
  feed_url = f"https://www.freecodecamp.org/news/rss"
  query = query.lower()
  result = []
  for entry in feedparser.parse(feed_url).entries:
    title = entry.get("title", "").lower()
    description = entry.get("description", "").lower()
    if query in title or query in description:
      result.append({
        "title": entry.get("title", ""),
        "link": entry.get("link", ""),
        "published": entry.get("published", ""),
        "summary": entry.get("summary", "")
      })
      if len(result) >= max_entries:
        break

  return result

@mcp.tool()
def search_youtube(query:str,max_results:int=3) -> list:
  """ Search YouTube for videos matching the query."""
  feed = feedparser.parse(f"https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")
  query = query.lower()
  results = []
  for entry in feed.entries:
    title = entry.get("title", "").lower()
    if query in title:
      results.append({
        "title": entry.get("title", ""),
        "link": entry.get("link", ""),
        "published": entry.get("published", "")
      })
      if len(results) >= max_results:
        break

  return results

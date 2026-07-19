from duckduckgo_search import DDGS


def get_live_news_context(sport_name):
    query = f"{sport_name} latest tournament results championship winners news"

    news = []

    try:
        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=5
            )

            for result in results:

                title = result.get("title", "")
                body = result.get("body", "")

                if title and body:
                    news.append(
                        f"Title: {title}\nNews: {body}"
                    )

    except Exception as e:

        print("DuckDuckGo Error:", e)

        return f"Search Error: {e}"

    if news:

        return "\n\n".join(news)

    return "No live news found."
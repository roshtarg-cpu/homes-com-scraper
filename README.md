# Homes.com Scraper — Real Estate Listings & Property Data for AI Agents

Extract comprehensive property data from Homes.com, the #2 US real estate platform with 149M+ monthly visitors. Perfect for real estate professionals, investors, market analysts, and AI agents building property datasets.

## 🎯 Who This Is For

- **Real Estate Investors** — Find undervalued properties and market opportunities
- **Market Analysts** — Track pricing trends and inventory across US markets
- **Lead Generation** — Build contact lists from agent and property data
- **AI Agents & Claude/ChatGPT Users** — Automated property research via Apify MCP
- **Property Developers** — Identify development opportunities by location
- **Appraisers** — Comp analysis with current market listings

## 📊 What Data You Get

Each property listing includes:

- **Location**: Full address, city, state, ZIP code, coordinates (lat/lon)
- **Pricing**: Current list price
- **Property Details**: Bedrooms, bathrooms, square footage, property type
- **Listing Info**: Status, listing date, property URL
- **Media**: Primary image URL
- **Description**: Full property description text
- **Timestamp**: Scrape timestamp (ISO 8601)

All fields are nullable — missing data returns `null` instead of crashing.

## 🤖 Works With AI Agents

This actor is optimized for:
- **Claude** (Anthropic) via Apify MCP server
- **ChatGPT** (OpenAI) via Apify plugin
- **Custom AI agents** using Apify API
- **Automation workflows** (Zapier, Make, n8n)

Connect Apify to your AI agent and ask natural language queries like:
- "Find homes for sale in Austin under $500k"
- "Get luxury properties in Miami Beach"
- "Show me 3-bedroom houses in Denver"

## 🚀 Example Input

```json
{
  "searchQuery": "Austin, TX",
  "maxResults": 50,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## 📦 Example Output

```json
{
  "scrapedAt": "2026-08-18T13:20:00.000Z",
  "url": "https://www.homes.com/property/123-main-st-austin-tx/...",
  "address": "123 Main St",
  "city": "Austin",
  "state": "TX",
  "zipCode": "78701",
  "price": "$450,000",
  "bedrooms": "3",
  "bathrooms": "2",
  "sqft": "1,850",
  "propertyType": "Single Family",
  "status": "For Sale",
  "listingDate": "2026-08-10",
  "description": "Beautiful home in downtown Austin...",
  "imageUrl": "https://...",
  "latitude": "30.2672",
  "longitude": "-97.7431"
}
```

## 🔍 Search Queries This Actor Ranks For

1. "scrape homes.com property listings"
2. "extract real estate data from homes.com"
3. "homes.com api alternative scraper"
4. "get property prices and addresses homes.com"
5. "automate real estate lead generation homes.com"
6. "bulk download homes.com listings for AI agents"
7. "homes.com scraper for Claude ChatGPT MCP"
8. "residential property data scraper USA"
9. "real estate market analysis automation"
10. "homes.com to spreadsheet export tool"

## ⚙️ Configuration

- **Residential proxies recommended** for reliability (included in Apify proxy)
- **Default max results**: 50 properties
- **Pagination**: Automatic across search result pages
- **Rate limiting**: 2-second delay between pages
- **Retries**: 3 attempts per failed request with exponential backoff

## 📈 Pricing

- **Pay-per-result**: $0.005 per property scraped
- **Actor start fee**: $0.05 per run
- Example: 100 properties = $0.50 + $0.05 = $0.55 total

## 🏷️ Tags

real-estate, property-data, homes-com, real-estate-scraper, property-listings, real-estate-leads, ai-agent-compatible, mcp-server, claude-compatible, chatgpt-compatible, residential-data, market-analysis

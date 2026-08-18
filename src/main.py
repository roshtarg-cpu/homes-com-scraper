from apify import Actor
from .utils import _fetch
from .parser import parse_listings
import asyncio

async def main():
    async with Actor:
        # Get input
        actor_input = await Actor.get_input() or {}
        search_query = actor_input.get('searchQuery', 'San Francisco, CA')
        max_results = actor_input.get('maxResults', 50)
        proxy_config = actor_input.get('proxyConfiguration', {})
        
        Actor.log.info(f'Starting Homes.com scraper for: {search_query}')
        Actor.log.info(f'Max results: {max_results}')
        
        # Build proxy URL
        proxy_url = None
        if proxy_config:
            groups = proxy_config.get('useApifyProxy') and proxy_config.get('apifyProxyGroups', ['RESIDENTIAL'])
            if groups:
                group = groups[0]
                proxy_url = f"http://auto:{Actor.config.proxy_password}@proxy.apify.com:8000"
                if group != 'RESIDENTIAL':
                    proxy_url = proxy_url.replace('auto', f'groups-{group}')
        
        results_count = 0
        page_num = 1
        
        while results_count < max_results:
            # Build search URL with pagination
            offset = (page_num - 1) * 50
            search_url = f"https://www.homes.com/for-sale/?q={search_query.replace(' ', '%20')}&offset={offset}"
            
            Actor.log.info(f'Fetching page {page_num}: {search_url}')
            
            # Fetch with retries
            html = None
            for attempt in range(3):
                try:
                    html = await _fetch(search_url, proxy_url)
                    if html:
                        break
                    Actor.log.warning(f'Attempt {attempt + 1}/3 returned empty content')
                    await asyncio.sleep(2 ** attempt)
                except Exception as e:
                    Actor.log.error(f'Attempt {attempt + 1}/3 failed: {e}')
                    if attempt < 2:
                        await asyncio.sleep(2 ** attempt)
            
            if not html:
                Actor.log.error(f'Failed to fetch page {page_num} after 3 attempts')
                break
            
            # Parse listings
            listings = parse_listings(html)
            
            if not listings:
                Actor.log.warning(f'No listings found on page {page_num}, stopping pagination')
                break
            
            Actor.log.info(f'Found {len(listings)} listings on page {page_num}')
            
            # Push results immediately
            for listing in listings:
                if results_count >= max_results:
                    break
                await Actor.push_data(listing)
                results_count += 1
            
            # Log progress every 10 results
            if results_count % 10 == 0:
                Actor.log.info(f'Progress: {results_count}/{max_results} results scraped')
            
            # Check if we should continue
            if results_count >= max_results:
                break
            
            if len(listings) < 10:
                Actor.log.info('Fewer than 10 listings on page, likely end of results')
                break
            
            page_num += 1
            await asyncio.sleep(2)  # Rate limiting
        
        Actor.log.info(f'Scraping completed. Total results: {results_count}')

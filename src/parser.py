from bs4 import BeautifulSoup
from datetime import datetime, timezone

def parse_listings(html):
    """Extract property listings from Homes.com HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    listings = []
    
    # Find all property cards - adjust selectors based on actual site structure
    cards = soup.find_all(['div', 'article'], class_=lambda x: x and ('property' in x.lower() or 'listing' in x.lower() or 'card' in x.lower()))
    
    if not cards:
        # Fallback: try to find any links with property URLs
        cards = soup.find_all('a', href=lambda x: x and '/property/' in x)
    
    for card in cards[:50]:  # Limit per page
        try:
            listing = {
                'scrapedAt': datetime.now(timezone.utc).isoformat(),
                'url': None,
                'address': None,
                'city': None,
                'state': None,
                'zipCode': None,
                'price': None,
                'bedrooms': None,
                'bathrooms': None,
                'sqft': None,
                'propertyType': None,
                'status': None,
                'listingDate': None,
                'description': None,
                'imageUrl': None,
                'latitude': None,
                'longitude': None,
            }
            
            # Extract URL
            link = card.find('a', href=True)
            if link:
                href = link['href']
                if href.startswith('/'):
                    listing['url'] = f"https://www.homes.com{href}"
                else:
                    listing['url'] = href
            
            # Extract address
            address_elem = card.find(['h2', 'h3', 'div'], class_=lambda x: x and 'address' in x.lower())
            if address_elem:
                listing['address'] = address_elem.get_text(strip=True)
            
            # Extract price
            price_elem = card.find(['span', 'div'], class_=lambda x: x and 'price' in x.lower())
            if price_elem:
                listing['price'] = price_elem.get_text(strip=True)
            
            # Extract bedrooms
            bed_elem = card.find(text=lambda x: x and ('bed' in x.lower() or 'bd' in x.lower()))
            if bed_elem:
                listing['bedrooms'] = bed_elem.strip()
            
            # Extract bathrooms
            bath_elem = card.find(text=lambda x: x and ('bath' in x.lower() or 'ba' in x.lower()))
            if bath_elem:
                listing['bathrooms'] = bath_elem.strip()
            
            # Extract square footage
            sqft_elem = card.find(text=lambda x: x and 'sqft' in x.lower())
            if sqft_elem:
                listing['sqft'] = sqft_elem.strip()
            
            # Extract image
            img = card.find('img', src=True)
            if img:
                listing['imageUrl'] = img['src']
            
            # Only add if we have at least URL or address
            if listing['url'] or listing['address']:
                listings.append(listing)
        except Exception as e:
            print(f"Error parsing listing: {e}")
            continue
    
    return listings

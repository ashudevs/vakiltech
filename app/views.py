import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScrapedData
from .serializers import ScrapedDataSerializer

@api_view(['POST'])
def scrape_data(request):
    url = request.data.get('url')
    if not url:
        return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Define column names you want to extract
    column_names = ['Column1', 'Column2', 'Column3']  # Modify with actual column names

    # Find the table element
    table = soup.find('table')
    if table:
        # Extract data from the table
        table_data = []
        rows = table.find_all('tr')
        for row in rows:
            row_data = {}
            cells = row.find_all(['th', 'td'])
            for i, cell in enumerate(cells):
                # Check if the current column index is within the defined column names
                if i < len(column_names):
                    row_data[column_names[i]] = cell.get_text(strip=True)
            if row_data:  # Ensure row_data is not empty (skips header row)
                table_data.append(row_data)
    else:
        table_data = None

    title = soup.title.string if soup.title else 'No title'
    content = soup.get_text()

    # Save scraped data including table data
    scraped_data = ScrapedData(url=url, title=title, content=content)
    scraped_data.save()

    # Attach table_data to the scraped_data instance
    scraped_data.table_data = table_data
    scraped_data.save()

    serializer = ScrapedDataSerializer(scraped_data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)







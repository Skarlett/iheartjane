from algoliasearch.configs import SearchConfig
from algoliasearch.search_client import SearchClient
import json

STORE_ID = 1234

# check http headers to get your variant of API-ID, and API-KEY
config = SearchConfig('VFM4X0N23A', 'b499e29eb7542dc373ec0254e007205d')

# don't be suspicious
config.headers['User-Agent'] = 'Algolia for JavaScript (4.13.0); Browser; JS Helper (3.7.4); react (16.14.0); react-instantsearch (6.23.1)'

client = SearchClient.create_with_config(config)
index = client.init_index('menu-products-production')

# empty query returns everything
# limited to 1000 hits
# only worth scraping 24h - 3d
results = index.search("", {
         "filters": f"store_id:{STORE_ID}",
         "hitsPerPage":"1000"
     }
)

with open("response.json", "w") as fd:
    fd.write(json.dumps(results, indent=4))

print('OK')

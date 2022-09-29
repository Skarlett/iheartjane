#!/usr/bin/env python
from algoliasearch.configs import SearchConfig
from algoliasearch.search_client import SearchClient
import json
import fire

def main(
        filter="store_id:2877",
        hits=1000,
        index="menu-products-production",
        useragent='Algolia for JavaScript (4.13.0);' \
            'Browser; JS Helper (3.7.4);' \
            'react (16.14.0); react-instantsearch (6.23.1)',
        algolia_id="VFM4X0N23A",
        algolia_key='b499e29eb7542dc373ec0254e007205d'
):
        # check http headers to get your variant of API-ID, and API-KEY
        config = SearchConfig('VFM4X0N23A', 'b499e29eb7542dc373ec0254e007205d')
        # don't be suspicious
        config.headers['User-Agent'] = 'Algolia for JavaScript (4.13.0); Browser; JS Helper (3.7.4); react (16.14.0); react-instantsearch (6.23.1)'
        client = SearchClient.create_with_config(config)

        index = client.init_index('menu-products-production')

        results = index.search("", {
                "filters": filter,
                "hitsPerPage":"1000"
        })

        print(json.dumps(results, indent=4))

if __name__ == '__main__':
    fire.Fire(main)

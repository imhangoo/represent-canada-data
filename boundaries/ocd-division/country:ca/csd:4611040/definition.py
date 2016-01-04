from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Winnipeg wards',
    domain='Winnipeg, MB',
    last_updated=date(2015, 10, 3),
    name_func=boundaries.clean_attr('Name'),
    id_func=lambda f: int(f.get('Number')),
    authority='City of Winnipeg',
    source_url='https://data.winnipeg.ca/Council-Services/Electoral-Ward/ede3-teb8',
    licence_url='https://data.winnipeg.ca/open-data-licence',
    data_url='https://data.winnipeg.ca/api/geospatial/ede3-teb8?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4611040'},
)
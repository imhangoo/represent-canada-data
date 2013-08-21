from datetime import date

import boundaries

boundaries.register('North Dumfries wards',
    domain='North Dumfries, ON',
    last_updated=date(2012, 5, 14),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardNumber'),
    authority='Region of Waterloo',
    source_url='http://www.regionofwaterloo.ca/en/regionalGovernment/WardBoundaries.asp',
    licence_url='http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
    data_url='http://www.regionofwaterloo.ca/opendatadownloads/WardBoundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3530004'},
    ogr2ogr='''-where "Municipali='North Dumfries'"''',
)

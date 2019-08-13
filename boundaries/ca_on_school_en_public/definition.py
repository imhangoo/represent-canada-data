from datetime import date

import boundaries

boundaries.register('Ontario English Public School Board',
    domain='Canada',
    last_updated=date(2016, 11, 8),
    name_func=boundaries.attr('CDNAME'),
    id_func=boundaries.attr('CDUID'),
    slug_func=boundaries.attr('CDUID'),
    authority='Ontario Council of University Libraries',
    source_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries',
    licence_url='http://geo2.scholarsportal.info/tou.html#terms',
    data_url='http://geo.scholarsportal.info/#r/details/_uri@=1011603538$OpenContent_LIO_SchoolBoard_EP_2016&_add:true_nozoom:true',
    encoding='utf-8',
)

#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Beaconsfield districts',
    domain=u'Beaconsfield, QC',
    file='Beaconsfield.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466107',
)

boundaries.register(u'Cote-Saint-Luc districts',
    domain=u'Cote-Saint-Luc, QC',
    file='Cote-Saint-Luc.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466058',
)

boundaries.register(u'Dollard-des-Ormeaux districts',
    domain=u'Dollard-des-Ormeaux, QC',
    file='Dollard-des-Ormeaux.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466142',
)

boundaries.register(u'Dorval districts',
    domain=u'Dorval, QC',
    file='Dorval.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466087',
)

boundaries.register(u'Kirkland districts',
    domain=u'Kirkland, QC',
    file='Kirkland.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466102',
)

boundaries.register(u'Montréal-Est districts',
    domain=u'Montréal-Est, QC',
    file='Montreal-Est.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466007',
)

boundaries.register(u'Pointe-Claire districts',
    domain=u'Pointe-Claire, QC',
    file='Pointe-Claire.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466097',
)

boundaries.register(u'Sainte-Anne-de-Bellevue districts',
    domain=u'Sainte-Anne-de-Bellevue, QC',
    file='Sainte-Anne-de-Bellevue.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466117',
)

boundaries.register(u'Senneville districts',
    domain=u'Senneville, QC',
    file='Senneville.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466127',
)

boundaries.register(u'Westmount districts',
    domain=u'Westmount, QC',
    file='Westmount.shp',
    last_updated=date(2013, 2, 4),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    geographic_code='2466032',
)

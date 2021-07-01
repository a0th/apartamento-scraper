# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import json


# %%
zap_apartamentos_api_dump = json.load(open('zap_apartamentos_api_dump.json'))


# %%
len(zap_apartamentos_api_dump)


# %%
data_raw = pd.json_normalize(zap_apartamentos_api_dump)


# %%
data = pd.DataFrame()


# %%
data_raw.head(10)#['usableAreas'].str.get(0)


# %%
data['area_util'] = data_raw['listing.usableAreas'].str.get(0)
data['data_de_criacao'] = data_raw['listing.createdAt']
data['ultima_atualizacao'] = data_raw['listing.updatedAt']
data['andares'] = data_raw['listing.floors'].str.get(0)
data['id'] = data_raw['listing.id']
data['vagas_estacionamento'] = data_raw['listing.parkingSpaces'].str.get(0)
data['suites'] = data_raw['listing.suites'].str.get(0)
data['banheiros'] = data_raw['listing.bathrooms'].str.get(0)
data['quartos'] = data_raw['listing.bedrooms'].str.get(0)
data['iptu_anual'] = data_raw['listing.pricingInfos'].str.get(0).str.get('yearlyIptu')
data['condominio'] = data_raw['listing.pricingInfos'].str.get(0).str.get('monthlyCondoFee')
data['aluguel_mensal_total'] = data_raw['listing.pricingInfos'].str.get(0).str.get('rentalInfo').str.get('monthlyRentalTotalPrice')
data['cep'] = data_raw['listing.address.zipCode']
data['longitude'] = data_raw['listing.address.point.lon']
data['latitude'] = data_raw['listing.address.point.lat']


# %%
data['id'].value_counts().value_counts()


# %%
data = data.drop_duplicates('id')


# %%
import matplotlib.pyplot as plt


# %%
data[['area_util','aluguel_mensal_total']].astype(float).plot(kind='scatter',x='area_util',y='aluguel_mensal_total')


# %%
data.to_csv('zap_imoveis.csv',index=False)


# %%
data.latitude



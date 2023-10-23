from pymongo.mongo_client import MongoClient
sector_names = ['technology', 'health', 'finance', 'consumer_discretionary', 'industrial', 'cosumer_staples',
                'energy', 'utility', 'real_estate', 'commodities', 's_p']

def delete_data(sector_names):
    uri = 'mongodb+srv://jmetzg11:G3Ql9orCKrrZ1eKF@stocks.gqzzrrh.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(uri)
    db = client['stocks']
    for sector in sector_names:
        collection = db[sector]
        result = collection.delete_many({})
        print(f'Deleted {result.deleted_count} documents')

# delete_data(sector_names)
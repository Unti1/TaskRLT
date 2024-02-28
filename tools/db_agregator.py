from settings import *

async def aggregate_salaries(dt_from, dt_upto, group_type):
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client.MyDB
    collection = db.sample_collection
    
    # Преобразование типа агрегации в формат MongoDB
    group_format = '%Y-%m-%dT%H' if group_type == 'hour' else '%Y-%m-%d' if group_type == 'day' else '%Y-%m'
    
    pipeline = [
        {
            '$match': {
                'dt': {
                    '$gte': datetime.fromisoformat(dt_from),
                    '$lte': datetime.fromisoformat(dt_upto)
                }
            }
        },
        {
            '$group': {
                '_id': {
                    '$dateToString': {
                        'format': group_format, 'date': '$dt'
                    }
                },
                'totalAmount': {
                    '$sum': '$value'
                }
            }
        },
        {
            '$sort': {
                '_id': 1
            }
        },
        {
            '$project': {
                '_id': 0,
                'label': {
                    '$concat': [
                        '$_id', 
                        {
                            '$cond': {
                                'if': {'$eq': [group_type, 'month']},
                                'then': '-01T00:00:00',
                                'else': ''
                            }
                        }
                    ]
                },
                'totalAmount': 1
            }
        }
    ]
    
    cursor = collection.aggregate(pipeline)
    dataset = []
    labels = []
    async for doc in cursor:
        labels.append(doc['label'])
        dataset.append(doc['totalAmount'])
    
    return {'dataset': dataset, 'labels': labels}


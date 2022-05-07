import pymongo

class db:

    def __init__(self, db_url):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client["api"]
        self.col = self.db["users"]

    def __del__(self):
        """析构函数"""
        self.client.close()

    # def find(self, collect_name, *args, **kwargs):
    #     """查询所有记录"""
    #     return self.db.get_collection(collect_name).find(*args, **kwargs)

    def col_find(self, query, field):
        """查询所有记录"""
        return self.col.find(query, field)
    


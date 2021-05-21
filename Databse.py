from utility import DB, DbConfigure

# Driver Code
if __name__ == "__main__":
    config = DbConfigure()
    db = DB(server=config)
    query = '''SELECT *from EquipActivityLogs eal  '''
    data = db.query(query=query)
    print(data)
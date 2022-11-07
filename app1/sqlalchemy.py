# from sqlalchemy import create_engine
  
# # DEFINE THE DATABASE CREDENTIALS
# user = 'postgres'
# password = 'Saransh#999'
# host = 'saranshdb1.cm0pvbcyghvn.ap-south-1.rds.amazonaws.com'
# port = 5432
# database = 'postgres'
  
# # PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# # RETURN THE SQLACHEMY ENGINE OBJECT
# def get_connection():
#     return create_engine(
#         url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )
  
  
# if __name__ == '__main__':
  
#     try:
#         # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         print(
#             f"Connection to the {host} for user {user} created successfully.")
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)
        
        
# from sqlalchemy import create_engine
# engine = create_engine("postgresql://postgres:Saransh#999@saranshdb1.cm0pvbcyghvn.ap-south-1.rds.amazonaws.com:5432/saranshdb1")
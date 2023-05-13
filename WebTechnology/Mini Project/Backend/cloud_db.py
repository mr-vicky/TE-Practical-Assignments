from pymongo import MongoClient

mongo = MongoClient('mongodb+srv://sanket56:XVCvJp2vveZBvN2g@jarvis.pe42eeu.mongodb.net/?retryWrites=true&w=majority')
db = mongo.users


class CloudDB():
    
    def retrieve_user(self, email: str, password: str) -> tuple :
        try:
            result = False
            data = db.details.find_one({'email': email, 'password': password })
            if data:
                result = True
                output = "User is valid!"
            else:
                output = "User not found!"
        except Exception as e:
            output = f"Some error has occurred: {e}"
        return {'status':str(result), 'result': output }, result


    def insert_user(self, username: str, password: str, firstName: str, lastName: str, email: str) -> tuple :
        try:
            result = False
            data = db.details.find_one({'username': username })
            if data:
                output = "User already exists."
            else:
                datatoput = {}
                if firstName:
                    datatoput.update({'firstName': firstName })
                if lastName:
                    datatoput.update({'lastName': lastName })
                if username:
                    datatoput.update({'username': username })
                if email:
                    datatoput.update({'email': email })
                if password:
                    datatoput.update({'password': password })
                db.details.insert_one(datatoput)
                output = "User registered successfully."
                result = True
        except Exception as e:
            output = f"Some error has occurred: {e}"
        return {'registered':str(result), 'result': output }, result


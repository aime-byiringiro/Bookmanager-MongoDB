

from pymongo import MongoClient

from pymongo_connector import collection
from pymongo_connector import P_collection
# from pymongo_connector import pymongo

# Select the 'Book' collection




# add a publisher
def addPublisher(city, name, phone):
    results = P_collection.insert_one({'city': city, 'name': name, 'phone': name })
    print("Add successufully")
    return results
# checker if a publisher is in the database
def Publisher_chercker(publisher_name):
        results = P_collection.find_one({'name': publisher_name})   
        return results
# check if the ISBN is in the database
def ISBN_checker(ISBN_num):
        results = collection.find_one({'ISBN': ISBN_num})
        return results
    
    
# add a book using its all fields
def addBook(ISBN_num, title, year, published_by, previous_edition, price):
    results = collection.insert_one({'ISBN' : ISBN_num, 'previous_edition' : previous_edition , 'price' : price , 'published_by' : published_by, 'title' : title, 'year': year})
    print("Add successufully")
    return results

# edit a book with specif ISBN
def editBook(ISBN_num, dictionary):
    update_data = {"$set": {}}
    
    # Check if each field is present in the dictionary and add it to the update_data
    if "previous_edition" in dictionary:
        update_data["$set"]["previous_edition"] = dictionary["previous_edition"]
    
    if "price" in dictionary:
        update_data["$set"]["price"] = dictionary["price"]
    
    if "published_by" in dictionary:
        update_data["$set"]["published_by"] = dictionary["published_by"]
    
    if "title" in dictionary:
        update_data["$set"]["title"] = dictionary["title"]
    
    if "year" in dictionary:
        update_data["$set"]["year"] = dictionary["year"]

    # Perform the update
    result = collection.update_one({"ISBN": ISBN_num}, update_data)
    return result
# delete a book with a specif ISBN
def deleteBook(ISBN_num):
    results = collection.find_one_and_delete({"ISBN":ISBN_num}) 
    # results = collection.delete_one({"ISBN":ISBN_num}) 
    return results


    















def findAll():
    results = collection.find()
    return results

def findByTitle(book_title):
    results = collection.find({'title': book_title})
    return results

def findByISBN(ISBN_num):
    results = collection.find({'ISBN': ISBN_num})
    return results






def findByPublisher(publisher_name):
     
     results = collection.find({'published_by': publisher_name}) 
     return results
 
def PriceRanger(Min, Max):
    results = collection.find({'price': {"$gte": Min, "$lte": Max}})
    return results

def findByYear(year):
    results = collection.find({'year': year})
    return results

def findByTitleAndPublisher(title, publisher_name):
    results = collection.find({'title': title, 'published_by': publisher_name})
    return results
     





    

    

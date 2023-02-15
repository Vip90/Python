#!/usr/bin/env python
# coding: utf-8

# In[1]:


def load_dataset_module_userrating():
    try:
        listrows=[]
        f=open('Book-Ratings.csv','r')
        colname_detect=f.readline()
        #below section reads the data without the header and stored in the list
        valuesdata=f.readlines()
        for row in valuesdata:
            rowsdata=row.replace('"','')#replcae the inverted comma from the data
            rowsdata_1=rowsdata.replace(';',',')#replace the semicolon from the data and add a comma to distingush coloums data
            listrows.append(rowsdata_1)#stored the data in list
        listtobeused=[]#this list is being used to use only userid as a data dictionary key 
        for item in listrows:
            userid=str(item)
            listtobeused.append(item.split(','))#finds first coloumn by comma seprator
        row_as_a_dictionary = {}      
        for item in listtobeused:
            row_as_a_dictionary.setdefault(item[0], {}).update({item[1]:item[2]})
        return row_as_a_dictionary
    except IOError:
        print('File Does not Exist:Please check the file name and path')
    except:
        print('Some error has occured please Read the Implemtation report for instructions.')
    finally:
        f.close()
def load_dataset_module_bookdetails():
    try:
        listrows=[]
        f=open('Books.csv','r')
        colname_detect=f.readline()
        #below section reads the data without the header and stored in the list
        valuesdata=f.readlines()
        for row in valuesdata:
            rowsdata=row.replace('"','')#replcae the inverted comma from the data
            rowsdata_1=rowsdata.replace(';',',')#replace the semicolon from the data and add a comma to distingush coloums data
            listrows.append(rowsdata_1)#stored the data in list
        listtobeused=[]#this list is being used to use only userid as a data dictionary key 
        for item in listrows:
            userid=str(item)
            listtobeused.append(item.split(','))#finds first coloumn by comma seprator
        row_as_a_dictionary = {}       
        for item in listtobeused:
            row_as_a_dictionary.setdefault(item[0], {}).update({item[1]:item[2]})#item[o] has key which is Bokkisbn and other values has all the details of book
        return row_as_a_dictionary
    except IOError:
        print('File Does not Exist:Please check the file name and path')
    except:
        print('Some error has occured please Read the Implemtation report for instructions.')
    finally:
        f.close()

    


# In[3]:





# In[ ]:





import meraki
import csv
import os
from dotenv import load_dotenv
#extracts data from CSV and populates the clients list with it for the API call
def csvData(file, clients):

    #check file type
    type(file)
    #create a csvreader instance
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    #this is based on my data, please index your rows accordingly
    for row in csvreader:
        mac_address = row[0]
        name = row[3]
        clients.append([{'mac': mac_address, 'name': name}])



if __name__ == '__main__':

    #define API parameters
    load_dotenv(override=True, dotenv_path=".env")  # take environment variables from .env.
    # You can also go into terminal in the directory this script is running in and do export API_KEY=<your_API_key>
    api_key = os.environ.get("API_KEY")
    network_id = os.environ.get("NETWORK_ID")

    dashboard = meraki.DashboardAPI(api_key)

    #define clients list
    clients = []
    #create home directory, aka the "~"
    home_dir = os.path.expanduser("~")

    #create path variable to data
    path = home_dir + "/sample_data.csv"

    #open the file
    file = open(path)

    #call csv function to extract data
    csvData(file, clients)

    #set device policy
    device_policy = 'Normal'

    #set length of loop
    length = len(clients)

    #loop through each client and call provisionNetworkClients
    for i in range(length):
        dashboard.networks.provisionNetworkClients(network_id, clients[i], device_policy)

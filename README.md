# provisionClients-by-CSV
Use the Meraki API call, provisionNetworkClients, to provision devices using their MAC Address and a friendly name, by importing information from a CSV file.

This script uses dotenv to load environment variables. These can be added to an .env script in the same directory the python script is running in, added to configurations in an IDE like Pycharm, or exported directly from terminal. 

If using terminal use the following syntax: export MERAKI_API_KEY=<API_KEY>. 

The CSV file needs to contain the MAC Address of the device and a friendly name. Please note the row index. 

<img width="545" alt="image" src="https://github.com/mpenno23/provisionClients-by-CSV/assets/89180381/1d09515f-6042-4551-b1ee-198362bb35b2">

For example, the MAC Address field is row[0] and the name field is row[3] in this case (and in the script). You will need to manually adjust the row index for this script by editing it. 




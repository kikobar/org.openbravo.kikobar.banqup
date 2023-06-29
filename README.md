**Objective**

This Python script extracts data from Openbravo to generate a JSON invoice to submit
to the Banqup API of Unifiedpost.

**Requirements**
* Python installed on the machine running this application.
* Credentials for accessing an Openbravo 3+ instance running with the REST API enabled.
* The role in Openbravo used for the extraction/integration must have read access to 'Sales Invoices' and 'Product' via web services. 
* Credentials for accessing the Banqup API by Unifiedpost
* Add the businessPartner id to the 'Customer code' of the customer on the 'Customers & Suppliers' section of the Banqup portal - This is critical, this program requires this field to extract some parameters that only exist in the Banqup platform.

**How to run this application**

* Copy the file `config-sample.py` to `config.py`.
* Edit `config.py` with your credentials for Openbravo and Banqup.
* Run `python3 extract_invoice.py <documentNo>`, where `<documentNo>` is the human readable invoice number in Openbravo.
* The application will do the following:
  * Fetch the invoice `<documentNo>` from Openbravo.
  * Authenticate with Banqup using OAuth2, for which it will launch a webbrowser to complete the authentication. The browser will receive the response from the Banqup server including the authentication token. The user will need to 'Copy' and 'Paste' this response at the corresponding prompt in the terminal.
  * Fetch the corresponding `businessPartner` from Banqup to verify its existence and correct setup.
  * Build a JSON record for the requested invoice `<documentNo>`, which is compatible with the Banqup API format.
  * Post the invoice to the Banqup API for the creation of the corresponding invoice in Banqup.
  * Display the response from the Banqup API, confirming the success or failure of the request.
  * If the requests is successful, a new invoice will be created with status 'Draft' in the Banqup portal, so that it could be further processed on that system.

**Credits**

* This script is heavily inspired by python-billtobox-api by alexander-schillemans available at: https://github.com/alexander-schillemans/python-billtobox-api

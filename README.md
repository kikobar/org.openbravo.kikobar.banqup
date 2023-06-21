**Objective**

This project attempt to extract data from Openbravo to generate a JSON to submit
to the Banqup API of Unifiedpost.

**Requirements**
* Python installed on the machine running this application
* Credentials for accessing an Openbravo 3+ instance running with the REST API enabled
* Credentials for accessing the Banqup API by Unifiedpost

**How to run this application**
`python3 extract-invoice.py <documentNo>`

Where `<documentNo>` is the human readable invoice number in Openbravo.

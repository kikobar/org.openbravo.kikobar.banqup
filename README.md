**Objective**

This project attempt to extract data from Openbravo to generate a JSON to submit
to the Banqup API of Unifiedpost.

**Requirements**
* Python installed on the machine running this application
* Credentials for accessing an Openbravo 3+ instance running with the REST API enabled
* Credentials for accessing the Banqup API by Unifiedpost
* Add the businessPartner id to the customer code or client_debtor_number at the Banqup portal

**How to run this application**

* Copy the file `config-sample.py` to `config.py`
* Edit `config.py` with your credentials for Openbravo and Banqup
* Run `python3 extract_invoice.py <documentNo>`

Where `<documentNo>` is the human readable invoice number in Openbravo.

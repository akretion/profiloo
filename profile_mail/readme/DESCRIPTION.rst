In Odoo, there are a few quirks that are common across projects when dealing with emails.

* mail_send_copy: for an automatic BCC for the initiator of an email
* mail_outbound_static: to avoid emails being filtered as spam. Use the true email address of the server instead
  of a fake one
* mail_unique_layout: standardize the look of emails sent from Odoo
* sale_no_portal_button: hide portal button for sale orders
* mail_partial_autodelete: purge contents of sensitive emails instead of deleting them

# send-connection-request-linkedin
The Project automates sending connection requests to linkedin profiles. A use case that I can think of (and used) is sending automated connection requests to linkedin recruiters and can aid job seekers in their job search.
The arguments to the function send-connection-requets is as follows:
Input: 
* input message
* company URL from linkedin, filtered by 'hiring' (Auto search will be implemented in next version)
* number of invitations to send

![](./gifs/send-connection-requests-linkedin.gif)

## Env to run this script (after cloning)
* Install selenium
* download chromedriver and update chromedriver path in utils.py
* update your linkedin email address and password in utils.py
* see an example in lookup_dict.py and update you messages
* $ python send_connection_request_on_linkedIn.py `company name` `number of invitations to send` `number of times to scroll when hiring members are not found`
* $ python send_connection_request_on_linkedIn.py ericsson 3 2

import datetime
import os
import uuid

import requests
from requests.auth import HTTPBasicAuth


class Client:
    def __init__(self):
        self.base_url = os.environ['BASE_URL']
        self.tpaga_user = os.environ['TPAGA_USER']
        self.tpaga_pwd = os.environ['TPAGA_PWD']


    def create_payment_request(
        self,
        cost: int,
        purchase_details_url: str,
        voucher_url: str,
        order_id: str,
        terminal_id: str,
        purchase_description: str,
        user_ip_address: str
    ) -> str:

        now = datetime.datetime.now()
        expires_at = now + datetime.timedelta(days=3)
        expires_at_iso = expires_at.isoformat()
        uuid_ = str(uuid.uuid4())
        url = f'{self.base_url}create'

        data = dict(
            cost=cost,
            purchase_details_url=purchase_details_url,
            voucher_url=voucher_url,
            idempotency_token=uuid_,
            order_id=order_id,
            terminal_id=terminal_id,
            purchase_description=purchase_description,
            user_ip_address=user_ip_address,
            expires_at=expires_at_iso
        )

        response = requests.post(
            url,
            auth=HTTPBasicAuth(self.tpaga_user, self.tpaga_pwd),
            data=data,
        )
        return response.text

    
    def payment_request_confirmation(
        self,
        token: str
    ) -> str:

        url = f'{self.base_url}{token}/info' 

        response = requests.get(
            url,
            auth=HTTPBasicAuth(self.tpaga_user, self.tpaga_pwd)
        )
        return response.text


    def confirm_delivery(
        self,
        payment_request_token: str
    ) -> str:

        url = f'{self.base_url}confirm_delivery'

        data = dict(
            payment_request_token=payment_request_token
        )

        response = requests.post(
            url,
            auth=HTTPBasicAuth(self.tpaga_user, self.tpaga_pwd),
            data=data
        )
        return response.text


    def refund_payment(
        self,
        payment_request_token: str
    ) -> str:

        url = f'{self.base_url}refund'

        data = dict(
            payment_request_token=payment_request_token
        )

        response = requests.post(
            url,
            auth=HTTPBasicAuth(self.tpaga_user, self.tpaga_pwd),
            data=data
        )
        return response.text


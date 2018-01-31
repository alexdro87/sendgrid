#!/usr/bin/env python3
"""
base.py
=======
Small library for interacting with the sendgrid API
"""

__version__ = '0.0.1'


class BaseMailService:

    def __init__(self, api_key, api_version='v3',
                 default_sender=None, sender_name=None,
                 default_mail_type='text/html'):
        self.api_key = api_key
        self.api_version = api_version
        self.default_sender = default_sender
        self.sender_name = sender_name
        self.default_mail_type = default_mail_type

    @property
    def base_url(self):
        return 'https://api.sendgrid.com/{}'.format(self.api_version)

    @property
    def headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'Content-Type': 'application/json'
        }

    def _generate_send_mail_payload(self, recipients, subject, content,
                                    sender=None, mail_type=None,
                                    files=None):
        """Send a single email
        
        :param files: Tuple of (filename, type, base64encoded data)
        """

        if sender is None:
            sender = self.default_sender

        if mail_type is None:
            mail_type = self.default_mail_type

        payload = {
            'personalizations': [
                {
                    'to': [],
                    'subject': subject
                }
            ],
            "from": {
                "email": sender
            },
            'content': [
                {
                    'type': mail_type,
                    'value': content
                }
            ]
        }

        for recipient in recipients:
            payload['personalizations'][0]['to'].append(
                {
                    'email': recipient
                }
            )

        if self.sender_name is not None:
            payload['personalizations'][0]['from']['name'] = self.sender_name

        if files is not None:
            payload['attachements'] = []
            for attachement in files:
                filename, filetype, data = attachement
                payload['attachements'].append(
                    {
                        'content': data,
                        'type': filetype,
                        'filename': filename
                    }
                )

        return payload

#!/usr/bin/env python3
"""
session.py
==========
Small library for interacting with the sendgrid API
"""
import requests
import json

__version__ = 'v0.0.1'


class MailService:

    def __init__(self, api_key, api_version='v3',
                 default_sender=None, sender_name=None,
                 default_mail_type='text/html'):
        self.api_key = api_key
        self.api_version = api_version
        self.default_sender = default_sender
        self.sender_name = sender_name
        self.default_mail_type = default_mail_type

        self.session = requests.session()
        headers = {
            'Authorization': 'Bearer {}'.format(api_key),
            'Content-Type': 'application/json'
        }
        self.session.headers.update(headers)

    @property
    def base_url(self):
        return 'https://api.sendgrid.com/{}'.format(self.api_version)

    def _parse_response(self, response):
        """Do some basic errorhandling and try to parse json if any"""
        if response.status_code == requests.codes.ok:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return response.text
            else:
                response.raise_for_status()

    def _get(self, path):
        url = '{}/{}'.format(self.base_url, path)
        response = self.session.get(url).json()

        return response

    def _post(self, path, payload=None):
        """POST request"""
        url = '{}/{}'.format(self.base_url, path)

        if payload is not None:
            response = self.session.post(url, data=json.dumps(payload))
            return self._parse_response(response)
        else:
            self.session.post(url)
            return self._parse_response(response)

        return response

    def send(self, recipients, subject, content, sender=None, mail_type=None):
        """Send a single email"""

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

        print(payload)
        return self._post('mail/send', payload)

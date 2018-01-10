#!/usr/bin/env python3
"""
session.py
==========
Small library for interacting with the sendgrid API
"""
from .base import BaseMailService
import requests
import json

__version__ = 'v0.0.1'


class MailService(BaseMailService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.session = requests.session()
        self.session.headers.update(self.headers)

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

    def send(self, *args, **kwargs):
        """Synchronously send email"""
        payload = self._generate_send_mail_payload(*args, **kwargs)
        return self._post('mail/send', payload)

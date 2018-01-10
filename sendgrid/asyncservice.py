#!/usr/bin/env python3
"""
asyncservice.py
===============
Small library for interacting with the sendgrid API
"""
from .base import BaseMailService
import json
import aiohttp
import asyncio


class AsyncMailService(BaseMailService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(
            loop=loop,
            headers=self.headers
        )

    def __del__(self):
        self.session.close()

    def _parse_response(self, response):
        """Do some basic errorhandling and try to parse json if any"""
        try:
            return json.loads(response)
        except json.decoder.JSONDecodeError:
            return response

    async def _get(self, path):
        url = '{}/{}'.format(self.base_url, path)

        response_data = None
        async with self.session.get(url) as response:
            # TODO: check response status, no need to await
            response_data = await response.text()

        return self._parse_response(response_data)

    async def _post(self, path, payload=None):
        """POST request"""
        print(self.headers)
        url = '{}/{}'.format(self.base_url, path)

        response_data = None
        if payload is not None:
            async with self.session.post(url, json=payload) as response:
                response_data = await response.text()
        else:
            self.session.post(url)
            async with self.session.post(url) as response:
                response_data = await response.text()

        return self._parse_response(response_data)

    async def a_send(self, *args, **kwargs):
        """Asynchronously send email"""
        payload = self._generate_send_mail_payload(*args, **kwargs)
        return await self._post('mail/send', payload)

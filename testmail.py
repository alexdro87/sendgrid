#!/usr/bin/env python3

from sendgrid import MailService, AsyncMailService
import asyncio

API_KEY = (
    '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'
)
DEFAULT_SENDER = "hello@moorspots.com"
RECIPIENTS = ['mathijs@mortimer.nl']
SUBJECT = "Test Email"
BODY = "I love Big Bodies"


def sync_main():
    session = MailService(API_KEY, default_sender=DEFAULT_SENDER)

    print('Sending email...')
    result = session.send(RECIPIENTS, SUBJECT, BODY)
    print('Email sent, result: {}'.format(result))


async def send_email(session):
    result = await session.a_send(
        RECIPIENTS, SUBJECT, BODY.replace('Bodies', 'Async Bodies')
    )
    print('Email sent, result: {}'.format(result))


def async_main():
    """Send a test mail asynchronously"""
    session = AsyncMailService(API_KEY, default_sender=DEFAULT_SENDER)

    print('Sending async email...')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_email(session))


if __name__ == '__main__':
    # sync_main()
    print('\n\n')
    async_main()

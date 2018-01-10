#!/usr/bin/env python3

from sendgrid import MailService

API_KEY = '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'


def main():
    session = MailService(
        API_KEY,
        default_sender="hello@moorspots.com"
    )

    print('Sending email...')
    result = session.send(
        ["mathijs@mortimer.nl"],
        "My First SendGrid Email",
        "HEre's some text for the body.. go to <a href>https://www.moorspots.com</a>"
    )
    print(result)


if __name__ == '__main__':
    main()

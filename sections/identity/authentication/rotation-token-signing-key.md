---
author: Veracity
description: Describes how the key used for signing the tokens issued by the Veracity Identity provider is rotated 
---

# Rotation of the Veracity Identity (Azure AD B2C) Token Signing Key

According to security best practice we will implement a new rotation scheme for the key used to sign the tokens issued by the Veracity Identity provider (Azure AD B2C/login.veracity.com) as follows:
- The new key will be published to the metadata (https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/discovery/v2.0/keys?p=b2c_1a_signinwithadfsidp) **one month before it gets activated**. This will allow the services to pick up the new key.
- Once the new key is activated, tokens will be issued using the new key.
- A new key will be published **every 6 months**.

We do not expect this to cause issue for services as they should already handle such rotation in accordance with best practice, however, the very first time we activate a new key, we will only make it active for 1 day. When it expires, the old (the key used today) will be used again. This will allow services to detect potential issues, but get them working again (at the latest) the next day.

The first key will be:
- Published to metadata:**Sep 6, 2022**
- Set active: **Oct 11, 2022**
- Expired: **Oct 12, 2022**

If all goes well, we will start the 6 month rotation scheme as follows:
- Published to metadata: **Oct 18, 2022**
- Set active: **Nov 22, 2022**
- Expired:After **~6 months**
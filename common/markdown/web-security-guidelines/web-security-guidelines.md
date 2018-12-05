---
Title : "Web Security Guidelines"
Author: "Thomas Haugland Rudfoss"
---

## Overview

As more and more services migrate to the web it becomes increasingly important to ensure they are secure. Depending on how the service is built there are a myriad of ways to enforce security. This article describes some common principals you should follow to ensure you application is secure.

## Secure connection

HTTPS (SSL/TLS) secure connections are a great way to ensure your content is not tampered with in flight. When this is properly set up it will not only protect against attacks, but also drastically increase trust between your users and you. Having a certificate for your service tells the client that you indeed are who you claim to be. Client browsers will also surface this information by giving your website a nice padlock icon or even displaying your company name in the address bar.

![Website with a valid SSL certificate](https://veracity.azureedge.net/static/website-with-ssl-certificate.png)

In the old days of the internet aquiring and maintaining certificates was an expensive and tedious process. It also affected the speed of you application because server hardware performance was relatively poor compared to the task of encrypting data before transmission. Today these issues are pretty much gone. The overhead of encrypting a connection are pretty much non-existent thanks to improved algorithms and dedicated hardware and the price of certificates is basically [free](https://letsencrypt.org/). There are no good reasons left not to use SSL/TLS in your application.

## Never trust user input

Websites are public facing and respond to requests crafted by users. Most often these requests are done by a browser that follows the specification and send properly formatted requests, but there is nothing stopping anyone from building a malicious payload and sending it directly to your application or even tampering with your client-side javascript in order to try to gain access or steal information. When building application (and especially single-page web applications) you should follow these guidelines:

- Treat any data from the user as suspect until you sanitize and validate it. Injection attacks are still the [number 1 security threat online](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).
- Secure your REST endpoints as if they are the first contact point for your users even if you have implemented security client-side.
- Do not expose secret configuration parameters in client-side javascript.
- Remember anything your server sends out can be read by attackers.
- Obfuscation (minifying) is NOT a security mechanism. Don't trust it to hide information.

## Security Headers

Any HTTP/HTTPS response contains headers providing details about what is being sent and in some cases how to handle the response. This section describes common best-practice for using headers with web facing services like REST APIs or websites.

Note that defining these headers will not stop attackers from visiting your site, but it will greatly enhance the security of regular users using browsers that understand them.

### Content-Security-Policy

The Content-Security-Policy or CSP header defines a whitelist of sources the client may load different types of data from. For instance you can limit the client to only allow loading of script files from your own domain which will prevent many cross-site-scripting (XSS) vectors. The CSP header should be set to the most restrictive configuration you can while still allowing your website or service to operate properly. Read more about this header on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) and [OWASP](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#csp).

### Strict-Transport-Security

This header tells clients that your website supports HTTPS connections and that if the user types your address or visists your site from a link it should try to fetch it using a secure connection first. This is *not* a substitute for redirecting HTTP connections to HTTPS though as first-time users do not know of the header until they load your page. However once they have their browser will cache this information and future requests to your application will always be performed using a secure connection. Read more about this header on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security).

### X-Frame-Options

This header defines how your website can be embedded either as an iframe or other mechanisms. Most browsers will prevent pages on different domains from communicating with each other even when the page is embedded, but there are other attack vectors that may be utilized such as [clickjacking](https://en.wikipedia.org/wiki/Clickjacking) even if no communication is allowed. You should set this header as restrictive as possible for your application. Read more about this header on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options).

### X-Content-Type-Options

The `Content-Type` header describes the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the payload of a response from the server. If the header is missing the browser can attempt to "sniff" out the correct content type in order to handle the content correctly. An image should be displayed as an image while a JavaScript may execute. A problem and potential security issue occurs when the browser sniffs for the content type and ends up interpreting something as something else. Your server application should *always* report the correct content type to begin with, but the `X-Content-Type-Options` header can additionally define whether the browser should even try to sniff for content types. Read more about this header on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options).

### Referrer-Policy

When a user clicks a link on a site that takes them to another one the browser can include information about the previous site in the `Referer` (yes, it's [misspelled](https://en.wikipedia.org/wiki/HTTP_referer)) header. In some cases you may not wish to reveal where the user comes from. The `Referrer-Policy` heaader allows you to do this by restricting where the browser will add the `Referer` header. Read more about it on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy).

### X-XSS-Protection

This header controls whether the browser will attempt to protect users against cross-site-scripting (XSS) attacks. It is not respected by all browsers and covers mostly the same issues as the `Content-Security-Policy` header, but is still a useful security mechanism that should be enabled if supported. Read more about the header on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection).

### Headers that should be removed

Depending on the type of technology stack you have the default configuration may reveal unwanted information about your application. For instance expressjs will by default return the header `X-Powered-By` wich contains information about express itself potentially including the version number. This type of information could help attackers know that your system may be vulnerable and should not be surfaces if it can be avoided. You should therefore always remove these headers from your responses.

- `X-Powered-By`<br>This header usually contains information about the server software used to serve the request. This header should not be sent as it reveals information about the underlying technology stack that may be used by hackers to target your application. If you are running on an older version of software it may contain known security vulnerabilities that may be advertised to the world if this header is set.
- `Server`<br>The Server header sometimes include IPs or other identifying information for the server you are running.


## Tools and more information

There are several useful tools both online and available for download that help you detect and prevent security issues with your application. Below is a short description of some of these.

### NodeJs and Express

If you are building services using NodeJS and Express you should read their [Production Best Practices: Security](https://expressjs.com/en/advanced/best-practice-security.html) documentation. It describes many useful and relatively simple techniques that will dramatically improve the security of your application.

### Online tools

There are several useful tools online for testing whether your site conforms to common security best-practices. Try using these regularly to ensure your application follows these practices.

- [Report URI](https://report-uri.com/home/tools) contains tools for performing analysis as well as setting up security related headers.
- [securityheaders.io](https://securityheaders.io/) analyse your headers and reports whether they are conforming to security best-practices. 
- [OWASP](https://www.owasp.org/index.php/Main_Page) is a giant resource for learning about security practices and potential attack vectors. They regularly publish a [list of the most common web application security risks](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) as well as information about attacks and how to protect against them.
- [Mozilla Observatory](https://observatory.mozilla.org) is a comprehensive tool for analyzing many aspects of your website.


## Disclaimer

Veracity does not endores or promote any links within this document. Use at your own risk.

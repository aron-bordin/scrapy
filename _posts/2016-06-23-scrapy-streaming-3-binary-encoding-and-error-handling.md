---
layout: post
title: Scrapy-Streaming [3] - Binary Encoding and Error Handling
image:
  feature: feature-scrapy.jpg
date: 2016-06-23T21:08:31-04:00
---
Hi !
In the third week of the project, I implemented the from_response_request.

This allows external spiders to create a request using a response from another request.

## Binary Responses

To be able to serialize binary responses into json messages, such as images, videos, and files, I added the base64
parameter to the request message.

Now, external spiders are able to download and check binary data using scrapy streaming.

## Error Handling

I've implemented the exception message, that checks internal exceptions and sends it to the external spider.

We've two kind of issues: errors and exceptions.

Errors are raised when there are some problem in the communication channel, such as an invalid request, invalid field, and so on.

Exceptions represents problem in the Scrapy Streaming runtime, such as an invalid url to request, invalid incoming data, etc.

## Docs and PRs

This modifications have been documented in the docs PR: https://github.com/scrapy-plugins/scrapy-streaming/pull/7

And the modification in the communication channel can be found at: https://github.com/scrapy-plugins/scrapy-streaming/pull/5

## Examples

I've added new Scrapy Streaming examples here: https://github.com/scrapy-plugins/scrapy-streaming/pull/4

This examples may help new developers to implement their own spiders using any programing language, so each example shows a basic feature of Scrapy Streaming.

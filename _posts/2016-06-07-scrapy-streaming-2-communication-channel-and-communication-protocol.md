---
layout: post
title: Scrapy-Streaming [2] - Communication Channel and Communication Protocol
image:
  feature: feature-scrapy.jpg
date: 2016-06-07T00:15:52-04:00
---

Hello everyone !

In the second week of the project, I continued implementing the scrapy-streaming communication channel and started to work in the communication protocol.

## Communication Channel

The communication channel is responsible for connecting scrapy and external spiders, receiving / sending messages, validate incoming data, handle the process, etc.

I've implemented the communication validators, that are responsible for checking the the incoming messages have all required fields, valid data type, setting its default values. If any problem in the incoming message is found, a verbose information is sent to the external spider.

Also, a buffered line receiver was implemented, that receives and buffer data from the process stdout, and parse messages line by line.


## Communication Protocol

I made some advance in the communication protocol as well. I've implemented the following messages:

* **spider**: generates a new scrapy spider
* **request**: opens a new request
* **close**: close the current spider
* **log**: print something in the scrapy-streaming logger
* **response**: send request's responses
* **error**: send errors in the communication channel

PR: [https://github.com/scrapy-plugins/scrapy-streaming/pull/5](https://github.com/scrapy-plugins/scrapy-streaming/pull/5)

## Examples

I'll be adding scrapy-streaming examples while developing the project. The first example is a github spider that tracks project informations, and it's already possible to run it using the current communication protocol.

PR: [https://github.com/scrapy-plugins/scrapy-streaming/pull/4](https://github.com/scrapy-plugins/scrapy-streaming/pull/4)

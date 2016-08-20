---
layout: post
title: Scrapy-Streaming - Support for Spiders in Other Programming Languages
image:
  feature: feature-scrapy.jpg
date: 2016-08-20T14:27:41-04:00
---

This page describes the Scrapy Streaming project, the summer goals, submitted patches, and a simple overview of the results.

# About this project - Abstract

Scrapy is one of the most popular web crawling and web scraping framework. It’s written in Python and known by its good performance, simplicity, and powerful API. However, it’s only possible to write Scrapy’s Spiders using the Python Language. The goal of this project is to provide an interface that allows developers to write spiders using any programming language, using json objects to make requests, parse web contents, get data, and more. Also, a helper library will be available for Java, JS, and R.

## Scrapy Streaming

This project was named Scrapy Streaming, and it's a Scrapy's extension that provides an json layer to develop spiders using any language.

You can download and play with it in the [scrapy-plugins/scrapy-streaming](https://github.com/scrapy-plugins/scrapy-streaming) repository.


# Development

In this section, you can read an overview of the development progress and the submitted pull request related to each topic.

## Documentation

I started the Scrapy Streaming development defining the project API. writing the Communication Channel spec and writing about its usage.

I considered important to start with the project docs because it gave me some time to share my API proposal and discuss with the Scrapy developers and contributors
to get some feedback, even before starting with the development.

**Pull request**: [https://github.com/scrapy-plugins/scrapy-streaming/pull/7](https://github.com/scrapy-plugins/scrapy-streaming/pull/7)

**Documentation url**: [http://gsoc2016.readthedocs.io/](http://gsoc2016.readthedocs.io/)

## Travis and Unit Tests

Before coding, I defined the project and source code structure, adding travis, configuring codecov to check the test coverage, and implemented some initial tests.

To outcome a good project, codecov would help me to ensure to test everything under development.

**Pull request**: [https://github.com/scrapy-plugins/scrapy-streaming/pull/2](https://github.com/scrapy-plugins/scrapy-streaming/pull/2)

## Scrapy Commands

Scrapy has a [command line interface](http://doc.scrapy.org/en/latest/topics/commands.html).

The Scrapy Streaming adds the ``streaming`` command to the CLI. The ``streaming`` command allows you to execute scripts/executables as a Spider, using the following command:

    scrapy streaming my_executable -a arg1 -a arg2 -a arg3,arg4

For example, to run a R spider named ``sample.R``, you can use the following command:

    scrapy streaming Rscript -a sample.R

If you are using a scrapy project, you can also add multiple spiders. To do this, you must add a file named ``external.json`` in the project root similar to the following example:

{% highlight json %}
[
    {
      "name": "java_spider",
      "command": "java",
      "args": ["/home/user/MySpider"]
    },
    {
      "name": "compiled_spider",
      "command": "/home/user/my_executable"
    }
]
{% endhighlight %}

and then run it using the ``crawl`` command. For example:

    scrapy crawl java_spider

This definition lets you implement multiple spiders using multiple programming languages and organize them in the same project.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/3](https://github.com/scrapy-plugins/scrapy-streaming/pull/3)

## Communication Protocol

The Communication Protocol is a json API the lets any process to communicate with Scrapy, letting you develop spiders with any programming language.

This section was a bit challenging because I needed to implement a good code that supports stdin/stdout buffering, preventing user mistakes, system errors, processing performance,
scrapy problems, and spider problems.

This is the core of the project, the most important patch. So I added a lot of unit tests to ensure it's working well in both Python2 and Python3.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/5](https://github.com/scrapy-plugins/scrapy-streaming/pull/5)

## Examples

Something very important in this project is spider examples. Future users may depend on initial examples to be able to learn and use Scrapy Streaming.

I added examples in Python, R, Node.js, and Java, describing its basic usage. Also, the documentation contains a Quickstart section that provids a brief explanation about
how to use it in each programming language.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/4](https://github.com/scrapy-plugins/scrapy-streaming/pull/4)

## R package

To help the development of spiders using the R language, I implement a R package to wrap the communication channel and help developers. It contains unit tests, documentation, examples,
and it's developed using the standard R package structure.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/8](https://github.com/scrapy-plugins/scrapy-streaming/pull/8)

## Java library

To help the development of spiders using the Java language, I implement a Java library to wrap the communication channel and help developers. It contains unit tests, documentation, examples,
and it's developed using the standard Java library structure with Maven.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/9](https://github.com/scrapy-plugins/scrapy-streaming/pull/9)

## Node.js package

To help the development of spiders using the Javascript (with Node.js) language, I implement a Node package to wrap the communication channel and help developers. It contains unit tests, documentation, examples, and it's developed using the standard Node.js package structure.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/10](https://github.com/scrapy-plugins/scrapy-streaming/pull/10)

## Selectors

My initial proposal had some features called "Selectors". With selectors, you could extract data from the HTML response using css/xpath filters in the communication protocol.
This part was removed from the proposal, because this could add more complexity to the project.

I implemented a proof of concept, and I'd be happy to implement it after the summer because I consider this a very important feature to Scrapy Streaming.

**Pull request:** [https://github.com/scrapy-plugins/scrapy-streaming/pull/11](https://github.com/scrapy-plugins/scrapy-streaming/pull/11)

# WIP

Here, I highlight some topics that is not yet done.

* Publish the documentation in a official page (currently I'm using my [personal readthedocs page to store the docs](http://gsoc2016.readthedocs.io/).)
* Publish Scrapy Streaming to PIP
* Publish helper packages to the following repositories (the code is ready to be published):
    * Java -> Maven Central Repository
    * R -> CRAN
    * Node.js -> NPM
* Some pull requests requires reviews.

# Final Considerations

This summer was very good for me. I was able to develop the project and I achieved my goals with this project. Now, it's
possible and easy to implement spiders using your preferred programming language.

I received an awesome support and I'd like to thank my mentors (@eLRuLL and @ptremberth), and another GSoC student (@Preetwinder) for all the help in this project.
We've discussed a lot about its usage, best practices, and coding.

I'm a big fan of the Open Source community, so I'll be happy to continue contributing with the Scrapy Streaming repository, and some related project after this summer.

Thank you !!,

Aron Bordin.

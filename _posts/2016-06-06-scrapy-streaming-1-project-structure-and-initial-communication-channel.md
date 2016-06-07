---
layout: post
title: 'Scrapy-Streaming [1] - Project Structure and Initial Communication Channel'
image:
  feature: feature-scrapy.jpg
date: 2016-06-06T23:54:50-04:00
---


Hi !


In the first week, I implemented some initial work in the **Scrapy-Streaming** project's structure and documentation.

## Project Structure

I started defining the new project package, with **tox**, **travis**, and **codecov**.

I added two new commands to scrapy: `streaming` and `crawl`.  

The `streaming` command let you can standalone external spiders; and the `crawl` command allows you to integrate external spiders in your Scrapy's projects.


To run a standalone spider, you can use:

    scrapy streaming my_executable -a arg1 -a arg2 -a arg3,arg4

and if you want to integrate it with a scrapy project, you must create a file named ``external.json`` in the project root, similar to this example:

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

and then, you can run these spiders using:

    scrapy crawl <spider name>

These implementations were tested and pushed at: [https://github.com/scrapy-plugins/scrapy-streaming/pull/2](https://github.com/scrapy-plugins/scrapy-streaming/pull/2)

## Documentation

I've written a big part of the documentation to better define the API under development, and it can be read at: [http://gsoc2016.readthedocs.io](http://gsoc2016.readthedocs.io).

The documentation contains the whole communication channel, a simple tutorial, and descriptions about the project behavior.

Pull request: [https://github.com/scrapy-plugins/scrapy-streaming/pull/7](https://github.com/scrapy-plugins/scrapy-streaming/pull/7)


## Communication Channel

I started to work in the communication channel, defining the classes responsible for connecting external processes with scrapy, and implemented the basic message wrappers.

PR: [ https://github.com/scrapy-plugins/scrapy-streaming/pull/3
]( https://github.com/scrapy-plugins/scrapy-streaming/pull/3)

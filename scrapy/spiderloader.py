# -*- coding: utf-8 -*-
from __future__ import absolute_import

from zope.interface import implementer

from scrapy.interfaces import ISpiderLoader
from scrapy.utils.misc import walk_modules
from scrapy.utils.spider import iter_spider_classes, iter_external_spiders


@implementer(ISpiderLoader)
class SpiderLoader(object):
    """
    SpiderLoader is a class which locates and loads spiders
    in a Scrapy project.
    """
    def __init__(self, settings):
        self.spider_modules = settings.getlist('SPIDER_MODULES')
        self._spiders = {}
        self._spiders_external = {}
        self._load_all_spiders()
            
    def _load_spiders(self, module):
        for spcls in iter_spider_classes(module):
            self._spiders[spcls.name] = spcls

    def _load_all_spiders(self):
        for name in self.spider_modules:
            for module in walk_modules(name):
                self._load_spiders(module)

        required_fields = ['name', 'command']
        for spider in iter_external_spiders():
            if required_fields in spider.keys():
                raise KeyError("Each external Spider must have a name and a command")

            self._spiders_external[spider['name']] = spider

    @classmethod
    def from_settings(cls, settings):
        return cls(settings)

    def load(self, spider_name):
        """
        Return the Spider class for the given spider name. If the spider
        name is not found, raise a KeyError.
        """
        try:
            return self._spiders[spider_name]
        except KeyError:
            raise KeyError("Spider not found: {}".format(spider_name))

    def find_by_request(self, request):
        """
        Return the list of spider names that can handle the given request.
        """
        return [name for name, cls in self._spiders.items()
                if cls.handles_request(request)]

    def list(self):
        """
        Return a list with the names of all spiders available in the project.
        """
        return list(self._spiders.keys())

    def list_external(self):
        """
        Return a list with the names of all external spiders configured in external.json
        """
        return list(self._spiders_external.keys())

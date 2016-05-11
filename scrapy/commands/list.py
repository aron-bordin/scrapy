from __future__ import print_function
from scrapy.commands import ScrapyCommand

class Command(ScrapyCommand):

    requires_project = True
    default_settings = {'LOG_ENABLED': False}

    def short_desc(self):
        return "List available spiders"

    def run(self, args, opts):
        print("[Scrapy Spiders]")
        for s in sorted(self.crawler_process.spider_loader.list()):
            print(s)
        external = self.crawler_process.spider_loader.list_external()

        if external:
            print('\n[External Spiders]')
            for s in sorted(external):
                print(s)

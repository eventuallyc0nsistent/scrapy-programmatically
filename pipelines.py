from database.connection import db
from database.models import AllData

class AddTablePipeline(object):

    def process_item(self, item, spider):
        if item['title'] and item['url']:
            if 'date' not in item or not item['date']:
                date = None
            else:
                date = item['date'][0]

            record = AllData(title=item['title'][0].decode('unicode_escape'),
                             url=item['url'][0],
                             date=date)
            db.add(record)
            db.commit()
            return item

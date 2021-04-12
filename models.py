import os
from peewee import CharField, DateTimeField, Model, DoesNotExist, fn
from playhouse.postgres_ext import PostgresqlExtDatabase, JSONField
from datetime import datetime
from playhouse.db_url import connect


# CONNECT TO DB
if 'ON_HEROKU' in os.environ:
  DATABASE = connect(os.environ.get('DATABASE_URL'))
else: 
  DATABASE = PostgresqlExtDatabase('sdv_resource_calculator')



class CraftableItems(Model):
  item = CharField()
  category = CharField()
  resources = JSONField()
  img = CharField()
  created_at = DateTimeField(default=datetime.now)

  class Meta:
    database = DATABASE


data_source = [
{
	'item': 'Mayonnaise Machine',
	'category': 'Artisan Equipment',
	'resources': [
		{
			'item': 'Wood',
			'amount': 15
		},{
			'item': 'Stone',
			'amount': 15
		},{
      'item': 'Earth Crystal',
      'amount': 1
    }, {
      'item': 'Copper Bar',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/e/ef/Mayonnaise_Machine.png'
},{
  'item': 'Bee House',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 40
    },{
      'item': 'Coal',
      'amount': 8
    },{
      'item': 'Iron Bar',
      'amount': 1
    },{
      'item': 'Maple Syrup',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/c/ce/Bee_House.png'
},{
  'item': 'Preserves Jar',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 50
    },{
      'item': 'Stone',
      'amount': 40
    },{
      'item': 'Coal',
      'amount': 8
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/1/1e/Preserves_Jar.png'
},{
  'item': 'Cheese Press',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 45
    },{
      'item': 'Stone',
      'amount': 45
    },{
      'item': 'Hardwood',
      'amount': 10
    },{
      'item': 'Copper Bar ',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/7/79/Cheese_Press.png'
},{
  'item': 'Loom',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 60
    },{
      'item': 'Fiber',
      'amount': 30
    },{
      'item': 'Pine Tar',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/3/3b/Loom.png'
},{
  'item': 'Keg',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 30
    },{
      'item': 'Copper Bar',
      'amount': 1
    },{
      'item': 'Iron Bar',
      'amount': 1
    },{
      'item': 'Oak Resin',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/7/7c/Keg.png'
},{
  'item': 'Oil Maker',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Slime',
      'amount': 50
    },{
      'item': 'Hardwood',
      'amount': 20
    },{
      'item': 'Gold Bar',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/c/c5/Oil_Maker.png'
},{
  'item': 'Cask',
  'category': 'Artisan Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 20
    },{
      'item': 'Hardwood',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/7/7c/Cask.png'
},{
  'item': 'Charcoal Kiln',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 20
    },{
      'item': 'Copper Bar',
      'amount': 2
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/7/76/Charcoal_Kiln.png'
},{
  'item': 'Crystalarium',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Stone',
      'amount': 99
    },{
      'item': 'Gold Bar',
      'amount': 5
    },{
      'item': 'Iridium Bar',
      'amount': 2
    },{
      'item': 'Battery Pack',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/6/63/Crystalarium.png'
},{
  'item': 'Furnace',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Copper Ore',
      'amount': 20
    },{
      'item': 'Stone',
      'amount': 25
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/0/0f/Furnace.png'
},{
  'item': 'Lightning Rod',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Iron Bar',
      'amount': 1
    },{
      'item': 'Refined Quartz',
      'amount': 1
    },{
      'item': 'Bat Wing',
      'amount': 5
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/6/62/Lightning_Rod.png'
},{
  'item': 'Solar Panel',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Refined Quartz',
      'amount': 10
    },{
      'item': 'Iron Bar',
      'amount': 5
    },{
      'item': 'Gold Bar',
      'amount': 5
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/5/5d/Solar_Panel.png'
},{
  'item': 'Recycling Machine',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 25
    },{
      'item': 'Stone',
      'amount': 25
    },{
      'item': 'Iron Bar',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/2/26/Recycling_Machine.png'
},{
  'item': 'Seed Maker',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 25
    },{
      'item': 'Coal',
      'amount': 10
    },{
      'item': 'Gold Bar',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/1/19/Seed_Maker.png'
},{
  'item': 'Slime Incubator',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Iridium Bar',
      'amount': 2
    },{
      'item': 'Slime',
      'amount': 100
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/c/c0/Slime_Incubator.png'
},{
  'item': 'Ostrich Incubator',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Bone Fragment',
      'amount': 50
    },{
      'item': 'Hardwood',
      'amount': 50
    },{
      'item': 'Cinder Shard',
      'amount': 20
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/5/51/Ostrich_Incubator.png'
},{
  'item': 'Slime Egg-Press',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Coal',
      'amount': 25
    },{
      'item': 'Fire Quartz',
      'amount': 1
    },{
      'item': 'Battery Pack',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/7/79/Slime_Egg-Press.png'
},{
  'item': 'Tapper',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Wood',
      'amount': 40
    },{
      'item': 'Copper Bar',
      'amount': 2
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/d/da/Tapper.png'
},{
  'item': 'Heavy Tapper',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Hardwood',
      'amount': 30
    },{
      'item': 'Radioactive Bar',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/0/0c/Heavy_Tapper.png'
},{
  'item': 'Worm Bin',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Hardwood',
      'amount': 25
    },{
      'item': 'Gold Bar',
      'amount': 1
    },{
      'item': 'Iron Bar',
      'amount': 1
    },{
      'item': 'Fiber',
      'amount': 50
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/7/71/Worm_Bin.png'
},{
  'item': 'Bone Mill',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Bone Fragment',
      'amount': 10
    }, {
      'item': 'Clay',
      'amount': 3
    },{
      'item': 'Stone',
      'amount': 20
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/c/cc/Bone_Mill.png'
},{
  'item': 'Geode Crusher',
  'category': 'Refining Equipment',
  'resources': [
    {
      'item': 'Gold Bar',
      'amount': 2
    },{
      'item': 'Stone',
      'amount': 50
    },{
      'item': 'Diamond',
      'amount': 1
    }
  ],
  'img': 'https://stardewvalleywiki.com/mediawiki/images/0/02/Geode_Crusher.png'
}]


def createdb():
  num_records = (CraftableItems.select())
  if len(num_records) < len(data_source):
    for data_dict in data_source:
      CraftableItems.create(**data_dict)


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([CraftableItems], safe=True)
  print("TABLES Created")
  DATABASE.close()

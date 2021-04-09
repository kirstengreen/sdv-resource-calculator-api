import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict


craftable_item = Blueprint('caftable_items', 'caftable_item')


'''
ROUTES
'''

# GET
@craftable_item.route('/', methods=['GET'])
def get_all_caftable_items():
  try:
    caftable_items = [model_to_dict(craftable_item) for craftable_item in models.CraftableItems.select()]
    # print(caftable_items)
    return jsonify(data=caftable_items, status={'code': 200, 'message': 'Success'})
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'}) 
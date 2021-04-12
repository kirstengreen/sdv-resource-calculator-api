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


# SHOW
@craftable_item.route('/<id>', methods=["GET"])
def get_one_craftable_item(id):
    craftable_item = models.CraftableItems.get_by_id(id)
    # print(craftable_item.__dict__)
    return jsonify(data=model_to_dict(craftable_item), status={"code": 200, "message": "Success"})


# DELETE
# @craftable_item.route('/<id>', methods=["DELETE"])
# def delete_craftable_item(id):
#     query = models.CraftableItems.delete().where(models.CraftableItems.id==id)
#     query.execute()
#     return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})
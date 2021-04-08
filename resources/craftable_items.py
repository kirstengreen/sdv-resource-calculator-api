import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

craftable_items = Blueprint('caftable_items', 'caftable_items')
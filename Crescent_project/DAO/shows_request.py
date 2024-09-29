from flask import request
from database.database import Shows

def shows_request():
    page = request.args.get('page', 1, type=int)
    per_page = 30  
    shows = Shows.query.paginate(page=page, per_page=per_page)
    return shows
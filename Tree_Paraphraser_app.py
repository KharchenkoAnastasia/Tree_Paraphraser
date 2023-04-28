
from flask import Flask, request, jsonify
from TreeParaphraser import *
import json
app = Flask(__name__)


@app.route('/paraphrase', methods=['GET'])
def paraphrase_tree():
    
   
    # Get the tree parameter from the query string
    tree_str = request.args.get('tree')
    if not tree_str:
        return jsonify({'error': 'Tree parameter is missing'}), 400
    paraphraser = TreeParaphraser(tree_str)
    # Get the limit parameter from the query string or use the default value of 20
    limit = int(request.args.get('limit', 20))
    
    # Call the swap_np_children method of the TreeParaphraser class to generate paraphrased trees
    paraphrased_trees = paraphraser.swap_np_children(limit)   
    paraphrases = [{'tree': tree} for tree in paraphrased_trees]
    response = {'paraphrase': paraphrases}
    
       
    json_string = json.dumps(response,ensure_ascii=False, indent=2)
    return json_string

if __name__ == '__main__':
    app.run(port=8080)

import json

import pytest

from label_studio_ml.text_extractor.model import BBOXOCR


@pytest.fixture
def client():
    from _wsgi import init_app

    app = init_app(model_class=BBOXOCR)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_basic_interactions(client):
    # draw first bbox
    response = client.post(
        "/predict",
        json=json.loads(
            '{"tasks": [{"id": 311, "annotations": [], "file_upload": "a79e939b-images.json", "drafts": [], "predictions": [], "data": {"image": "https://s3.amazonaws.com/htx-pub/datasets/images/125135519_415708316105264_2277342140805257509_n.jpg"}, "meta": {}, "created_at": "2024-03-19T23:15:01.004453Z", "updated_at": "2024-03-20T01:55:39.644616Z", "inner_id": 11, "total_annotations": 0, "cancelled_annotations": 0, "total_predictions": 0, "comment_count": 0, "unresolved_comment_count": 0, "last_comment_updated_at": null, "project": 3, "updated_by": 1, "comment_authors": []}], "project": "3.1710890019", "label_config": "<View>    \\n   <Image name=\\"image\\" value=\\"$image\\" zoom=\\"true\\" zoomControl=\\"false\\"\\n         rotateControl=\\"true\\" width=\\"100%\\" height=\\"100%\\"\\n         maxHeight=\\"auto\\" maxWidth=\\"auto\\"/>\\n   \\n   <RectangleLabels name=\\"bbox\\" toName=\\"image\\" strokeWidth=\\"1\\" smart=\\"true\\">\\n      <Label value=\\"Label1\\" background=\\"green\\"/>\\n      <Label value=\\"Label2\\" background=\\"blue\\"/>\\n      <Label value=\\"Label3\\" background=\\"red\\"/>\\n   </RectangleLabels>\\n\\n   <TextArea name=\\"transcription\\" toName=\\"image\\" \\n   editable=\\"true\\" perRegion=\\"true\\" required=\\"false\\" \\n   maxSubmissions=\\"1\\" rows=\\"5\\" placeholder=\\"Recognized Text\\" \\n   displayMode=\\"region-list\\"/>\\n</View>", "params": {"login": null, "password": null, "context": {"result": [{"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "rectanglelabels": ["Label1"]}, "id": "n8NSdVeuJi", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}]}}}'
        ),
    )
    assert response.status_code == 200
    r = response.json
    assert len(r["results"][0]["result"]) == 2
    assert r["results"][0]["result"][0]["value"]["text"][0] == "KENAPA"
    assert r["results"][0]["result"][1]["value"]["rectanglelabels"][0] == "Label1"

    # draw second bbox, same label
    response = client.post(
        "/predict",
        json=json.loads(
            '{"tasks": [{"id": 311, "annotations": [], "file_upload": "a79e939b-images.json", "drafts": [{"id": 22, "user": "heartex@heartex.net", "created_username": "heartex@heartex.net, 1", "created_ago": "15\\u00a0minutes", "result": [{"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "text": ["KENAPA"]}, "id": "n8NSdVeuJi", "from_name": "transcription", "to_name": "image", "type": "textarea", "origin": "manual"}, {"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "rectanglelabels": ["Label1"]}, "id": "n8NSdVeuJi", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}], "lead_time": 10.845, "was_postponed": false, "import_id": null, "created_at": "2024-03-20T02:00:08.156706Z", "updated_at": "2024-03-20T02:00:08.156740Z", "task": 311, "annotation": null}], "predictions": [], "data": {"image": "https://s3.amazonaws.com/htx-pub/datasets/images/125135519_415708316105264_2277342140805257509_n.jpg"}, "meta": {}, "created_at": "2024-03-19T23:15:01.004453Z", "updated_at": "2024-03-20T01:55:39.644616Z", "inner_id": 11, "total_annotations": 0, "cancelled_annotations": 0, "total_predictions": 0, "comment_count": 0, "unresolved_comment_count": 0, "last_comment_updated_at": null, "project": 3, "updated_by": 1, "comment_authors": []}], "project": "3.1710890019", "label_config": "<View>    \\n   <Image name=\\"image\\" value=\\"$image\\" zoom=\\"true\\" zoomControl=\\"false\\"\\n         rotateControl=\\"true\\" width=\\"100%\\" height=\\"100%\\"\\n         maxHeight=\\"auto\\" maxWidth=\\"auto\\"/>\\n   \\n   <RectangleLabels name=\\"bbox\\" toName=\\"image\\" strokeWidth=\\"1\\" smart=\\"true\\">\\n      <Label value=\\"Label1\\" background=\\"green\\"/>\\n      <Label value=\\"Label2\\" background=\\"blue\\"/>\\n      <Label value=\\"Label3\\" background=\\"red\\"/>\\n   </RectangleLabels>\\n\\n   <TextArea name=\\"transcription\\" toName=\\"image\\" \\n   editable=\\"true\\" perRegion=\\"true\\" required=\\"false\\" \\n   maxSubmissions=\\"1\\" rows=\\"5\\" placeholder=\\"Recognized Text\\" \\n   displayMode=\\"region-list\\"/>\\n</View>", "params": {"login": null, "password": null, "context": {"result": [{"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "text": ["KENAPA"]}, "id": "n8NSdVeuJi", "from_name": "transcription", "to_name": "image", "type": "textarea", "origin": "manual"}, {"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "rectanglelabels": ["Label1"]}, "id": "n8NSdVeuJi", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}, {"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 3.082614056720099, "y": 30.997066832169608, "width": 37.237977805178794, "height": 11.747296028752174, "rotation": 0, "rectanglelabels": ["Label1"]}, "id": "zUdI0qX9S6", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}]}}}'
        ),
    )
    assert response.status_code == 200
    r = response.json
    assert len(r["results"][0]["result"]) == 2
    assert r["results"][0]["result"][0]["value"]["text"][0] == "HARUS"
    assert r["results"][0]["result"][1]["value"]["rectanglelabels"][0] == "Label1"

    # draw third bbox, different label
    response = client.post(
        "/predict",
        json=json.loads(
            '{"tasks": [{"id": 311, "annotations": [], "file_upload": "a79e939b-images.json", "drafts": [{"id": 22, "user": "heartex@heartex.net", "created_username": "heartex@heartex.net, 1", "created_ago": "17\\u00a0minutes", "result": [{"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "text": ["KENAPA"]}, "id": "n8NSdVeuJi", "from_name": "transcription", "to_name": "image", "type": "textarea", "origin": "manual"}, {"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.5893958076448826, "y": 15.59725018943566, "width": 44.38964241676942, "height": 12.438313442208186, "rotation": 0, "rectanglelabels": ["Label1"]}, "id": "n8NSdVeuJi", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}, {"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 3.082614056720099, "y": 30.997066832169608, "width": 37.237977805178794, "height": 11.747296028752174, "rotation": 0, "text": ["HARUS"]}, "id": "zUdI0qX9S6", "from_name": "transcription", "to_name": "image", "type": "textarea", "origin": "manual"}, {"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 3.082614056720099, "y": 30.997066832169608, "width": 37.237977805178794, "height": 11.747296028752174, "rotation": 0, "rectanglelabels": ["Label1"]}, "id": "zUdI0qX9S6", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}], "lead_time": 972.868, "was_postponed": false, "import_id": null, "created_at": "2024-03-20T02:00:08.156706Z", "updated_at": "2024-03-20T02:16:10.178811Z", "task": 311, "annotation": null}], "predictions": [], "data": {"image": "https://s3.amazonaws.com/htx-pub/datasets/images/125135519_415708316105264_2277342140805257509_n.jpg"}, "meta": {}, "created_at": "2024-03-19T23:15:01.004453Z", "updated_at": "2024-03-20T01:55:39.644616Z", "inner_id": 11, "total_annotations": 0, "cancelled_annotations": 0, "total_predictions": 0, "comment_count": 0, "unresolved_comment_count": 0, "last_comment_updated_at": null, "project": 3, "updated_by": 1, "comment_authors": []}], "project": "3.1710890019", "label_config": "<View>    \\n   <Image name=\\"image\\" value=\\"$image\\" zoom=\\"true\\" zoomControl=\\"false\\"\\n         rotateControl=\\"true\\" width=\\"100%\\" height=\\"100%\\"\\n         maxHeight=\\"auto\\" maxWidth=\\"auto\\"/>\\n   \\n   <RectangleLabels name=\\"bbox\\" toName=\\"image\\" strokeWidth=\\"1\\" smart=\\"true\\">\\n      <Label value=\\"Label1\\" background=\\"green\\"/>\\n      <Label value=\\"Label2\\" background=\\"blue\\"/>\\n      <Label value=\\"Label3\\" background=\\"red\\"/>\\n   </RectangleLabels>\\n\\n   <TextArea name=\\"transcription\\" toName=\\"image\\" \\n   editable=\\"true\\" perRegion=\\"true\\" required=\\"false\\" \\n   maxSubmissions=\\"1\\" rows=\\"5\\" placeholder=\\"Recognized Text\\" \\n   displayMode=\\"region-list\\"/>\\n</View>", "params": {"login": null, "password": null, "context": {"result": [{"original_width": 1080, "original_height": 1349, "image_rotation": 0, "value": {"x": 2.7127003699136867, "y": 45.113565421342386, "width": 37.60789149198521, "height": 12.142163122155608, "rotation": 0, "rectanglelabels": ["Label2"]}, "id": "uzDKSm-XGv", "from_name": "bbox", "to_name": "image", "type": "rectanglelabels", "origin": "manual"}]}}}'
        ),
    )
    assert response.status_code == 200
    r = response.json
    assert len(r["results"][0]["result"]) == 2
    assert r["results"][0]["result"][0]["value"]["text"][0] == "PUNYA"
    assert r["results"][0]["result"][1]["value"]["rectanglelabels"][0] == "Label2"

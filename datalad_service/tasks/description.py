import difflib
import json
import os
from datalad_service.common.celery import dataset_task
from datalad_service.tasks.files import commit_files


def edit_description(description, new_fields):
    updated = description.copy()
    updated.update(new_fields)
    return updated


@dataset_task
def update_description(store, dataset, description_fields, name=None, email=None):
    ds = store.get_dataset(dataset)
    description = ds.repo.repo.tree(
        'HEAD')['dataset_description.json'].data_stream.read().decode('utf-8')
    description_json = json.loads(description)
    if description_json.get('License') != 'CC0':
        description_fields = edit_description(
            description_fields, {'License': 'CC0'})
    if description_fields is not None and any(description_fields):
        updated = edit_description(description_json, description_fields)
        path = os.path.join(store.get_dataset_path(
            dataset), 'dataset_description.json')
        # newline='' disables universal newlines since we just want to compare decoded bytes
        with open(path, 'r+', encoding='utf-8', newline='') as description_file:
            description_file_contents = description_file.read()
            if description != description_file_contents:
                raise Exception('unexpected dataset_description.json contents')
            description_file.seek(0)
            description_file.truncate(0)
            description_file.write(json.dumps(updated, indent=4))
        # Commit new content, run validator
        commit_files.run(store.annex_path, dataset, [
                         'dataset_description.json'])
        return updated
    else:
        return description_json
